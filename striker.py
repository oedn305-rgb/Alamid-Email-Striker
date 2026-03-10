import os
import smtplib
import time
from email.message import EmailMessage

EMAIL_FILE = "emails.txt"

# إعدادات السلامة لتجنب الحظر
BATCH_SIZE = 50              # عدد الإيميلات في كل دفعة
DELAY_BETWEEN_EMAILS = 3     # ثواني بين كل رسالة
DELAY_BETWEEN_BATCHES = 300  # ثواني بين كل دفعة (5 دقائق)

def start_striker():

    # قراءة البريد وكلمة السر من GitHub Secrets أو متغيرات البيئة
    EMAIL = os.getenv("BOT_EMAIL")           # بريد Gmail للبوت
    PASSWORD = os.getenv("BOT_EMAIL_PASS")   # App Password 16 حرف

    if not EMAIL or not PASSWORD:
        print("❌ Secrets ناقصة")
        return

    if not os.path.exists(EMAIL_FILE):
        print("❌ ملف emails.txt غير موجود")
        return

    # قراءة الإيميلات المستهدفة
    with open(EMAIL_FILE, "r") as f:
        targets = [line.strip() for line in f if "@" in line]

    print(f"📡 سيتم الإرسال إلى {len(targets)} إيميل")

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:

            smtp.login(EMAIL, PASSWORD)

            # تقسيم الإيميلات إلى دفعات
            for i in range(0, len(targets), BATCH_SIZE):
                batch = targets[i:i+BATCH_SIZE]

                for target in batch:
                    msg = EmailMessage()
                    msg["Subject"] = "عرض خاص"
                    msg["From"] = EMAIL
                    msg["To"] = target

                    # نص الإيميل مع رابط البوت
                    msg.set_content(f"""
مرحباً،

لدينا عرض جديد لخدماتنا.

يمكنك التفاعل معنا عبر بوتنا الرسمي على تيليجرام:
https://t.me/SaudiLegal_AI_bot

تواصل معنا لمعرفة التفاصيل.
""")
                    smtp.send_message(msg)
                    print("✅ تم الإرسال إلى:", target)
                    time.sleep(DELAY_BETWEEN_EMAILS)

                print(f"🕒 الانتظار {DELAY_BETWEEN_BATCHES} ثانية قبل الدفعة التالية")
                time.sleep(DELAY_BETWEEN_BATCHES)

    except Exception as e:
        print("❌ خطأ:", e)


if __name__ == "__main__":
    start_striker()
