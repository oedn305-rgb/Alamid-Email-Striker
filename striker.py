import smtplib
import time
import random
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# إعدادات Mailjet
SMTP_SERVER = "in-v3.mailjet.com"
SMTP_PORT = 587

# سحب المفاتيح
API_KEY = os.getenv("MAILJET_API_KEY") 
SECRET_KEY = os.getenv("MAILJET_SECRET_KEY")
SENDER_EMAIL = "Alamid.Systems.2026@outlook.com"

print("🔍 [فحص النظام]: جاري التحقق من الإعدادات...")

def send_lawyer_email(target_email):
    try:
        msg = MIMEMultipart()
        msg['From'] = f"منصة العميد - ذكاء قانوني ⚖️ <{SENDER_EMAIL}>"
        msg['To'] = target_email
        msg['Subject'] = "⚠️ تنبيه نظامي: هل أعمالكم محمية من ثغرات 2026؟"

        body = """
مرحباً بك، منصة العميد تمنحك القوة القانونية عبر الذكاء الاصطناعي.
🔗 ابدأ تجربة الـ 7 أيام مجاناً عبر تليجرام:
https://t.me/Alamid_Bot
        """
        msg.attach(MIMEText(body, 'plain', 'utf-8'))

        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(API_KEY, SECRET_KEY) 
        server.send_message(msg)
        server.quit()
        return True
    except Exception as e:
        print(f"❌ خطأ فني أثناء الإرسال لـ {target_email}: {e}")
        return False

def run_campaign():
    # 1. فحص المفاتيح
    if not API_KEY or not SECRET_KEY:
        print("❌ كارثة: مفاتيح Mailjet غير موجودة في الـ Secrets! تأكد من الأسماء.")
        return
    else:
        print("✅ تم العثور على مفاتيح API بنجاح.")

    # 2. فحص ملف الإيميلات
    if not os.path.exists("emails.txt"):
        print("❌ خطأ: ملف emails.txt غير موجود في المجلد الرئيسي!")
        return
    
    with open("emails.txt", "r") as f:
        emails = [line.strip() for line in f.readlines() if line.strip()]

    print(f"📊 فحص القائمة: وجدنا {len(emails)} إيميل جاهز.")

    if not emails:
        print("⚠️ تنبيه: ملف emails.txt فارغ، لا يوجد من نرسل له!")
        return

    # 3. بدء الإرسال
    target_list = emails[:100]
    print(f"🚀 [منصة العميد]: سأبدأ الآن بإرسال أول {len(target_list)} إيميل...")

    for index, email in enumerate(target_list):
        print(f"📨 جاري المحاولة الآن مع: {email} ...")
        if send_lawyer_email(email):
            print(f"✅ [{index+1}/{len(target_list)}] تم الإرسال بنجاح!")
        
        if index < len(target_list) - 1:
            wait_time = random.randint(30, 60) # قللت الوقت شوي عشان تشوف النتائج أسرع
            print(f"⏳ سأرتاح لمدة {wait_time} ثانية لتجنب الحظر...")
            time.sleep(wait_time)

    print("🏁 اكتملت المهمة! جميع الإيميلات أُرسلت بنجاح.")

if __name__ == "__main__":
    try:
        run_campaign()
    except Exception as global_e:
        print(f"💥 حدث خطأ غير متوقع في الكود: {global_e}")
