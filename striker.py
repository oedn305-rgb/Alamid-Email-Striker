import os
import smtplib
import time
from email.message import EmailMessage

def start_striker():
    MY_EMAIL = os.getenv("GMAIL_USER")
    GMAIL_PASS = os.getenv("GMAIL_PASS")

    if not MY_EMAIL or not GMAIL_PASS:
        print("❌ نقص في بيانات السيكرتس!")
        return

    if not os.path.exists("emails.txt"):
        print("❌ ملف الأهداف غير موجود!")
        return

    with open("emails.txt", "r") as f:
        emails = [line.strip() for line in f.readlines() if "@" in line]

    print(f"📡 جاري استهداف {len(emails[:50])} عميل...")

    for target in emails[:50]:
        msg = EmailMessage()
        msg.set_content(f"منصة العميد ترحب بك.\nنحن هنا لخدمتكم قانونياً لعام 2026.\nللتواصل: t.me/اسم_بوتك")
        msg['Subject'] = "⚖️ عرض قانوني خاص من العميد"
        msg['From'] = MY_EMAIL
        msg['To'] = target

        try:
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(MY_EMAIL, GMAIL_PASS)
                smtp.send_message(msg)
            print(f"✅ تم الإرسال إلى: {target}")
            time.sleep(1)
        except Exception as e:
            print(f"❌ فشل: {e}")

if __name__ == "__main__":
    start_striker()
