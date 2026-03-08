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
    log("🚀 [منصة العميد]: بدء محرك الإرسال الآمن...")
    
    if not GMAIL_APP_PASSWORD:
        log("❌ خطأ: مفتاح GMAIL_PASS مفقود في GitHub Secrets!")
        return

    try:
        # قراءة الإيميلات بتنسيق يمنع أخطاء الـ ASCII
        with open("emails.txt", "r", encoding="utf-8") as f:
            emails = [line.strip() for line in f.readlines() if line.strip()]
    except:
        log("❌ خطأ: ملف emails.txt غير موجود!")
        return

    # تحديد العدد بـ 50 شخص فقط لضمان عدم الحظر
    target_list = emails[:50]
    log(f"📊 وضع الأمان: سيتم الإرسال لـ {len(target_list)} شخص اليوم.")

    for index, email in enumerate(target_list):
        try:
            target = email.strip()
            msg = MIMEMultipart()
            msg['From'] = f"Alamid Systems <{SENDER_EMAIL}>"
            msg['To'] = target
            msg['Subject'] = "Alamid System | منصة العميد للذكاء القانوني"

            # النص المعدل باسم منصة العميد وبوتك
            body = """
مرحباً بك،

نحن في "منصة العميد" نضع بين يديك القوة القانونية مدعومة بأحدث تقنيات الذكاء الاصطناعي لعام 2026.

يسرنا دعوتك لتجربة نظامنا القانوني الذكي مجاناً لمدة 7 أيام عبر منصة تليجرام.

🔗 رابط التجربة المباشر: https://t.me/Alamid_Bot

مع تحيات،
فريق منصة العميد ⚖️
            """
            msg.attach(MIMEText(body, 'plain', 'utf-8'))

            # الاتصال بسيرفر جوجل
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(SENDER_EMAIL, GMAIL_APP_PASSWORD)
            server.send_message(msg)
            server.quit()
            
            log(f"✅ [{index+1}/50] تم الإرسال بنجاح إلى: {target}")
            
            # فاصل زمني طويل وعشوائي (60-90 ثانية) لمحاكاة الإرسال البشري
            if index < len(target_list) - 1:
                wait_time = random.randint(60, 90)
                log(f"⏳ انتظار {wait_time} ثانية للأمان...")
                time.sleep(wait_time)
            
        except Exception as e:
            log(f"❌ فشل الإرسال لـ {email}: {str(e)}")

if __name__ == "__main__":
    start_mission()
