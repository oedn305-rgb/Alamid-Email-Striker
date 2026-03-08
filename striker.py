import smtplib
import time
import os
import sys
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# --- إعدادات الحساب ---
# استبدل الإيميل اللي تحت بإيميلك الـ Gmail اللي طلعت له الكود الأصفر
SENDER_EMAIL = "اكتب_إيميلك_هنا@gmail.com" 
GMAIL_APP_PASSWORD = os.getenv("GMAIL_PASS") # الكود الأصفر المكون من 16 حرف

# إعدادات سيرفر جوجل الثابتة
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

def log(msg):
    """وظيفة لطباعة النتائج فوراً في الشاشة السوداء بـ GitHub"""
    print(f">>> {msg}")
    sys.stdout.flush()

def start_mission():
    log("🚀 [منصة العميد]: محرك Gmail بدأ العمل الآن...")
    
    if not GMAIL_APP_PASSWORD:
        log("❌ خطأ: لم تجد النظام مفتاح GMAIL_PASS في الـ Secrets!")
        return

    # التأكد من وجود ملف الإيميلات
    if not os.path.exists("emails.txt"):
        log("❌ خطأ: ملف emails.txt مفقود من المستودع!")
        return

    # قراءة الإيميلات من الملف
    with open("emails.txt", "r") as f:
        emails = [line.strip() for line in f.readlines() if line.strip()]

    log(f"📊 فحص القائمة: وجدنا {len(emails)} إيميل جاهز.")
    log("-----------------------------------------")

    # إرسال أول 100 إيميل (نطاق الأمان لجوجل)
    for index, email in enumerate(emails[:100]):
        try:
            # تجهيز محتوى الرسالة
            msg = MIMEMultipart()
            msg['From'] = f"منصة العميد ⚖️ <{SENDER_EMAIL}>"
            msg['To'] = email
            msg['Subject'] = "تنبيه نظامي: هل أعمالكم محمية من ثغرات 2026؟"
            
            body = """
مرحباً بك،
نحن في منصة العميد نغير مفهوم الحلول القانونية باستخدام الذكاء الاصطناعي.
ندعوك لتجربة نظامنا الجديد مجاناً لمدة 7 أيام عبر تليجرام.

🔗 رابط التجربة: https://t.me/Alamid_Bot
            """
            msg.attach(MIMEText(body, 'plain', 'utf-8'))

            # الاتصال بسيرفر Gmail والإرسال
            server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
            server.starttls()
            server.login(SENDER_EMAIL, GMAIL_APP_PASSWORD)
            server.send_message(msg)
            server.quit()
            
            log(f"✅ [{index+1}] تم الإرسال بنجاح إلى: {email}")
            
            # وقت راحة 15 ثانية بين كل إيميل (ضروري جداً لتجنب الحظر)
            time.sleep(15)
            
        except Exception as e:
            log(f"❌ فشل الإرسال لـ {email}. السبب: {str(e)}")

if __name__ == "__main__":
    start_mission()
