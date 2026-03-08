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
    log("🚀 [منصة العميد]: إطلاق محرك الاستقطاب المليوني...")
    
    if not GMAIL_APP_PASSWORD:
        log("❌ خطأ: مفتاح GMAIL_PASS مفقود في GitHub Secrets!")
        return

    try:
        with open("emails.txt", "r", encoding="utf-8") as f:
            emails = [line.strip() for line in f.readlines() if line.strip()]
    except:
        log("❌ خطأ: ملف emails.txt غير موجود!")
        return

    target_list = emails[:50] # 50 شخص لضمان أعلى مستوى أمان لحسابك
    log(f"📊 وضع القوة: استهداف {len(target_list)} عميل نخبة الآن.")

    for index, email in enumerate(target_list):
        try:
            target = email.strip()
            msg = MIMEMultipart()
            msg['From'] = f"Alamid Systems | منصة العميد ⚖️ <{SENDER_EMAIL}>"
            msg['To'] = target
            msg['Subject'] = "فرصة نظامية: مستشارك القانوني الذكي بانتظارك (دعوة خاصة) ⚖️"

            # نص احترافي "مغناطيسي" للاشتراك الفوري
            body = """
بكل تقدير،

في عصر السرعة ونيوم 2026، لم يعد البحث التقليدي كافياً. نحن في "منصة العميد" نفتح لك أبواب المستقبل القانوني في المملكة العربية السعودية.

لماذا يشترك الآلاف في "المحامي الذكي" الآن؟
✅ ذكاء اصطناعي يفهم الأنظمة السعودية بدقة 100%.
✅ صياغة مذكرات، استشارات فنية، وتحليل ثغرات في ثوانٍ.
✅ متاح لك 24/7.. مستشارك في جيبك أينما كنت.

🎁 هدية حصرية لك:
لقد تم اختيارك لتجربة "النسخة الاحترافية" مجاناً لمدة 7 أيام. لا تدع الفرصة تفوتك لتكون ضمن النخبة التي تدير أعمالها بذكاء.

🔗 ابدأ التجربة الفورية الآن عبر تليجرام:
https://t.me/SaudiLegal_AI_bot

انضم لثورة القانون الذكي.. منصة العميد، حيث الهيبة والسرعة.

مع تحيات،
إدارة العمليات | منصة العميد ⚖️
            """
            msg.attach(MIMEText(body, 'plain', 'utf-8'))

            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(SENDER_EMAIL, GMAIL_APP_PASSWORD)
            server.send_message(msg)
            server.quit()
            
            log(f"✅ [{index+1}/50] تم الإرسال بنجاح لـ: {target}")
            
            # فاصل أمان (60-90 ثانية)
            if index < len(target_list) - 1:
                wait_time = random.randint(60, 90)
                log(f"⏳ أمان: ننتظر {wait_time} ثانية قبل الهدف التالي...")
                time.sleep(wait_time)
            
        except Exception as e:
            log(f"❌ فشل الإرسال لـ {email}: {str(e)}")

if __name__ == "__main__":
    start_mission()
