import os
import smtplib
import time
from email.message import EmailMessage

EMAIL_FILE = "emails.txt"
LIMIT = 50

def load_emails():
    if not os.path.exists(EMAIL_FILE):
        print("❌ ملف emails.txt غير موجود")
        return []

    with open(EMAIL_FILE, "r") as f:
        return [line.strip() for line in f if "@" in line]


def start_striker():

    EMAIL = os.getenv("GMAIL_USER")
    PASS = os.getenv("GMAIL_PASS")

    if not EMAIL or not PASS:
        print("❌ Secrets ناقصة")
        return

    targets = load_emails()[:LIMIT]

    print(f"📡 سيتم إرسال رسائل إلى {len(targets)} عميل")

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(EMAIL, PASS)

            for target in targets:

                msg = EmailMessage()
                msg["Subject"] = "⚖️ عرض قانوني خاص"
                msg["From"] = EMAIL
                msg["To"] = target

                msg.set_content("""
مرحباً،

نقدم لكم خدمات قانونية ذكية لعام 2026.

🎁 تجربة مجانية 7 أيام

https://t.me/اسم_بوتك
""")

                smtp.send_message(msg)

                print("✅ تم الإرسال:", target)

                time.sleep(2)

    except Exception as e:
        print("❌ خطأ:", e)


if __name__ == "__main__":
    start_striker()
