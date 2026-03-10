import os
import smtplib
import time
from email.message import EmailMessage

EMAIL_FILE = "emails.txt"
PROGRESS_FILE = "sent_progress.txt"

DAILY_LIMIT = 30           # عدد الإيميلات التي ترسل كل يوم
DELAY_BETWEEN_EMAILS = 10  # ثواني بين كل رسالة لتجنب الحظر

def load_progress():
    if os.path.exists(PROGRESS_FILE):
        with open(PROGRESS_FILE, "r") as f:
            return int(f.read().strip())
    return 0

def save_progress(index):
    with open(PROGRESS_FILE, "w") as f:
        f.write(str(index))

def start_striker():
    EMAIL = os.getenv("BOT_EMAIL")          # البريد من Secrets
    PASSWORD = os.getenv("BOT_EMAIL_PASS")  # App Password

    if not EMAIL or not PASSWORD:
        print("❌ Secrets ناقصة")
        return

    if not os.path.exists(EMAIL_FILE):
        print("❌ ملف emails.txt غير موجود")
        return

    with open(EMAIL_FILE, "r") as f:
        targets = [line.strip() for line in f if "@" in line]

    start_index = load_progress()
    end_index = min(start_index + DAILY_LIMIT, len(targets))
    todays_targets = targets[start_index:end_index]

    print(f"📡 سيتم إرسال {len(todays_targets)} إيميل اليوم")

    if not todays_targets:
        print("✅ لا توجد إيميلات جديدة للإرسال اليوم")
        return

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(EMAIL, PASSWORD)

            for target in todays_targets:
                msg = EmailMessage()
                msg["Subject"] = "عرض خاص"
                msg["From"] = EMAIL
                msg["To"] = target

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

        # حفظ التقدم حتى يبدأ من هنا في اليوم التالي
        save_progress(end_index)
        print("✅ تم تحديث التقدم للإيميلات القادمة")

    except Exception as e:
        print("❌ خطأ:", e)

if __name__ == "__main__":
    start_striker()
