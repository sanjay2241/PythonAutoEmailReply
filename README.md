# 📧 Auto Email Reply Bot

A simple Python script that automatically checks your Gmail inbox every 30 seconds and sends an auto-reply to any new (unread) email with a specified subject line.

---

## ✨ Features

- Connects securely to your Gmail account using IMAP and SMTP.
- Searches for unread emails with a specific subject (e.g., "Job Application").
- Sends a predefined auto-reply to each matching email.
- Runs continuously and checks for new emails every 30 seconds.

---

## 🛠 Requirements

- Python 3.6+
- A Gmail account with:
  - IMAP access enabled
  - App Password (if 2FA is enabled)

### Python Packages

No external packages required beyond the Python standard library:
- `imaplib`
- `smtplib`
- `email`
- `time`

---


