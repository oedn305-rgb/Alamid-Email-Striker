import smtplib
import time
import os
import sys
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# --- إعدادات الحساب ---
SENDER_EMAIL = "اكتب_إيميلك_هنا@gmail.com"  # 👈 حط إيميلك هنا
GMAIL_APP_PASSWORD = os.getenv("GMAIL_PASS")

def log(msg):
    print(f">>> {msg}")
    sys.stdout.flush()

def start_mission():
    log("🚀 [Alamid System]: Starting the engine...")
    
    if not GMAIL_APP_PASSWORD:
        log("❌ Secret GMAIL_PASS is missing!")
        return

    try:
        with open("emails.txt", "r") as f:
            emails = [line.strip() for line in f.readlines() if line.strip()]
    except:
        log("❌ emails.txt not found!")
        return

    log(f"📊 Found {len(emails)} emails. Ready to fly.")

    for index, email in enumerate(emails[:100]):
        try:
            msg = MIMEMultipart()
            # استخدمنا اسم إنجليزي في الـ From عشان السيرفر ما يرفض
            msg['From'] = f"Alamid Systems <{SENDER_EMAIL}>"
            msg['To'] = email
            # عنوان بالإنجليزية لضمان الوصول السريع
            msg['Subject'] = "Important Legal Update - Alamid System"
            
            # الكلام العربي هنا "مسموح" وما يسبب مشاكل
            body = """
مرحباً بك،
منصة العميد تمنحك القوة القانونية عبر الذكاء الاصطناعي.
🔗 تجربة الـ 7 أيام مجاناً عبر تليجرام: https://t.me/Alamid_Bot
            """
            msg.attach(MIMEText(body, 'plain', 'utf-8'))

            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(SENDER_EMAIL, GMAIL_APP_PASSWORD)
            server.send_message(msg)
            server.quit()
            
            log(f"✅ [{index+1}] Sent successfully to: {email}")
            time.sleep(15) 
            
        except Exception as e:
            log(f"❌ Error with {email}: {str(e)}")

if __name__ == "__main__":
    start_mission()
