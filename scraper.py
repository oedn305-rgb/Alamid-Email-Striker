import smtplib
import time
import os
import re
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# دالة لتنظيف النصوص من أي أحرف عربية مخفية أو مسافات
def clean_text(text):
    if text:
        # حذف أي حرف غير قابل للطباعة أو أحرف التنسيق العربي المخفية
        return re.sub(r'[^\x00-\x7f]', '', text).strip()
    return None

# إعدادات الحساب (تنظيف آلي)
EMAIL_ADDRESS = clean_text("alamid.ai.bot@gmail.com")
EMAIL_PASSWORD = clean_text(os.environ.get('MS_APP_PASS'))

def send_emails():
    print("-" * 40)
    print("🚀 [العميد التقني]: بدأت عملية التنظيف والإرسال..")
    
    if not EMAIL_PASSWORD:
        print("❌ خطأ: لم يتم العثور على كلمة مرور التطبيق في Secrets!")
        return

    # قراءة وتنظيف قائمة الإيميلات
    try:
        with open('emails.txt', 'r', encoding='utf-8') as f:
            emails = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print("❌ خطأ: ملف emails.txt غير موجود!")
        return

    print(f"📧 المرسل: {EMAIL_ADDRESS}")
    print(f"📋 القائمة تحتوي على {len(emails)} إيميل.")
    
    batch = emails[:100]
    print(f"🎯 الهدف: أول {len(batch)} جهة قانونية.")
    print("-" * 40)

    try:
        print("🔌 جاري الاتصال بسيرفر Google...")
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.set_debuglevel(0)
        server.starttls()
        
        # تسجيل الدخول بعد التنظيف
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        print("🔓 تم تسجيل الدخول بنجاح! الحملة بدأت:")
        print("-" * 40)

        for i, target_email in enumerate(batch, 1):
            target_email = clean_text(target_email) # تنظيف إيميل المستلم أيضاً
            try:
                msg = MIMEMultipart()
                msg['From'] = EMAIL_ADDRESS
                msg['To'] = target_email
                msg['Subject'] = "مساعد المحامي الذكي - عرض خاص"

                body = (
                    "سعادة المستشار،\n\n"
                    "نهديكم أطيب التحيات، ونضع بين أيديكم بوت 'العميد' المطور "
                    "بالذكاء الاصطناعي لخدمة المكاتب القانونية.\n\n"
                    "يسعدنا تواصلكم."
                )
                msg.attach(MIMEText(body, 'plain', 'utf-8'))

                server.send_message(msg)
                print(f"✅ [{i}/{len(batch)}] أرسل إلى: {target_email}")
                
                if i < len(batch):
                    time.sleep(60) # استراحة دقيقة

            except Exception as e:
                print(f"⚠️ خطأ في {target_email}: {e}")

        server.quit()
        print("-" * 40)
        print("🎉 انتهت المهمة بنجاح يا عميد!")

    except Exception as e:
        print(f"❌ فشل تسجيل الدخول: {e}")
        print("💡 جرب إعادة كتابة كلمة السر في الـ Secrets يدوياً (بدون نسخ ولصق) إذا استمر الخطأ.")

if __name__ == "__main__":
    send_emails()
