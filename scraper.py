import smtplib
import time
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# إعدادات الحساب (تأكد من وضعها في Secrets بـ GitHub)
EMAIL_ADDRESS = os.environ.get('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')

def send_emails():
    print("🚀 [العميد التقني]: بدأت العملية الآن.. جاري التحضير.")
    
    try:
        with open('emails.txt', 'r') as f:
            emails = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print("❌ خطأ: ملف emails.txt غير موجود! تأكد من رفعه.")
        return

    total = len(emails)
    print(f"📋 تم العثور على {total} إيميل في القائمة.")
    
    # تحديد العدد (أول 100 لتجنب الحظر)
    batch = emails[:100]
    print(f"🎯 سيتم الإرسال إلى أول 100 إيميل في هذه الدفعة.")

    try:
        # الاتصال بالسيرفر
        print("🔌 جاري الاتصال بسيرفر Google...")
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        print("🔓 تم تسجيل الدخول بنجاح. نبدأ الإرسال:")
        print("-" * 30)

        for i, target_email in enumerate(batch, 1):
            try:
                msg = MIMEMultipart()
                msg['From'] = EMAIL_ADDRESS
                msg['To'] = target_email
                msg['Subject'] = "مساعد المحامي الذكي - عرض خاص لنخبة القانون"

                body = f"سعادة المستشار،\n\nنقدم لكم بوت 'العميد' المطور لمراجعة العقود آلياً..\nتفضل بتجربته الآن."
                msg.attach(MIMEText(body, 'plain'))

                server.send_message(msg)
                print(f"✅ [{i}/{len(batch)}] تم الإرسال إلى: {target_email}")
                
                if i < len(batch):
                    print(f"💤 استراحة أمان لمدة 60 ثانية (عشان ما ننحظر)...")
                    time.sleep(60) 
            except Exception as e:
                print(f"⚠️ فشل الإرسال إلى {target_email}: {e}")

        server.quit()
        print("-" * 30)
        print("🎉 كفو يا العميد! انتهت المهمة بنجاح 100%.")

    except Exception as e:
        print(f"❌ وقع خطأ فني كبير: {e}")
        print("💡 تأكد من أن 'كلمة مرور التطبيق' (App Password) صحيحة.")

if __name__ == "__main__":
    send_emails()
