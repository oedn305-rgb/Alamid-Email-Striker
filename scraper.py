import smtplib
import time
import random
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# --- إعدادات سيرفر Mailjet ---
SMTP_SERVER = "in-v3.mailjet.com"
SMTP_PORT = 587

# سحب المفاتيح من GitHub Secrets (اللي أضفتها أنت قبل قليل)
API_KEY = os.getenv("MAILJET_API_KEY") 
SECRET_KEY = os.getenv("MAILJET_SECRET_KEY")

# إيميلك المعتمد في Mailjet
SENDER_EMAIL = "Alamid.Systems.2026@outlook.com"

def send_lawyer_email(target_email):
    """وظيفة إرسال الإيميل القانوني"""
    try:
        msg = MIMEMultipart()
        # الاسم اللي بيظهر للمستلم
        msg['From'] = f"منصة العميد - ذكاء قانوني ⚖️ <{SENDER_EMAIL}>"
        msg['To'] = target_email
        msg['Subject'] = "⚠️ تنبيه نظامي: هل أعمالكم محمية من ثغرات 2026؟"

        # نص الرسالة
        body = f"""
مرحباً بك،

عالم الأنظمة السعودية يتغير بسرعة، ومنصة "العميد" تمنحك القوة القانونية عبر الذكاء الاصطناعي.
حلل قضاياك، استخرج ثغراتك، واحمل حقك بقوة نظام 2026.

💡 ماذا تقدم لك منصة العميد؟
✅ تحليل المذكرات القانونية واستخراج الثغرات.
✅ صياغة ردود قانونية محكمة بناءً على الأنظمة السعودية.
✅ دعم فني قانوني ذكي على مدار الساعة.

🔗 ابدأ تجربة الـ 7 أيام مجاناً عبر تليجرام:
https://t.me/Alamid_Bot

منصة العميد - شريكك القانوني الذكي.
        """
        msg.attach(MIMEText(body, 'plain', 'utf-8'))

        # تنفيذ عملية الإرسال
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        # تسجيل الدخول بمفاتيح Mailjet
        server.login(API_KEY, SECRET_KEY) 
        server.send_message(msg)
        server.quit()
        return True
    except Exception as e:
        print(f"❌ خطأ في الإرسال لـ {target_email}: {e}")
        return False

def run_campaign():
    """تشغيل الحملة على قائمة الإيميلات"""
    if not API_KEY or not SECRET_KEY:
        print("❌ خطأ: مفاتيح Mailjet غير موجودة في الـ Secrets!")
        return

    # التأكد من وجود ملف الإيميلات
    if not os.path.exists("emails.txt"):
        print("❌ خطأ: ملف emails.txt مفقود!")
        return

    with open("emails.txt", "r") as f:
        emails = [line.strip() for line in f.readlines() if line.strip()]

    if not emails:
        print("⚠️ القائمة فارغة!")
        return

    # إرسال لأول 100 إيميل
    target_list = emails[:100]
    print(f"🚀 [منصة العميد]: انطلاق الحملة.. المستهدف {len(target_list)} جهة.")

    for index, email in enumerate(target_list):
        if send_lawyer_email(email):
            print(f"✅ [{index+1}/100] تم الإرسال بنجاح: {email}")
        
        # استراحة أمان (دقيقة تقريباً) عشان ما يحظرك السيرفر
        if index < len(target_list) - 1:
            wait_time = random.randint(60, 90)
            print(f"⏳ انتظار {wait_time} ثانية للأمان...")
            time.sleep(wait_time)

    print("🏁 انتهت المهمة بنجاح يا سعادة المحامي!")

if __name__ == "__main__":
    run_campaign()
