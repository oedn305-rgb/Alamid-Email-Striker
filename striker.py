import smtplib
import time
import os
import sys
import random
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# --- إعدادات الحساب الخاصة بك ---
SENDER_EMAIL = "oedn305@gmail.com" 
GMAIL_APP_PASSWORD = os.getenv("GMAIL_PASS")

def log(msg):
    print(f">>> {msg}")
    sys.stdout.flush()

def start_mission():
    log("🚀 [Alamid System]: Starting safe delivery engine...")
    
    if not GMAIL_APP_PASSWORD:
        log("❌ Error: GMAIL_PASS is missing in GitHub Secrets!")
        return

    try:
        # قراءة الإيميلات بتنسيق يمنع أخطاء الـ ASCII
        with open("emails.txt", "r", encoding="utf-8") as f:
            emails = [line.strip() for line in f.readlines() if line.strip()]
    except:
        log("❌ Error: emails.txt not found!")
        return

    # تحديد العدد بـ 50 شخص فقط لضمان عدم الحظر
    target_list = emails[:50]
    log(f"📊 Safe Mode: Sending to {len(target_list)} people today.")

    for index, email in enumerate(target_list):
        try:
            target = email.strip()
            msg = MIMEMultipart()
            msg['From'] = f"Alamid Systems <{SENDER_EMAIL}>"
            msg['To'] = target
            msg['Subject'] = "Alamid System | منصة العميد"

            body = """
مرحباً بك،
منصة العميد تمنحك القوة القانونية عبر الذكاء الاصطناعي.
🔗 تجربة الـ 7 أيام مجاناً عبر تليجرام: https://t.me/Alamid_Bot
            """
            msg.attach(MIMEText(body, 'plain', 'utf-8'))

            # الاتصال بسيرفر جوجل
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(SENDER_EMAIL, GMAIL_APP_PASSWORD)
            server.send_message(msg)
            server.quit()
            
            log(f"✅ [{index+1}/50] Sent successfully to: {target}")
            
            # فاصل زمني طويل وعشوائي (60-90 ثانية) لمحاكاة الإرسال البشري وتجنب السبام
            wait_time = random.randint(60, 90)
            if index < len(target_list) - 1: # لا تنتظر بعد آخر إيميل
                log(f"⏳ Waiting {wait_time} seconds for safety...")
                time.sleep(wait_time)
            
        except Exception as e:
            log(f"❌ Failed for {email}: {str(e)}")

if __name__ == "__main__":
    start_mission()
