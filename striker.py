import os
import smtplib
import time
from email.message import EmailMessage

EMAIL_FILE = "emails.txt"
PROGRESS_FILE = "sent_progress.txt"

DAILY_LIMIT = 30
DELAY_BETWEEN_EMAILS = 15


def load_progress():
    if os.path.exists(PROGRESS_FILE):
        try:
            with open(PROGRESS_FILE, "r") as f:
                return int(f.read().strip())
        except:
            return 0
    return 0


def save_progress(index):
    with open(PROGRESS_FILE, "w") as f:
        f.write(str(index))


def start_striker():

    EMAIL = os.getenv("BOT_EMAIL")
    PASSWORD = os.getenv("BOT_EMAIL_PASS")

    if not EMAIL or not PASSWORD:
        print("❌ BOT_EMAIL أو BOT_EMAIL_PASS غير موجود في Secrets")
        return

    if not os.path.exists(EMAIL_FILE):
        print("❌ ملف emails.txt غير موجود")
        return

    with open(EMAIL_FILE, "r") as f:
        targets = [line.strip() for line in f.readlines() if "@" in line]

    if not targets:
        print("❌ لا يوجد إيميلات داخل الملف")
        return

    start_index = load_progress()
    end_index = min(start_index + DAILY_LIMIT, len(targets))

    todays_targets = targets[start_index:end_index]

    print(f"📡 سيتم إرسال {len(todays_targets)} إيميل اليوم")

    if len(todays_targets) == 0:
        print("✅ جميع الإيميلات تم إرسالها")
        return

    try:

        smtp = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        smtp.login(EMAIL, PASSWORD)

        for target in todays_targets:

            msg = EmailMessage()
            msg["Subject"] = "عرض خاص"
            msg["From"] = EMAIL
            msg["To"] = target

            msg.set_content("""
مرحباً،

لدينا عرض جديد لخدماتنا.

يمكنك التفاعل معنا عبر بوتنا الرسمي على تيليجرام:
https://t.me/SaudiLegal_AI_bot

تواصل معنا لمعرفة التفاصيل.
""")

            smtp.send_message(msg)

            print("✅ تم الإرسال إلى:", target)

            time.sleep(DELAY_BETWEEN_EMAILS)

        smtp.quit()

        save_progress(end_index)

        print("✅ تم حفظ التقدم")

    except Exception as e:
        print("❌ خطأ في الإرسال:", e)


if __name__ == "__main__":
    start_striker()
