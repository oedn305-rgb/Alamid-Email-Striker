import smtplib
import os
import time
import random
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# --- الإعدادات الفنية (تُسحب آلياً من GitHub Secrets) ---
SENDER_EMAIL = "Alamid.Systems.2026@outlook.com"
APP_PASSWORD = os.getenv("MS_APP_PASS") 

def send_marketing_email(target_email):
    """وظيفة إرسال الرسالة التسويقية بجودة عالية"""
    try:
        # 1. تجهيز هيكل الرسالة
        msg = MIMEMultipart()
        msg['From'] = f"العميد - المستشار الذكي ⚖️ <{SENDER_EMAIL}>"
        msg['To'] = target_email
        msg['Subject'] = "⚠️ تنبيه نظامي: هل أعمالكم محمية من ثغرات 2026؟"

        # 2. نص الرسالة الصاروخي (الذي يجلب المشتركين)
        body = f"""
مرحباً بك،

عالم الأنظمة السعودية يتغير بسرعة، وتجاهل ثغرة واحدة في عقودك أو قضاياك قد يكلفك الكثير. نحن هنا لنمنحك القوة.

يسرنا دعوتك لتجربة "العميد" - أول محرك ذكاء اصطناعي متخصص في كشف الثغرات القانونية السعودية بناءً على تحديثات عام 2026.

🔹 تحليل فوري للقضايا (جنائي، تجاري، عقاري، عمالي).
🔹 استخراج ثغرات مبنية على أحدث مبادئ المحكمة العليا.
🔹 تجربة مجانية بالكامل لمدة 7 أيام.

🔗 ابدأ الحماية الآن عبر تليجرام:
https://t.me/Alamid_Bot  <-- (تأكد من وضع رابط بوتك الصحيح هنا)

منصة العميد - لا تترك حقك للصدفة.
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

if __name__ == "__main__":
    # التأكد من وجود كلمة السر
    if not APP_PASSWORD:
        print("❌ خطأ: لم يتم العثور على MS_APP_PASS في الـ Secrets!")
    else:
        # قراءة الأهداف من ملف الإيميلات
        if os.path.exists("emails.txt"):
            with open("emails.txt", "r") as f:
                # تنظيف القائمة ومنع التكرار
                emails = list(set([line.strip() for line in f.readlines() if "@" in line]))
            
            print(f"🚀 انطلاق الحملة! استهداف {len(emails)} عميل محتمل...")

            for index, email in enumerate(emails):
                if send_marketing_email(email):
                    print(f"✅ [{index+1}/{len(emails)}] تم الإرسال بنجاح إلى: {email}")
                
                # استراحة ذكية لتجنب حظر الإيميل (بين دقيقة ودقيقتين)
                if index < len(emails) - 1:
                    wait = random.randint(60, 120)
                    print(f"⏳ انتظار {wait} ثانية للتخفي...")
                    time.sleep(wait)
            
            print("🏁 تمت الحملة بنجاح يا عميد!")
        else:
            print("❌ خطأ: ملف emails.txt غير موجود!")
