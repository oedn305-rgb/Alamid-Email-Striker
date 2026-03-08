import smtplib
import os
import sys
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# إعدادات ثابتة وقوية
SMTP_SERVER = "in-v3.mailjet.com"
SMTP_PORT = 587
SENDER_EMAIL = "Alamid.Systems.2026@outlook.com"

# جلب المفاتيح
API_KEY = os.getenv("MAILJET_API_KEY")
SECRET_KEY = os.getenv("MAILJET_SECRET_KEY")

def log(message):
    """وظيفة لطباعة النتائج فوراً بدون تأخير"""
    print(f">>> {message}")
    sys.stdout.flush()

def start_mission():
    log("🚀 انطلاق منصة العميد... جاري فحص المحركات")
    
    if not API_KEY or not SECRET_KEY:
        log("❌ خطأ قاتل: المفاتيح غير موجودة في الـ Secrets!")
        return

    if not os.path.exists("emails.txt"):
        log("❌ خطأ: ملف emails.txt مفقود!")
        return

    with open("emails.txt", "r") as f:
        emails = [line.strip() for line in f.readlines() if line.strip()]

    if not emails:
        log("⚠️ القائمة فارغة!")
        return

    log(f"✅ تم العثور على {len(emails)} إيميل. سأبدأ الإرسال فوراً...")

    # إرسال تجريبي لأول 5 إيميلات بسرعة البرق للتأكد من العمل
    for index, email in enumerate(emails[:100]):
        try:
            msg = MIMEMultipart()
            msg['From'] = f"منصة العميد ⚖️ <{SENDER_EMAIL}>"
            msg['To'] = email
            msg['Subject'] = "تنبيه نظامي: منصة العميد للذكاء القانوني"
            
            body = "مرحباً بك في منصة العميد. نحن نغير قواعد اللعبة القانونية في 2026."
            msg.attach(MIMEText(body, 'plain'))

            server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
            server.starttls()
            server.login(API_KEY, SECRET_KEY)
            server.send_message(msg)
            server.quit()
            
            log(f"✅ [{index+1}] تم الإرسال بنجاح إلى: {email}")
            
        except Exception as e:
            log(f"❌ فشل مع {email}. الخطأ: {str(e)}")

if __name__ == "__main__":
    start_mission()
