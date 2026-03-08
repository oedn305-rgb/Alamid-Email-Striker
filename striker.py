import os
import smtplib
import time
from email.message import EmailMessage

def start_striker():
    print("🚀 [المهاجم]: بدء الإرسال الفعلي لعملاء النخبة...")

    # --- بياناتك اللي طلبتها ---
    MY_EMAIL = "oedn305@gmail.com"  
    GMAIL_PASS = os.getenv("GMAIL_PASS") # بيسحب الكود السري من Secrets

    if not GMAIL_PASS:
        print("❌ خطأ: لم يتم العثور على GMAIL_PASS في الـ Secrets!")
        return

    if not os.path.exists("emails.txt"):
        print("❌ لم أجد ملف emails.txt")
        return

    with open("emails.txt", "r") as f:
        emails = [line.strip() for line in f.readlines() if "@" in line]

    print(f"📂 تم العثور على {len(emails)} هدف. جاري استهداف أول 50...")

    # الإرسال الفعلي
    count = 0
    for target in emails[:50]:
        msg = EmailMessage()
        msg.set_content(f"مرحباً بك في منصة العميد.\nنحن هنا لخدمتكم قانونياً وتقديم الاستشارات النوعية لعام 2026.\n\nللتواصل المباشر عبر تليجرام: t.me/ALAMID_STRIKE_BOT")
        msg['Subject'] = "⚖️ عرض قانوني خاص من منصة العميد"
        msg['From'] = MY_EMAIL
        msg['To'] = target

        try:
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(MY_EMAIL, GMAIL_PASS)
                smtp.send_message(msg)
            print(f"✅ تم الإرسال بنجاح إلى: {target}")
            count += 1
            time.sleep(1) # تأخير بسيط للأمان
        except Exception as e:
            print(f"❌ فشل الإرسال إلى {target}: {e}")

    print(f"🏁 المهمة انتهت! تم استقطاب {count} عملاء بنجاح.")

if __name__ == "__main__":
    start_striker()
