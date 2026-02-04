# 📊 Telegram Channel Activity Analyzer

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python)
![Telethon](https://img.shields.io/badge/Telethon-v1.24-orange?style=for-the-badge&logo=telegram)
![Status](https://img.shields.io/badge/Status-Active-green?style=for-the-badge)

A powerful **Telegram Userbot** written in Python that analyzes the posting frequency of any public Telegram channel within a specific date range and generates a beautiful, dark-themed activity chart.

> **Developer:** [@tiivik](https://t.me/tiivik)

---

## ✨ Features

- 🚀 **Userbot based:** Bypasses "Bot API" restrictions to read history from any public channel.
- 📅 **Custom Date Ranges:** Analyze specific periods (e.g., last month, last year).
- 🎨 **Beautiful Visuals:** Generates high-quality, dark-mode line charts using **Seaborn** & **Matplotlib**.
- ⚡ **Asynchronous:** Built with `Telethon` for fast data fetching.
- 🔒 **Secure:** Runs locally on your machine or server.

---

## 📸 Preview

*Input Command:*
`@telegram 2024-01-01 2024-02-01`

*Output:*
> The bot replies with a generated PNG chart showing daily post counts.

---

## 🛠️ Installation

### 1. Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/Telegram-Activity-Analyzer.git
cd Telegram-Activity-Analyzer

### 2. Install Dependencies
Make sure you have Python installed, then run:
bash
pip install telethon pandas matplotlib seaborn

---

## ⚙️ Configuration

To run this script, you need your **API ID** and **API HASH** from Telegram.

1. Go to [my.telegram.org](https://my.telegram.org).
2. Login with your phone number.
3. Click on **API development tools**.
4. Create a new application (if you haven't already).
5. Copy your `api_id` and `api_hash`.

Open `main.py` (or whatever you named the script) and edit these lines:

python
API_ID = 1234567          # Your API ID
API_HASH = 'your_hash'    # Your API HASH

---

## 🚀 Usage

1. **Run the script:**
   
```bash
   python main.py
