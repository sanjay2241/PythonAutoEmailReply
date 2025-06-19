
import imaplib
import smtplib
import email
import time
from email.mime.text import MIMEText
from email.header import decode_header

# === CONFIGURATION ===
EMAIL_ACCOUNT = "youremail@gmail.com"
EMAIL_PASSWORD = ""  # Use App Password if 2FA is on
IMAP_SERVER = "imap.gmail.com"
SMTP_SERVER = "smtp.gmail.com"
SEARCH_SUBJECT = "Job Application"  # Change this to your desired title
REPLY_BODY = """\
Hello,

Thank you for reaching out. This is an automatic response confirming that we have received your email.

Best regards,
Sanjay Dhakal
"""

# === CONNECT TO IMAP AND FETCH EMAILS ===
def check_emails():
    mail = imaplib.IMAP4_SSL(IMAP_SERVER)
    mail.login(EMAIL_ACCOUNT, EMAIL_PASSWORD)
    mail.select("inbox")

    # Search for unread emails with specific subject
    status, messages = mail.search(None, '(UNSEEN SUBJECT "{}")'.format(SEARCH_SUBJECT))
    email_ids = messages[0].split()

    for e_id in email_ids:
        status, data = mail.fetch(e_id, '(RFC822)')
        raw_email = data[0][1]
        msg = email.message_from_bytes(raw_email)
        from_addr = email.utils.parseaddr(msg["From"])[1]
        subject = decode_header(msg["Subject"])[0][0]
        print(f"Replying to: {from_addr} | Subject: {subject}")

        send_reply(from_addr, subject)

    mail.logout()

# === SEND REPLY ===
def send_reply(to_email, original_subject):
    server = smtplib.SMTP(SMTP_SERVER, 587)
    server.starttls()
    server.login(EMAIL_ACCOUNT, EMAIL_PASSWORD)

    reply = MIMEText(REPLY_BODY)
    reply["From"] = EMAIL_ACCOUNT
    reply["To"] = to_email
    reply["Subject"] = "Re: " + original_subject

    server.sendmail(EMAIL_ACCOUNT, to_email, reply.as_string())
    server.quit()

# === RUN EVERY 30 SECONDS ===
if __name__ == "__main__":
    print("Starting auto-reply service... (checking every 30 seconds)")
    while True:
        check_emails()
        time.sleep(30)
