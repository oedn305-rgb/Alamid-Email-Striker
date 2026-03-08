import smtplib
import time
import random
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# --- الإعدادات الفنية ---
# ملاحظة: يفضل وضع كلمة السر في GitHub Secrets باسم MS_APP_PASS
SENDER_EMAIL = "Alamid.Systems.2026@outlook.com"
APP_PASSWORD = os.getenv("MS_APP_PASS") # يسحب الـ 16 حرف من الإعدادات السرية

def send_marketing_email(target_email):
    """وظيفة إرسال الرسالة التسويقية"""
    try:
        # 1. تجهيز هيكل الرسالة
        msg = MIMEMultipart()
        msg['From'] = f"العميد - المستشار الذكي ⚖️ <{SENDER_EMAIL}>"
        msg['To'] = target_email
        msg['Subject'] = "⚠️ تنبيه نظامي: هل أعمالكم محمية من ثغرات 2026؟"

        # 2. محتوى الرسالة (الرسالة التي تجذب الملايين)
        body = f"""
        مرحباً بك،
        
        عالم الأنظمة السعودية يتغير بسرعة، وتجاهل ثغرة واحدة قد يكلفك الكثير.
        نحن هنا لنمنحك القوة.
        
        يسرنا دعوتك لتجربة "العميد" - أول محرك ذكاء اصطناعي متخصص في كشف الثغرات القانونية السعودية.
        
        🔹 تحليل فوري للقضايا (جنائي، تجاري، عقاري، عمالي).
        🔹 استخراج ثغرات مبنية على أحدث مبادئ المحكمة العليا 2026.
        🔹 تجربة مجانية بالكامل لمدة 7 أيام.
        
        🔗 ابدأ الحماية الآن عبر تليجرام: [ضع رابط بوتك هنا]
        
        بعد الفترة التجريبية، يمكنك الاستمرار في الخدمة عبر باقاتنا الميسرة.
        
        منصة العميد - لا تترك حقك للصدفة.
        """
        
        msg.attach(MIMEText(body, 'plain', 'utf-8'))

        # 3. الاتصال بسيرفر مايكروسوفت وإرسال الإيميل
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
    """تشغيل الحملة التسويقية من ملف الإيميلات"""
    if not APP_PASSWORD:
        print("❌ خطأ: لم يتم العثور على MS_APP_PASS في الـ Secrets!")
        return

    # قراءة الإيميلات من الملف السري
    try:
        with open("emails.txt", "r") as file:
            emails = [line.strip() for line in file.readlines() if line.strip()]
    except FileNotFoundError:
        print("❌ خطأ: ملف emails.txt غير موجود!")
        return

    print(f"🚀 انطلاق الحملة! استهداف {len(emails)} عميل محتمل...")

    for index, email in enumerate(emails):
        success = send_marketing_email(email)
        if success:
            print(f"✅ [{index+1}/{len(emails)}] تم الإرسال إلى: {email}")
        
        # --- استراتيجية "التسلل" للنجاة من الحظر ---
        # ننتظر وقتاً عشوائياً بين 60 إلى 120 ثانية بين كل إرسال
        wait_time = random.randint(60, 120)
        if index < len(emails) - 1: # لا تنتظر بعد آخر إيميل
            print(f"⏳ استراحة ذكية لمدة {wait_time} ثانية لتجنب الرقابة...")
            time.sleep(wait_time)

    print("🏁 اكتملت الحملة بنجاح. العميد في انتظار المشتركين الجدد!")

if __name__ == "__main__":
    run_campaign()
