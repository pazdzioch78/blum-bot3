from datetime import datetime
import json
import time
from colorama import Fore
import requests
import random


class blum:
    BASE_URL = "https://user-domain.blum.codes/api/v1/"
    HEADERS = {
        "accept": "application/json, text/plain, */*",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "en-GB,en;q=0.9,en-US;q=0.8",
        "origin": "https://telegram.blum.codes",
        "referer": "https://telegram.blum.codes/",
        "priority": "u=1, i", 
        "sec-ch-ua": '"Microsoft Edge";v="134", "Chromium";v="134", "Not:A-Brand";v="24", "Microsoft Edge WebView2";v="134"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0",
    }

    def __init__(self):
        self.query_list = self.load_query("query.txt")
        self.token = None
        self.config = self.load_config()

    def banner(self) -> None:
        """Displays the banner for the bot."""
        self.log("🎉 Blum Free Bot", Fore.CYAN)
        self.log("🚀 Created by LIVEXORDS", Fore.CYAN)
        self.log("📢 Channel: t.me/livexordsscript\n", Fore.CYAN)

    def log(self, message, color=Fore.RESET):
        safe_message = message.encode("utf-8", "backslashreplace").decode("utf-8")
        print(
            Fore.LIGHTBLACK_EX
            + datetime.now().strftime("[%Y:%m:%d ~ %H:%M:%S] |")
            + " "
            + color
            + safe_message
            + Fore.RESET
        )

    def load_config(self) -> dict:
        """
        Loads configuration from config.json.

        Returns:
            dict: Configuration data or an empty dictionary if an error occurs.
        """
        try:
            with open("config.json", "r") as config_file:
                config = json.load(config_file)
                self.log("✅ Configuration loaded successfully.", Fore.GREEN)
                return config
        except FileNotFoundError:
            self.log("❌ File not found: config.json", Fore.RED)
            return {}
        except json.JSONDecodeError:
            self.log(
                "❌ Failed to parse config.json. Please check the file format.",
                Fore.RED,
            )
            return {}

    def load_query(self, path_file: str = "query.txt") -> list:
        """
        Loads a list of queries from the specified file.

        Args:
            path_file (str): The path to the query file. Defaults to "query.txt".

        Returns:
            list: A list of queries or an empty list if an error occurs.
        """
        self.banner()

        try:
            with open(path_file, "r") as file:
                queries = [line.strip() for line in file if line.strip()]

            if not queries:
                self.log(f"⚠️ Warning: {path_file} is empty.", Fore.YELLOW)

            self.log(f"✅ Loaded {len(queries)} queries from {path_file}.", Fore.GREEN)
            return queries

        except FileNotFoundError:
            self.log(f"❌ File not found: {path_file}", Fore.RED)
            return []
        except Exception as e:
            self.log(f"❌ Unexpected error loading queries: {e}", Fore.RED)
            return []

    def login(self, index: int) -> None:
        self.log("🔐 Attempting to log in...", Fore.GREEN)
        if index >= len(self.query_list):
            self.log("❌ Invalid login index. Please check again.", Fore.RED)
            return

        token = self.query_list[index]
        self.log(f"📋 Using token: {token[:10]}... (truncated for security)", Fore.CYAN)

        # API 1: Login via Telegram Mini App
        login_url = f"{self.BASE_URL}auth/provider/PROVIDER_TELEGRAM_MINI_APP"
        payload = json.dumps({"query": token})
        login_headers = {
            "accept": "application/json, text/plain, */*",
            "accept-language": "en-US,en;q=0.9",
            "content-type": "application/json",
            "origin": "https://telegram.blum.codes",
            "priority": "u=1, i",
            "referer": "https://telegram.blum.codes/"
        }

        try:
            self.log("📡 Sending login request...", Fore.CYAN)
            login_response = requests.post(login_url, headers=login_headers, data=payload)
            login_response.raise_for_status()
            login_data = login_response.json()
        except requests.exceptions.RequestException as e:
            self.log(f"❌ Failed to send login request: {e}", Fore.RED)
            try:
                self.log(f"📄 Response content: {login_response.text}", Fore.RED)
            except Exception:
                pass
            return
        except Exception as e:
            self.log(f"❌ Unexpected error during login: {e}", Fore.RED)
            try:
                self.log(f"📄 Response content: {login_response.text}", Fore.RED)
            except Exception:
                pass
            return

        # Proses respons login agar tidak tampil mentah
        try:
            token_data = login_data.get("token", {})
            access_token = token_data.get("access", "")

            # Simpan token refresh untuk digunakan di API berikutnya
            self.token = access_token

            self.log("✅ Login successful! Processed login response", Fore.GREEN)
        except Exception as e:
            self.log(f"❌ Error processing login response: {e}", Fore.RED)
            return

        # API 2: Mendapatkan informasi user via /user/me
        user_me_url = f"{self.BASE_URL}user/me"
        user_me_headers = {**self.HEADERS, "authorization": f"Bearer {self.token}"}
        try:
            self.log("📡 Sending user info request...", Fore.CYAN)
            user_me_response = requests.get(user_me_url, headers=user_me_headers)
            user_me_response.raise_for_status()
            user_me_data = user_me_response.json()

            # Proses respons user/me
            u_id = user_me_data.get("id", {}).get("id", "N/A")
            u_name = user_me_data.get("username", "N/A")
            referrer_token = user_me_data.get("referrerToken", "N/A")
            u_created_at = user_me_data.get("createdAt", "N/A")

            self.log("👤 User Info:", Fore.GREEN)
            self.log(f"    - ID: {u_id}", Fore.CYAN)
            self.log(f"    - Username: {u_name}", Fore.CYAN)
            self.log(f"    - Referrer Token: {referrer_token}", Fore.CYAN)
            self.log(f"    - Created At: {u_created_at}", Fore.CYAN)
        except requests.exceptions.RequestException as e:
            self.log(f"❌ Failed to fetch user info: {e}", Fore.RED)
            try:
                self.log(f"📄 Response content: {user_me_response.text}", Fore.RED)
            except Exception:
                pass
        except Exception as e:
            self.log(f"❌ Unexpected error in user info request: {e}", Fore.RED)
            try:
                self.log(f"📄 Response content: {user_me_response.text}", Fore.RED)
            except Exception:
                pass

        # API 3: Mendapatkan saldo friends via /friends/balance
        friends_balance_url = f"{self.BASE_URL}friends/balance"
        user_balance_headers = {**self.HEADERS, "authorization": f"Bearer {self.token}"}
        try:
            self.log("📡 Sending friends balance request...", Fore.CYAN)
            friends_response = requests.get(friends_balance_url, headers=user_balance_headers)
            friends_response.raise_for_status()
            friends_data = friends_response.json()

            # Proses respons friends balance
            limit_inv = friends_data.get("limitInvitation", "N/A")
            used_inv = friends_data.get("usedInvitation", "N/A")
            amount_for_claim = friends_data.get("amountForClaim", "N/A")
            referral_token = friends_data.get("referralToken", "N/A")
            percent_friends = friends_data.get("percentFromFriends", "N/A")
            percent_friends_friends = friends_data.get("percentFromFriendsOfFriends", "N/A")
            can_claim = friends_data.get("canClaim", "N/A")
            enable_new_balance = friends_data.get("enableNewBalance", "N/A")

            self.log("💰 Friends Balance:", Fore.GREEN)
            self.log(f"    - Limit Invitation: {limit_inv}", Fore.CYAN)
            self.log(f"    - Used Invitation: {used_inv}", Fore.CYAN)
            self.log(f"    - Amount For Claim: {amount_for_claim}", Fore.CYAN)
            self.log(f"    - Referral Token: {referral_token}", Fore.CYAN)
            self.log(f"    - Percent From Friends: {percent_friends}", Fore.CYAN)
            self.log(f"    - Percent From Friends Of Friends: {percent_friends_friends}", Fore.CYAN)
            self.log(f"    - Can Claim: {can_claim}", Fore.CYAN)
            self.log(f"    - Enable New Balance: {enable_new_balance}", Fore.CYAN)
        except requests.exceptions.RequestException as e:
            self.log(f"❌ Failed to fetch friends balance: {e}", Fore.RED)
            try:
                self.log(f"📄 Response content: {friends_response.text}", Fore.RED)
            except Exception:
                pass
        except Exception as e:
            self.log(f"❌ Unexpected error in friends balance request: {e}", Fore.RED)
            try:
                self.log(f"📄 Response content: {friends_response.text}", Fore.RED)
            except Exception:
                pass
    
    def daily(self) -> None:
        import time
        self.log("🔄 Attempting to check daily reward...", Fore.GREEN)
        
        daily_url = "https://game-domain.blum.codes/api/v2/daily-reward"
        daily_headers = {**self.HEADERS, "authorization": f"Bearer {self.token}"}
        
        # API 1: GET reward info
        try:
            self.log("📡 Sending GET daily reward request...", Fore.CYAN)
            response = requests.get(daily_url, headers=daily_headers)
            response.raise_for_status()
            data = response.json()
        except requests.exceptions.RequestException as e:
            self.log(f"❌ Failed to fetch daily reward info: {e}", Fore.RED)
            try:
                self.log(f"📄 Response content: {response.text}", Fore.RED)
            except Exception:
                pass
            return
        except Exception as e:
            self.log(f"❌ Unexpected error during GET daily reward: {e}", Fore.RED)
            try:
                self.log(f"📄 Response content: {response.text}", Fore.RED)
            except Exception:
                pass
            return

        try:
            claim_status = data.get("claim", "N/A")
            current_streak = data.get("currentStreakDays", "N/A")
            today_reward = data.get("todayReward", {})
            can_claim_at = data.get("canClaimAt", None)
            
            self.log("✅ Daily reward info received:", Fore.GREEN)
            self.log(f"    - Claim: {claim_status}", Fore.CYAN)
            self.log(f"    - Current Streak Days: {current_streak}", Fore.CYAN)
            self.log(f"    - Today's Reward: {today_reward}", Fore.CYAN)
            self.log(f"    - Can Claim At: {can_claim_at}", Fore.CYAN)
        except Exception as e:
            self.log(f"❌ Error processing daily reward info: {e}", Fore.RED)
            return

        # Cek apakah saat ini sudah waktunya untuk claim reward
        current_time = int(time.time() * 1000)
        self.log(f"⏰ Device current time: {current_time}", Fore.CYAN)
        
        if can_claim_at is None:
            self.log("❌ 'canClaimAt' not found in response.", Fore.RED)
            return

        if current_time < int(can_claim_at):
            self.log("⏳ Reward is not claimable yet. Please wait until the claim time.", Fore.YELLOW)
            return

        # API 2: Jika sudah waktunya, claim reward dengan POST
        try:
            self.log("🚀 Claiming daily reward...", Fore.CYAN)
            claim_response = requests.post(daily_url, headers=daily_headers)
            claim_response.raise_for_status()
            claim_data = claim_response.json()
            self.log("✅ Daily reward claimed successfully:", Fore.GREEN)
            self.log(f"    - Response: {claim_data}", Fore.CYAN)
        except requests.exceptions.RequestException as e:
            self.log(f"❌ Failed to claim daily reward: {e}", Fore.RED)
            try:
                self.log(f"📄 Response content: {claim_response.text}", Fore.RED)
            except Exception:
                pass
        except Exception as e:
            self.log(f"❌ Unexpected error during claiming daily reward: {e}", Fore.RED)
            try:
                self.log(f"📄 Response content: {claim_response.text}", Fore.RED)
            except Exception:
                pass

    def task(self) -> None:
        import time
        import json
        import requests

        self.log("🚀 Fetching tasks...", Fore.GREEN)
        tasks_url = "https://earn-domain.blum.codes/api/v1/tasks"
        headers = {**self.HEADERS, "authorization": f"Bearer {self.token}"}

        # Ambil mapping keyword dari GitHub
        task_json_url = "https://raw.githubusercontent.com/livexords-nw/blum-bot/refs/heads/main/task.json"
        try:
            self.log("🔑 Loading task keyword mapping from GitHub...", Fore.GREEN)
            task_response = requests.get(task_json_url)
            task_response.raise_for_status()
            keyword_mapping = task_response.json()
            self.log("✅ Loaded task keyword mapping from GitHub", Fore.GREEN)
        except Exception as e:
            self.log(f"❌ Failed to load task keyword mapping from GitHub: {e}", Fore.RED)
            keyword_mapping = {}

        # Ambil daftar tasks
        try:
            tasks_response = requests.get(tasks_url, headers=headers)
            tasks_response.raise_for_status()
            tasks_list = tasks_response.json()
        except requests.exceptions.RequestException as e:
            self.log(f"❌ Failed to fetch tasks: {e}", Fore.RED)
            try:
                self.log(f"📄 Response content: {tasks_response.text}", Fore.RED)
            except Exception:
                pass
            return
        except Exception as e:
            self.log(f"❌ Unexpected error when fetching tasks: {e}", Fore.RED)
            return

        self.log(f"✅ Fetched tasks. Total sections: {len(tasks_list)}", Fore.GREEN)
        
        # Ekstrak semua tasks (termasuk subTasks dan subSections)
        tasks_to_process = []

        def extract_tasks(section: dict) -> None:
            if "tasks" in section and isinstance(section["tasks"], list):
                for task in section["tasks"]:
                    tasks_to_process.append(task)
                    if "subTasks" in task and isinstance(task["subTasks"], list):
                        for sub in task["subTasks"]:
                            tasks_to_process.append(sub)
            if "subSections" in section and isinstance(section["subSections"], list):
                for sub_section in section["subSections"]:
                    extract_tasks(sub_section)

        for section in tasks_list:
            extract_tasks(section)

        self.log(f"👉 Found {len(tasks_to_process)} tasks in total.", Fore.GREEN)

        # Kategorisasi task berdasarkan status
        tasks_to_start = []
        tasks_to_verify = []
        tasks_to_claim = []

        for task_item in tasks_to_process:
            status = task_item.get("status", "").upper()
            if status == "NOT_STARTED":
                tasks_to_start.append(task_item)
            elif status == "READY_FOR_VERIFY":
                tasks_to_verify.append(task_item)
            elif status == "READY_FOR_CLAIM":
                tasks_to_claim.append(task_item)
            else:
                self.log(f"ℹ️ Task {task_item.get('id')} has status '{status}' - no action required.", Fore.YELLOW)

        self.log(f"👉 Tasks to start: {len(tasks_to_start)}", Fore.GREEN)
        self.log(f"👉 Tasks to verify: {len(tasks_to_verify)}", Fore.GREEN)
        self.log(f"👉 Tasks to claim: {len(tasks_to_claim)}", Fore.GREEN)

        # 1. Proses task dengan status NOT_STARTED: Start task
        for task_item in tasks_to_start:
            task_id = task_item.get("id")
            if not task_id:
                continue
            start_url = f"https://earn-domain.blum.codes/api/v1/tasks/{task_id}/start"
            try:
                self.log(f"🚀 Starting task {task_id}...", Fore.CYAN)
                start_response = requests.post(start_url, headers=headers)
                start_response.raise_for_status()
                self.log(f"✅ Task {task_id} started.", Fore.GREEN)
            except requests.exceptions.RequestException as e:
                self.log(f"❌ Failed to start task {task_id}: {e}", Fore.RED)
                try:
                    self.log(f"📄 Response content: {start_response.text}", Fore.RED)
                except Exception:
                    pass
            except Exception as e:
                self.log(f"❌ Unexpected error when starting task {task_id}: {e}", Fore.RED)

        # 2. Proses task dengan status READY_FOR_VERIFY: Verify task
        for task_item in tasks_to_verify:
            task_id = task_item.get("id")
            if not task_id:
                continue
            verify_url = f"https://earn-domain.blum.codes/api/v1/tasks/{task_id}/validate"
            payload = {}
            if task_item.get("validationType", "").upper() == "KEYWORD":
                # Cari keyword dari mapping yang diambil dari GitHub
                keyword = keyword_mapping.get(task_id)
                if keyword:
                    payload = {"keyword": keyword}
                else:
                    self.log(f"❌ Keyword not found for task {task_id} in mapping.", Fore.RED)
                    continue  # Lewati verifikasi jika keyword tidak ditemukan
            try:
                self.log(f"🛠 Verifying task {task_id}...", Fore.CYAN)
                if payload:
                    verify_response = requests.post(verify_url, headers=headers, json=payload)
                else:
                    verify_response = requests.post(verify_url, headers=headers)
                verify_response.raise_for_status()
                verify_data = verify_response.json()
                self.log(f"✅ Task {task_id} verified. Response: {verify_data}", Fore.GREEN)
            except requests.exceptions.RequestException as e:
                self.log(f"❌ Failed to verify task {task_id}: {e}", Fore.RED)
                try:
                    self.log(f"📄 Response content: {verify_response.text}", Fore.RED)
                except Exception:
                    pass
            except Exception as e:
                self.log(f"❌ Unexpected error when verifying task {task_id}: {e}", Fore.RED)

        # Delay 5 detik sebelum claim
        self.log("⏳ Waiting 5 seconds before claiming tasks...", Fore.YELLOW)
        time.sleep(5)

        # 3. Proses task dengan status READY_FOR_CLAIM: Claim task
        for task_item in tasks_to_claim:
            task_id = task_item.get("id")
            if not task_id:
                continue
            claim_url = f"https://earn-domain.blum.codes/api/v1/tasks/{task_id}/claim"
            try:
                self.log(f"💰 Claiming task {task_id}...", Fore.CYAN)
                claim_response = requests.post(claim_url, headers=headers)
                claim_response.raise_for_status()
                claim_data = claim_response.json()
                self.log(f"✅ Task {task_id} claimed. Response: {claim_data}", Fore.GREEN)
            except requests.exceptions.RequestException as e:
                self.log(f"❌ Failed to claim task {task_id}: {e}", Fore.RED)
                try:
                    self.log(f"📄 Response content: {claim_response.text}", Fore.RED)
                except Exception:
                    pass
            except Exception as e:
                self.log(f"❌ Unexpected error when claiming task {task_id}: {e}", Fore.RED)
                
    def farming(self) -> None:
        import time
        import requests

        self.log("🚜 Starting farming process...", Fore.GREEN)
        
        # Header yang akan digunakan (authorization ditambahkan)
        headers = {**self.HEADERS, "authorization": f"Bearer {self.token}"}
        
        # Step 1: Ambil informasi wallet points balance
        balance_url = "https://wallet-domain.blum.codes/api/v1/wallet/my/points/balance"
        try:
            self.log("📡 Fetching wallet points balance...", Fore.CYAN)
            balance_response = requests.get(balance_url, headers=headers)
            balance_response.raise_for_status()
            balance_data = balance_response.json()
        except requests.exceptions.RequestException as e:
            self.log(f"❌ Failed to fetch wallet points balance: {e}", Fore.RED)
            try:
                self.log(f"📄 Response content: {balance_response.text}", Fore.RED)
            except Exception:
                pass
            return
        except Exception as e:
            self.log(f"❌ Unexpected error fetching wallet points balance: {e}", Fore.RED)
            return

        # Cari data Blum points berdasarkan currencyId yang spesifik
        blum_points = None
        for point in balance_data.get("points", []):
            if point.get("currencyId") == "59bee2e3-a682-4ec5-93df-a3bb294f7bed":
                blum_points = point
                break
        if not blum_points:
            self.log("❌ Blum points data not found in wallet points balance.", Fore.RED)
            return

        # Ekstrak informasi farming dari Blum points
        farming_info = blum_points.get("farming")
        if not farming_info:
            self.log("❌ Farming info not available in Blum points data.", Fore.RED)
            return

        start_time = farming_info.get("startTime", "N/A")
        end_time = farming_info.get("endTime", "N/A")
        server_current_time = farming_info.get("currentTime", "N/A")
        earnings_rate = farming_info.get("earningsRate", "N/A")
        farming_balance = farming_info.get("balance", "N/A")
        
        self.log("📊 Farming Info:", Fore.GREEN)
        self.log(f"    - Start Time: {start_time}", Fore.CYAN)
        self.log(f"    - End Time: {end_time}", Fore.CYAN)
        self.log(f"    - Server Current Time: {server_current_time}", Fore.CYAN)
        self.log(f"    - Earnings Rate: {earnings_rate}", Fore.CYAN)
        self.log(f"    - Farming Balance: {farming_balance}", Fore.CYAN)

        # Gunakan waktu dari device (dalam ms)
        current_device_time = int(time.time() * 1000)
        self.log(f"⏰ Device current time: {current_device_time}", Fore.CYAN)
        
        try:
            end_time_int = int(end_time)
        except Exception:
            self.log("❌ Invalid end time in farming info.", Fore.RED)
            return

        # Jika waktu device sudah mencapai atau melebihi endTime, klaim farming reward
        if current_device_time >= end_time_int:
            claim_url = "https://wallet-domain.blum.codes/api/v1/farming/claim"
            try:
                self.log("🚜 Claiming farming reward...", Fore.CYAN)
                claim_response = requests.post(claim_url, headers=headers)
                claim_response.raise_for_status()
                claim_data = claim_response.json()
                self.log("✅ Farming reward claimed:", Fore.GREEN)
                self.log(f"    - Available Balance: {claim_data.get('availableBalance', 'N/A')}", Fore.CYAN)
                self.log(f"    - Play Passes: {claim_data.get('playPasses', 'N/A')}", Fore.CYAN)
                self.log(f"    - Is Fast Farming Enabled: {claim_data.get('isFastFarmingEnabled', 'N/A')}", Fore.CYAN)
                self.log(f"    - Timestamp: {claim_data.get('timestamp', 'N/A')}", Fore.CYAN)
            except requests.exceptions.RequestException as e:
                self.log(f"❌ Failed to claim farming reward: {e}", Fore.RED)
                try:
                    self.log(f"📄 Response content: {claim_response.text}", Fore.RED)
                except Exception:
                    pass
        else:
            # Jika belum waktunya untuk klaim, mulai sesi farming baru
            start_url = "https://wallet-domain.blum.codes/api/v1/farming/start"
            try:
                self.log("🚜 Starting farming session...", Fore.CYAN)
                start_response = requests.post(start_url, headers=headers)
                start_response.raise_for_status()
                start_data = start_response.json()
                self.log("✅ Farming session started:", Fore.GREEN)
                self.log(f"    - Start Time: {start_data.get('startTime', 'N/A')}", Fore.CYAN)
                self.log(f"    - End Time: {start_data.get('endTime', 'N/A')}", Fore.CYAN)
                self.log(f"    - Current Time: {start_data.get('currentTime', 'N/A')}", Fore.CYAN)
                self.log(f"    - Earnings Rate: {start_data.get('earningsRate', 'N/A')}", Fore.CYAN)
                self.log(f"    - Balance: {start_data.get('balance', 'N/A')}", Fore.CYAN)
            except requests.exceptions.RequestException as e:
                self.log(f"❌ Failed to start farming session: {e}", Fore.RED)
                try:
                    self.log(f"📄 Response content: {start_response.text}", Fore.RED)
                except Exception:
                    pass

    def load_proxies(self, filename="proxy.txt"):
        """
        Reads proxies from a file and returns them as a list.

        Args:
            filename (str): The path to the proxy file.

        Returns:
            list: A list of proxy addresses.
        """
        try:
            with open(filename, "r", encoding="utf-8") as file:
                proxies = [line.strip() for line in file if line.strip()]
            if not proxies:
                raise ValueError("Proxy file is empty.")
            return proxies
        except Exception as e:
            self.log(f"❌ Failed to load proxies: {e}", Fore.RED)
            return []

    def set_proxy_session(self, proxies: list) -> requests.Session:
        """
        Creates a requests session with a working proxy from the given list.

        If a chosen proxy fails the connectivity test, it will try another proxy
        until a working one is found. If no proxies work or the list is empty, it
        will return a session with a direct connection.

        Args:
            proxies (list): A list of proxy addresses (e.g., "http://proxy_address:port").

        Returns:
            requests.Session: A session object configured with a working proxy,
                            or a direct connection if none are available.
        """
        # If no proxies are provided, use a direct connection.
        if not proxies:
            self.log("⚠️ No proxies available. Using direct connection.", Fore.YELLOW)
            self.proxy_session = requests.Session()
            return self.proxy_session

        # Copy the list so that we can modify it without affecting the original.
        available_proxies = proxies.copy()

        while available_proxies:
            proxy_url = random.choice(available_proxies)
            self.proxy_session = requests.Session()
            self.proxy_session.proxies = {"http": proxy_url, "https": proxy_url}

            try:
                test_url = "https://httpbin.org/ip"
                response = self.proxy_session.get(test_url, timeout=5)
                response.raise_for_status()
                origin_ip = response.json().get("origin", "Unknown IP")
                self.log(
                    f"✅ Using Proxy: {proxy_url} | Your IP: {origin_ip}", Fore.GREEN
                )
                return self.proxy_session
            except requests.RequestException as e:
                self.log(f"❌ Proxy failed: {proxy_url} | Error: {e}", Fore.RED)
                # Remove the failed proxy and try again.
                available_proxies.remove(proxy_url)

        # If none of the proxies worked, use a direct connection.
        self.log("⚠️ All proxies failed. Using direct connection.", Fore.YELLOW)
        self.proxy_session = requests.Session()
        return self.proxy_session

    def override_requests(self):
        import random
        """Override requests functions globally when proxy is enabled."""
        if self.config.get("proxy", False):
            self.log("[CONFIG] 🛡️ Proxy: ✅ Enabled", Fore.YELLOW)
            proxies = self.load_proxies()
            self.set_proxy_session(proxies)

            # Override request methods
            requests.get = self.proxy_session.get
            requests.post = self.proxy_session.post
            requests.put = self.proxy_session.put
            requests.delete = self.proxy_session.delete
        else:
            self.log("[CONFIG] proxy: ❌ Disabled", Fore.RED)
            # Restore original functions if proxy is disabled
            requests.get = self._original_requests["get"]
            requests.post = self._original_requests["post"]
            requests.put = self._original_requests["put"]
            requests.delete = self._original_requests["delete"]


if __name__ == "__main__":
    blu = blum()
    index = 0
    max_index = len(blu.query_list)
    config = blu.load_config()
    if config.get("proxy", False):
        proxies = blu.load_proxies()

    blu.log(
        "🎉 [LIVEXORDS] === Welcome to Blum Automation === [LIVEXORDS]", Fore.YELLOW
    )
    blu.log(f"📂 Loaded {max_index} accounts from query list.", Fore.YELLOW)

    while True:
        current_account = blu.query_list[index]
        display_account = (
            current_account[:10] + "..."
            if len(current_account) > 10
            else current_account
        )

        blu.log(
            f"👤 [ACCOUNT] Processing account {index + 1}/{max_index}: {display_account}",
            Fore.YELLOW,
        )

        if config.get("proxy", False):
            blu.override_requests()
        else:
            blu.log("[CONFIG] Proxy: ❌ Disabled", Fore.RED)

        blu.login(index)

        blu.log("🛠️ Starting task execution...")
        tasks = {
            "daily": "auto daily",
            "task": "Automatically solving tasks 🤖",
            "farming": "Automatic farming for abundant harvest 🌾",
        }

        for task_key, task_name in tasks.items():
            task_status = config.get(task_key, False)
            blu.log(
                f"[CONFIG] {task_name}: {'✅ Enabled' if task_status else '❌ Disabled'}",
                Fore.YELLOW if task_status else Fore.RED,
            )

            if task_status:
                blu.log(f"🔄 Executing {task_name}...")
                getattr(blu, task_key)()

        if index == max_index - 1:
            blu.log("🔁 All accounts processed. Restarting loop.")
            blu.log(
                f"⏳ Sleeping for {config.get('delay_loop', 30)} seconds before restarting."
            )
            time.sleep(config.get("delay_loop", 30))
            index = 0
        else:
            blu.log(
                f"➡️ Switching to the next account in {config.get('delay_account_switch', 10)} seconds."
            )
            time.sleep(config.get("delay_account_switch", 10))
            index += 1
