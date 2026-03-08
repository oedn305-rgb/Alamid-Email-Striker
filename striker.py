import os
import smtplib
import time
from email.message import EmailMessage

def start_striker():
    print("🚀 [المهاجم]: بدء الإرسال الفعلي لعملاء النخبة...")

    # سحب البيانات من السيكرتس اللي عندك بالأسماء اللي ظهرت في الصورة
    # تأكد أن الإيميل اللي ترسل منه هو جيميل
    MY_EMAIL = "ضع_ايميلك_هنا@gmail.com"  # اكتب ايميلك هنا مباشرة
    GMAIL_PASS = os.getenv("GMAIL_PASS")  # يسحب الـ 16 حرف من السيكرت اللي عندك

    if not GMAIL_PASS:
        print("❌ خطأ: لم يتم العثور على GMAIL_PASS في الـ Secrets!")
        return

    if not os.path.exists("emails.txt"):
        print("❌ لم أجد ملف emails.txt")
        return

    with open("emails.txt", "r") as f:
        emails = [line.strip() for line in f.readlines() if "@" in line]

    print(f"📂 تم العثور على {len(emails)} إيميل. جاري استهداف أول 50...")

    for target in emails[:50]:
        msg = EmailMessage()
        # نص الرسالة (تقدر تغيره)
        msg.set_content(f"مرحباً بك في منصة العميد.\nنحن هنا لخدمتكم قانونياً لعام 2026.\n\nللتواصل السريع عبر تليجرام: t.me/اسم_بوتك")
        msg['Subject'] = "⚖️ استشارة قانونية من منصة العميد"
        msg['From'] = MY_EMAIL
        msg['To'] = target

        try:
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(MY_EMAIL, GMAIL_PASS)
                smtp.send_message(msg)
            print(f"✅ تم الإرسال بنجاح إلى: {target}")
            time.sleep(1) # عشان قوقل ما يزعل علينا
        except Exception as e:
            print(f"❌ فشل الإرسال إلى {target}: {e}")

if __name__ == "__main__":
    start_striker()
