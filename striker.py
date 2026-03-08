import smtplib
import time
import os
import sys
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.utils import formataddr

# --- إعدادات الحساب ---
SENDER_EMAIL = "اكتب_إيميلك_هنا@gmail.com"  # 👈 تأكد من وضع إيميلك هنا
GMAIL_APP_PASSWORD = os.getenv("GMAIL_PASS")

# إعدادات سيرفر جوجل
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

def log(msg):
    print(f">>> {msg}")
    sys.stdout.flush()

def start_mission():
    log("🚀 [منصة العميد]: محرك Gmail بدأ العمل الآن...")
    
    if not GMAIL_APP_PASSWORD:
        log("❌ خطأ: لم يجد النظام مفتاح GMAIL_PASS في الـ Secrets!")
        return

    if not os.path.exists("emails.txt"):
        log("❌ خطأ: ملف emails.txt مفقود!")
        return

    with open("emails.txt", "r") as f:
        emails = [line.strip() for line in f.readlines() if line.strip()]

    log(f"📊 فحص القائمة: وجدنا {len(emails)} إيميل جاهز.")

    for index, email in enumerate(emails[:100]):
        try:
            msg = MIMEMultipart()
            
            # --- حل مشكلة العربي في اسم المرسل ---
            sender_name = str(Header('منصة العميد ⚖️', 'utf-8'))
            msg['From'] = formataddr((sender_name, SENDER_EMAIL))
            msg['To'] = email
            
            # --- حل مشكلة العربي في العنوان ---
            msg['Subject'] = Header('تنبيه نظامي: منصة العميد للذكاء القانوني', 'utf-8').encode()
            
            body = "مرحباً، منصة العميد تمنحك القوة القانونية عبر الذكاء الاصطناعي.\nتجربة مجانية: https://t.me/Alamid_Bot"
            msg.attach(MIMEText(body, 'plain', 'utf-8'))

            server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
            server.starttls()
            server.login(SENDER_EMAIL, GMAIL_APP_PASSWORD)
            server.send_message(msg)
            server.quit()
            
            log(f"✅ [{index+1}] تم الإرسال بنجاح إلى: {email}")
            time.sleep(15) 
            
        except Exception as e:
            log(f"❌ فشل الإرسال لـ {email}: {str(e)}")

if __name__ == "__main__":
    start_mission()
