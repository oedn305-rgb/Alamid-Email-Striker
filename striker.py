import os
import smtplib
import time
from email.message import EmailMessage

EMAIL_FILE = "emails.txt"

def start_striker():

    # قراءة البريد وكلمة السر من GitHub Secrets أو متغيرات البيئة
    EMAIL = os.getenv("BOT_EMAIL")           # البريد الجديد للبوت
    PASSWORD = os.getenv("BOT_EMAIL_PASS")   # App Password

    if not EMAIL or not PASSWORD:
        print("❌ Secrets ناقصة")
        return

    if not os.path.exists(EMAIL_FILE):
        print("❌ ملف emails.txt غير موجود")
        return

    with open(EMAIL_FILE, "r") as f:
        targets = [line.strip() for line in f if "@" in line]

    print(f"📡 سيتم الإرسال إلى {len(targets)} إيميل")

    try:
        # الاتصال بسيرفر Gmail عبر SSL
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:

            smtp.login(EMAIL, PASSWORD)

            for target in targets:

                msg = EmailMessage()
                msg["Subject"] = "عرض خاص"
                msg["From"] = EMAIL
                msg["To"] = target

                msg.set_content("""
مرحباً،

لدينا عرض جديد لخدماتنا.

تواصل معنا لمعرفة التفاصيل.
""")

                smtp.send_message(msg)

                print("✅ تم الإرسال إلى:", target)

                time.sleep(2)  # تأخير بسيط لتجنب الحظر

    except Exception as e:
        print("❌ خطأ:", e)


if __name__ == "__main__":
    start_striker()
