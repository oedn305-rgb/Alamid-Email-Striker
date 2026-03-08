import smtplib
import time
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# --- إعدادات الحساب المباشرة يا العميد ---
EMAIL_ADDRESS = "alamid.ai.bot@gmail.com"  # تم وضع إيميلك هنا مباشرة
# كلمة مرور التطبيق (16 حرف) تسحب من الـ Secrets للأمان
EMAIL_PASSWORD = os.environ.get('MS_APP_PASS') 

def send_emails():
    print("-" * 40)
    print("🚀 [العميد التقني]: بدأت العملية الآن..")
    print(f"📧 الإيميل المرسل: {EMAIL_ADDRESS}")
    
    # التأكد من وجود كلمة مرور التطبيق
    if not EMAIL_PASSWORD:
        print("❌ خطأ: لم أجد 'MS_APP_PASS' في إعدادات الـ Secrets!")
        print("💡 تأكد من إضافة كلمة مرور التطبيق (16 حرف) في GitHub Settings.")
        return

    # قراءة القائمة (1432 إيميل)
    try:
        with open('emails.txt', 'r', encoding='utf-8') as f:
            emails = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print("❌ خطأ: ملف emails.txt غير موجود!")
        return

    total_count = len(emails)
    print(f"📋 تم العثور على {total_count} إيميل في ملفك.")
    
    # دفعة الـ 100 الأولى
    batch = emails[:100]
    print(f"🎯 سنبدأ بالإرسال لأول {len(batch)} جهة قانونية.")
    print("-" * 40)

    try:
        print("🔌 جاري الاتصال بسيرفر Google (Gmail)...")
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        
        # تسجيل الدخول
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        print("🔓 تم تسجيل الدخول بنجاح! جاري البدء بالحملة:")
        print("-" * 40)

        for i, target_email in enumerate(batch, 1):
            try:
                msg = MIMEMultipart()
                msg['From'] = EMAIL_ADDRESS
                msg['To'] = target_email
                msg['Subject'] = "مساعد المحامي الذكي - عرض خاص لنخبة القانون"

                body = (
                    "سعادة المستشار،\n\n"
                    "نهديكم أطيب التحيات، ونضع بين أيديكم بوت 'العميد' المطور "
                    "بالذكاء الاصطناعي لخدمة المكاتب القانونية في صياغة ومراجعة العقود.\n\n"
                    "للتجربة والاستفسار، يسعدنا تواصلكم عبر الرد على هذا الإيميل."
                )
                msg.attach(MIMEText(body, 'plain', 'utf-8'))

                server.send_message(msg)
                print(f"✅ [{i}/{len(batch)}] تم الإرسال إلى: {target_email}")
                
                # استراحة أمان (60 ثانية)
                if i < len(batch):
                    print(f"💤 استراحة دقيقة (جوجل يراقبنا).. البوت شغال")
                    time.sleep(60) 

            except Exception as e:
                print(f"⚠️ مشكلة في إرسال {target_email}: {e}")

        server.quit()
        print("-" * 40)
        print("🎉 كفو يا العميد! المهمة تمت بنجاح وبدون مشاكل.")

    except Exception as e:
        print(f"❌ فشل تسجيل الدخول: {e}")
        print("💡 نصيحة: تأكد أن MS_APP_PASS في الـ Secrets هي (16 حرف) صحيحة.")

if __name__ == "__main__":
    send_emails()
