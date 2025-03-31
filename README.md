---

<h1 align="center">Blum Bot</h1>

<p align="center">Automate tasks in Blum to enhance your efficiency and maximize your rewards!</p>

---

## 🚀 About the Bot

Blum Bot is designed to automate various tasks in **Blum**, helping you:

- **🌾 Auto Farming:**  
  Automate your farming process to maximize in-game rewards.

- **🛠️ Auto Task:**  
  Automatically execute tasks and claim rewards.

- **📆 Auto Daily:**  
  Check and claim your daily rewards (including friend reward claims) without manual intervention.

- **🎮 Auto Game:**  
  Play games automatically to earn points within your configured range.

Additionally, Blum Bot offers advanced features such as:

- **👥 Multi-Account Support:**  
  Manage multiple accounts simultaneously.

- **🧵 Multi-Threading Support:**  
  Process multiple accounts concurrently according to your configuration.

- **🔌 Proxy Support:**  
  Dynamically assign proxies for each account.

- **⏱️ Delay Loop and Account Switching:**  
  Configure delay intervals for looping and switching accounts to optimize performance.

---

## 🌟 Version v1.1.3

### Updates

1. Fixed a bug where the script was not working on some devices.
2. Added a new solver for the latest quest from Blum.

---

### **Features in This Version:**

- **🌾 Auto Farming:** Automatically handle farming sessions and reward claims.
- **🛠️ Auto Task:** Execute and claim available tasks automatically.
- **📆 Auto Daily:** Check and claim daily rewards along with friend rewards seamlessly.
- **🎮 Auto Game:** Automatically play games and claim points within your defined range.
- **👥 Multi-Account Support:** Manage multiple accounts simultaneously.
- **🧵 Multi-Threading Support:** Process multiple accounts concurrently with adjustable thread settings.
- **🔌 Proxy Support:** Dynamically assign proxies for each account.
- **⏱️ Delay Loop and Account Switching:** Set custom intervals for looping and account transitions.

---

## ⚙️ Configuration in `config.json`

```json
{
  "game": true,
  "daily": true,
  "task": true,
  "farming": true,
  "low_point": 260,
  "high_point": 280,
  "thread": 1,
  "proxy": false,
  "delay_account_switch": 10,
  "delay_loop": 3000
}
```

| **Function**           | **Description**                                                                     | **Default** |
| ---------------------- | ----------------------------------------------------------------------------------- | ----------- |
| `game`                 | Automate game play to earn points (randomized between `low_point` and `high_point`) | `true`      |
| `daily`                | Automate daily reward check & claim, including friend reward claim                  | `true`      |
| `task`                 | Automate task execution and reward claims                                           | `true`      |
| `farming`              | Automate farming sessions and reward claims                                         | `true`      |
| `low_point`            | Minimum points for auto game reward (used for randomization)                        | `260`       |
| `high_point`           | Maximum points for auto game reward (used for randomization)                        | `280`       |
| `thread`               | Number of concurrent threads (accounts) to process                                  | `1`         |
| `proxy`                | Enable/Disable proxy usage                                                          | `false`     |
| `delay_account_switch` | Delay between account switches (in seconds)                                         | `10`        |
| `delay_loop`           | Delay before the next loop iteration (in milliseconds)                              | `3000`      |

---

## 📥 How to Register

Start using Blum Bot by registering through the link below:

<div align="center">
  <a href="https://t.me/blum/app?startapp=ref_voyTtORCbG" target="_blank">
    <img src="https://img.shields.io/static/v1?message=Blum&logo=telegram&label=&color=2CA5E0&logoColor=white&style=for-the-badge" height="25" alt="Telegram Logo" />
  </a>
</div>

---

## 📖 Installation Steps

1. **Clone the Repository**  
   Copy the project to your local machine:

   ```bash
   git clone https://github.com/pazdzioch78/blum-bot3.git
   ```

2. **Navigate to the Project Folder**  
   Move to the project directory:

   ```bash
   cd blum-bot
   ```

3. **Install Dependencies**  
   Install the required libraries:

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Query**  
   Create a `query.txt` file and add your Blum query data.

5. **Set Up Proxy (Optional)**  
   To use a proxy, create a `proxy.txt` file and add proxies in the format:

   ```
   http://username:password@ip:port
   ```

   - Only HTTP and HTTPS proxies are supported.

6. **Run the Bot**  
   Execute the bot using the following command:

   ```bash
   python main.py
   ```

---

### 🔹 Want Free Proxies?

You can obtain free proxies from [Webshare.io](https://www.webshare.io/).

---

## 🛠️ Contributing

This project is developed by **Livexords**. If you have suggestions, questions, or would like to contribute, feel free to contact us:

<div align="center">
  <a href="https://t.me/blum/app?startapp=ref_voyTtORCbG" target="_blank">
    <img src="https://img.shields.io/static/v1?message=Livexords&logo=telegram&label=&color=2CA5E0&logoColor=white&style=for-the-badge" height="25" alt="Telegram Logo" />
  </a>
</div>

---

## 🙌 Contributors

- @Baronzs103
- @bioganteng14

---
