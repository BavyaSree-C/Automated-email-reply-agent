import json
import datetime
from fetch_email import fetch_unread_emails
from classify_and_reply import generate_reply, classify_email, filter_recent_and_valid_emails
from notify_telegram import send_to_telegram
from logger import logger

def log_reply(subject, sender, reply):
    try:
        with open("replies_log.json", "a") as f:
            json.dump({
                "timestamp": datetime.datetime.now().isoformat(),
                "sender": sender,
                "subject": subject,
                "reply": reply
            }, f)
            f.write("\n")
    except Exception as e:
        logger.warning(f"Failed to log reply: {e}")

def main():
    try:
        raw_emails = fetch_unread_emails()
        emails = []
        for subject, sender, body in raw_emails:
            emails.append({
                "subject": subject,
                "sender": sender,
                "body": body,
                "date": datetime.datetime.now().strftime("%Y-%m-%d")  # Or use actual email date if available
            })

        filtered_emails = filter_recent_and_valid_emails(emails)

        for email in filtered_emails:
            log_reply(email["subject"], email["sender"], email["reply"])
            message = (
                f"📩 From: {email['sender']}\n"
                f"Subject: {email['subject']}\n"
                f"Category: {email['category']}\n\n"
                f"Reply:\n{email['reply']}"
            )
            send_to_telegram(message)
            # Uncomment below to enable auto sending
            # send_email(email["sender"], f"Re: {email['subject']}", email["reply"])

    except Exception as e:
        logger.critical(f"Unhandled exception in main: {e}")

if __name__ == "__main__":
    main()
