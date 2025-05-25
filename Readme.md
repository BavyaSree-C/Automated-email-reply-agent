# 📬 Email Reply Agent with Telegram Notifications

## 💡 Overview

The **Email Reply Agent** is a smart automation tool that:

* Fetches unread emails from Gmail.
* Classifies each email’s intent using zero-shot learning.
* Generates a professional AI-based reply.
* Sends the draft to a Telegram chat for review and approval.

Built using Python, Hugging Face Transformers, Gmail API, and Telegram Bot API, this tool streamlines your email management with NLP and automation.

---

## 🚀 Features

* ✅ **Gmail API Integration** – Secure OAuth2 email access.
* 🧠 **Intent Classification** – Zero-shot classification using `facebook/bart-large-mnli`.
* ✍️ **Smart Replies** – AI-generated replies tailored by category using `google/flan-t5-large`.
* 🤖 **Telegram Bot Notification** – Replies are sent to your Telegram for manual review.
* 🔐 **Secure Environment Management** – `.env` file usage for tokens and secrets.
* 🪵 **Central Logging** – Log all system events and errors to a `.log` file.
* 📚 **Reply Log** – Maintains a JSON history of replies.
* 🗂️ **MIME-Safe Email Parsing** – Extracts plain text from complex email formats.

---

## 🗂 Project Structure

```
email_reply_agent/
├── README.md
├── requirements.txt
├── .env
├── venv/
└── src/
    ├── main.py                # Entry point
    ├── fetch_email.py         # Fetch emails from Gmail
    ├── classify_and_reply.py  # Classify and generate replies
    ├── notify_telegram.py     # Send replies to Telegram
    ├── send_email.py          # [Optional] For sending emails automatically
    ├── logger.py              # Logging setup
    ├── config.py              # Environment variable loader
    ├── credentials.json       # Gmail API credentials
```

---

## 🔧 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/BavyaSree-C/email_reply_agent.git
cd email_reply_agent
```

### 2. Set Up Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Gmail API

* Go to [Google Cloud Console](https://console.cloud.google.com/).
* Enable **Gmail API** and create **OAuth2 credentials**.
* Download `credentials.json` and place it in the `src/` folder.

### 5. Configure Telegram Bot

* Talk to [@BotFather](https://t.me/BotFather) to create a new bot and get the token.
* Use [@userinfobot](https://t.me/userinfobot) to find your `chat_id`.

Create a `.env` file in root:

```
TELEGRAM_TOKEN=your_telegram_bot_token
CHAT_ID=your_chat_id
```

---

## ▶️ Run the Bot

```bash
python src/main.py
```

---

## 📄 Module Overview

| Module                  | Description                                               |
| ----------------------- | --------------------------------------------------------- |
| `fetch_email.py`        | Connects to Gmail, fetches unread emails, parses content. |
| `classify_and_reply.py` | Classifies emails and generates context-aware replies.    |
| `notify_telegram.py`    | Sends replies to Telegram with formatting and fallback.   |
| `send_email.py`         | (Optional) Sends replies via SMTP (currently disabled).   |
| `logger.py`             | Handles logging of all system activities.                 |
| `main.py`               | Integrates all components and runs the bot.               |

---

## 📦 Requirements

See [`requirements.txt`](./requirements.txt). Major packages include:

* `google-api-python-client`
* `oauth2client`
* `transformers`
* `torch`
* `nltk`
* `scikit-learn`
* `requests`
* `python-dotenv`

---

## 🛡 License

MIT License – Feel free to use, modify, and distribute.

---

## 🙋‍♂️ Author

Developed by \[Your Name].
If this helps you, give it a ⭐ on GitHub!

---

