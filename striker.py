import smtplib
import time
import random
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# --- الإعدادات الفنية ---
# تأكد من وضع الـ 16 حرف في GitHub Secrets باسم MS_APP_PASS
SENDER_EMAIL = "Lawyer.Meshal.SA@outlook.com" 
APP_PASSWORD = os.getenv("MS_APP_PASS") 

def send_marketing_email(target_email):
    """وظيفة إرسال الرسالة التسويقية بنظام العميد"""
    try:
        # 1. تجهيز هيكل الرسالة
        msg = MIMEMultipart()
        msg['From'] = f"منصة العميد - ذكاء قانوني ⚖️ <{SENDER_EMAIL}>"
        msg['To'] = target_email
        msg['Subject'] = "⚠️ تنبيه نظامي: ثغرات قانونية قد تكلفكم الكثير في 2026"

        # 2. محتوى الرسالة (صياغة قانونية تسويقية احترافية)
        body = f"""
أهلاً بك،

عالم الأنظمة السعودية في 2026 يتطور بسرعة مذهلة، والبقاء في القمة يتطلب أدوات ذكية.

يسرنا في "منصة العميد" دعوتك لتجربة أول محرك ذكاء اصطناعي متخصص في كشف الثغرات القانونية السعودية وتفنيد مذكرات الخصوم بناءً على أحدث مبادئ المحكمة العليا.

💡 ما الذي يقدمه لك "العميد"؟
✅ تحليل فوري للمذكرات (جنائي، تجاري، أحوال شخصية).
✅ استنباط الثغرات النظامية في ثوانٍ.
✅ صياغة ردود قانونية محكمة ومفصلة.

🎁 هدية خاصة لك:
نمنحك تجربة مجانية بالكامل لمدة 7 أيام لاستكشاف قوة النظام.

🔗 ابدأ الحماية الآن وانضم لنخبة المحامين عبر تليجرام:
[ضع رابط بوت التليجرام هنا]

منصة العميد - ذكاء يصنع الفرق في قضيتك.
        """
        
        msg.attach(MIMEText(body, 'plain', 'utf-8'))

        # 3. الاتصال بسيرفر مايكروسوفت
        server = smtplib.SMTP("smtp.office365.com", 587)
        server.starttls() 
        server.login(SENDER_EMAIL, APP_PASSWORD)
        server.send_message(msg)
        server.quit()
        
        return True
    except Exception as e:
        print(f"❌ خطأ في الإرسال لـ {target_email}: {e}")
        return False

def run_campaign():
    """تشغيل الحملة من ملف الإيميلات"""
    if not APP_PASSWORD:
        print("❌ خطأ: لم يتم العثور على الرمز (MS_APP_PASS) في إعدادات GitHub Secrets!")
        return

    # قراءة الإيميلات من ملف emails.txt
    try:
        if not os.path.exists("emails.txt"):
            print("❌ خطأ: ملف emails.txt غير موجود في المستودع!")
            return
            
        with open("emails.txt", "r") as file:
            emails = [line.strip() for line in file.readlines() if line.strip()]
    except Exception as e:
        print(f"❌ خطأ أثناء قراءة الملف: {e}")
        return

    if not emails:
        print("⚠️ تنبيه: ملف الإيميلات فارغ!")
        return

    print(f"🚀 انطلاق حملة 'العميد'! استهداف {len(emails)} عميل...")

    for index, email in enumerate(emails):
        success = send_marketing_email(email)
        if success:
            print(f"✅ [{index+1}/{len(emails)}] تم الإرسال بنجاح إلى: {email}")
        
        # استراحة ذكية لتجنب الحظر (بين دقيقة ودقيقتين)
        if index < len(emails) - 1:
            wait_time = random.randint(60, 120)
            print(f"⏳ استراحة لمدة {wait_time} ثانية للحفاظ على أمان الحساب...")
            time.sleep(wait_time)

    print("🏁 اكتملت حملة العميد بنجاح. في انتظار المشتركين!")

if __name__ == "__main__":
    run_campaign()
