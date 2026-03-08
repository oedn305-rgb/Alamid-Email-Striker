import smtplib
import time
import random
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# --- الإعدادات الفنية ---
# تأكد من وضع الـ 16 حرف في GitHub Secrets باسم: MS_APP_PASS
SENDER_EMAIL = "Alamid.Systems.2026@outlook.com" 
APP_PASSWORD = os.getenv("MS_APP_PASS") 

def send_marketing_email(target_email):
    """وظيفة إرسال الرسالة التسويقية بنظام العميد عبر Microsoft Outlook"""
    try:
        # 1. تجهيز هيكل الرسالة
        msg = MIMEMultipart()
        msg['From'] = f"منصة العميد - ذكاء قانوني ⚖️ <{SENDER_EMAIL}>"
        msg['To'] = target_email
        msg['Subject'] = "⚠️ تنبيه نظامي: هل أعمالكم محمية من ثغرات 2026؟"

        # 2. محتوى الرسالة الاحترافي (صياغة العميد)
        body = f"""
أهلاً بك،

عالم الأنظمة السعودية في 2026 يتطور بسرعة، والتحديات القانونية تتطلب أدوات ذكية لمواكبتها.

يسرنا في "منصة العميد" دعوتك لتجربة أول محرك ذكاء اصطناعي متخصص في كشف الثغرات القانونية السعودية وتفنيد المذكرات بناءً على أحدث مبادئ المحكمة العليا.

💡 ما الذي يميز "العميد"؟
✅ تحليل فوري للمذكرات (جنائي، تجاري، عمالي، عقاري).
✅ استنباط الثغرات النظامية بدقة متناهية.
✅ صياغة ردود قانونية محكمة توفر عليك الساعات.

🎁 عرض خاص:
استمتع بتجربة مجانية بالكامل لمدة 7 أيام واكتشف الفرق بنفسك.

🔗 انضم الآن عبر تليجرام وابدأ الحماية:
[ضع رابط بوت التليجرام هنا]

منصة العميد - القوة القانونية بين يديك.
        """
        
        msg.attach(MIMEText(body, 'plain', 'utf-8'))

        # 3. الاتصال بسيرفر Microsoft
        server = smtplib.SMTP("smtp.office365.com", 587)
        server.starttls() # تشفير الاتصال
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
        print("❌ خطأ: لم يتم العثور على الرمز (MS_APP_PASS) في GitHub Secrets!")
        return

    # التأكد من وجود ملف الإيميلات
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
        print("⚠️ تنبيه: قائمة الإيميلات فارغة!")
        return

    print(f"🚀 انطلاق حملة 'العميد'! استهداف {len(emails)} عميل محتمل...")

    for index, email in enumerate(emails):
        success = send_marketing_email(email)
        if success:
            print(f"✅ [{index+1}/{len(emails)}] تم الإرسال بنجاح إلى: {email}")
        
        # استراحة ذكية (بين 60 إلى 120 ثانية) لتجنب حظر مايكروسوفت
        if index < len(emails) - 1:
            wait_time = random.randint(60, 120)
            print(f"⏳ استراحة أمان لمدة {wait_time} ثانية...")
            time.sleep(wait_time)

    print("🏁 اكتملت حملة العميد بنجاح.")

if __name__ == "__main__":
    run_campaign()
