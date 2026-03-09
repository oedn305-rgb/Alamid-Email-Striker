import os
import smtplib
import time
from email.message import EmailMessage

EMAIL_FILE = "emails.txt"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465
SEND_LIMIT = 50  # عدد الإيميلات التي سيتم إرسالها في كل تشغيل


def load_emails():
    """تحميل وتنظيف الإيميلات"""
    if not os.path.exists(EMAIL_FILE):
        print("❌ ملف emails.txt غير موجود!")
        return []

    with open(EMAIL_FILE, "r") as f:
        emails = set(line.strip().lower() for line in f if "@" in line)

    return list(emails)


def start_striker():

    MY_EMAIL = os.getenv("GMAIL_USER")
    GMAIL_PASS = os.getenv("GMAIL_PASS")

    if not MY_EMAIL or not GMAIL_PASS:
        print("❌ نقص في GitHub Secrets (GMAIL_USER / GMAIL_PASS)")
        return

    emails = load_emails()

    if not emails:
        print("⚠️ لا يوجد أهداف للإرسال.")
        return

    targets = emails[:SEND_LIMIT]

    print(f"📡 بدء الحملة... سيتم استهداف {len(targets)} عميل.")

    try:
        with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as smtp:
            smtp.login(MY_EMAIL, GMAIL_PASS)

            for target in targets:

                msg = EmailMessage()
                msg["Subject"] = "⚖️ عرض قانوني خاص من منصة العميد"
                msg["From"] = MY_EMAIL
                msg["To"] = target

                msg.set_content(
                    f"""
مرحباً،

منصة العميد تقدم خدمات قانونية ذكية لعام 2026.

🎁 عرض خاص: تجربة مجانية لمدة 7 أيام.

للتواصل مباشرة عبر البوت:
https://t.me/اسم_بوتك
"""
                )

                try:
                    smtp.send_message(msg)
                    print(f"✅ تم الإرسال إلى: {target}")
                    time.sleep(2)

                except Exception as e:
                    print(f"❌ فشل الإرسال إلى {target}: {e}")

    except Exception as e:
        print(f"❌ فشل الاتصال بخادم البريد: {e}")


if __name__ == "__main__":
    start_striker()
