Berikut adalah contoh README yang telah dimodifikasi sesuai instruksi:

---

<h1 align="center">Blum Bot</h1>

<p align="center">Automate tasks in Blum to enhance your efficiency and maximize your rewards!</p>

---

## 🚀 **About the Bot**

The Blum Bot is designed to automate various tasks in **Blum**, including:

- **Auto Farming:** Automate your farming process to maximize in-game rewards.
- **Auto Task:** Automatically execute tasks and claim rewards.
- **Auto Daily:** Claim your daily rewards without manual intervention.

Additionally, the bot offers advanced features such as:

- **Multi-Account Support:** Manage multiple accounts simultaneously.
- **Proxy Support:** Dynamically assign proxies for each account.
- **Delay Loop and Account Switching:** Configure delay intervals for looping and switching accounts to optimize performance.

---

## 🌟 Version v1.0.0

### Updates

- **Core Feature Update:**  
  Now with integrated support for Auto Farming, Auto Task, and Auto Daily, Blum Bot streamlines your routine operations.  
- **Enhanced Automation:**  
  The bot now automates the most critical tasks, reducing manual effort and increasing efficiency.

---

### **Features in This Version:**

- **Auto Farming:** Automatically handle farming sessions and reward claims.
- **Auto Task:** Execute and claim available tasks automatically.
- **Auto Daily:** Check and claim daily rewards based on your schedule.
- **Multi-Account Support:** Manage multiple accounts simultaneously.
- **Proxy Support:** Dynamically assign proxies for each account.
- **Delay Loop and Account Switching:** Set custom intervals for looping and account transitions.

---

## ⚙️ **Configuration in `config.json`**

```json
{
    "daily": true,
    "task": true,
    "farming": true,
    "proxy": false,
    "delay_account_switch": 10,
    "delay_loop": 3000
}
```

| **Function**             | **Description**                                    | **Default** |
| ------------------------ | -------------------------------------------------- | ----------- |
| `daily`                  | Automate daily reward claims                       | `true`      |
| `task`                   | Automate task execution and reward claims          | `true`      |
| `farming`                | Automate farming sessions and reward claims        | `true`      |
| `proxy`                  | Enable/Disable proxy usage                         | `false`     |
| `delay_account_switch`   | Delay between account switches (seconds)           | `10`        |
| `delay_loop`             | Delay before the next loop iteration (milliseconds) | `3000`      |

---

## 📥 **How to Register**

Start using Blum Bot by registering through the following link:

<div align="center">
  <a href="https://t.me/blum/app?startapp=ref_uTyHfMEx6P" target="_blank">
    <img src="https://img.shields.io/static/v1?message=Blum&logo=telegram&label=&color=2CA5E0&logoColor=white&labelColor=&style=for-the-badge" height="25" alt="telegram logo" />
  </a>
</div>

---

## 📖 **Installation Steps**

1. **Clone the Repository**  
   Copy the project to your local machine:

   ```bash
   git clone https://github.com/livexords-nw/blum-bot.git
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

## 🛠️ **Contributing**

This project is developed by **Livexords**. If you have suggestions, questions, or would like to contribute, feel free to contact us:

<div align="center">
  <a href="https://t.me/livexordsscript" target="_blank">
    <img src="https://img.shields.io/static/v1?message=Livexords&logo=telegram&label=&color=2CA5E0&logoColor=white&labelColor=&style=for-the-badge" height="25" alt="telegram logo" />
  </a>
</div>

---