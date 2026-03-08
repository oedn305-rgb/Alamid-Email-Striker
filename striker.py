import smtplib
import time
import random
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# --- الإعدادات الفنية لـ "العميد" ---
# تأكد أن اسم الـ Secret في GitHub هو: MS_APP_PASS
SENDER_EMAIL = "Alamid.Systems.2026@outlook.com" 
APP_PASSWORD = os.getenv("MS_APP_PASS") # سحب الرمز السري آلياً

def send_marketing_email(target_email):
    """إرسال إيميل واحد مع تشفير آمن"""
    try:
        msg = MIMEMultipart()
        msg['From'] = f"منصة العميد - ذكاء قانوني ⚖️ <{SENDER_EMAIL}>"
        msg['To'] = target_email
        msg['Subject'] = "⚠️ تنبيه نظامي: هل أعمالكم محمية من ثغرات 2026؟"

        body = f"""
أهلاً بك،

عالم الأنظمة السعودية في 2026 يتطور بسرعة، والتحديات القانونية تتطلب أدوات ذكية لمواكبتها.

يسرنا في "منصة العميد" دعوتك لتجربة أول محرك ذكاء اصطناعي متخصص في كشف الثغرات القانونية السعودية.

💡 مميزات "العميد":
✅ تحليل فوري للمذكرات (جنائي، تجاري، عمالي).
✅ استنباط الثغرات النظامية بناءً على مبادئ المحكمة العليا.
✅ صياغة ردود قانونية محكمة.

🎁 تجربة مجانية لمدة 7 أيام.
🔗 انضم الآن عبر تليجرام: [ضع رابط بوتك هنا]

منصة العميد - القوة القانونية بين يديك.
        """
        
        msg.attach(MIMEText(body, 'plain', 'utf-8'))

        # الاتصال بسيرفر مايكروسوفت (لأن إيميلك Outlook)
        server = smtplib.SMTP("smtp.office365.com", 587)
        server.starttls() 
        server.login(SENDER_EMAIL, APP_PASSWORD)
        server.send_message(msg)
        server.quit()
        return True
    except Exception as e:
        print(f"❌ فشل الإرسال لـ {target_email}: {e}")
        return False

def run_campaign():
    """تشغيل الحملة بنظام التنقيط لتجنب الحظر"""
    if not APP_PASSWORD:
        print("❌ خطأ: الرمز السري MS_APP_PASS غير موجود في الـ Secrets!")
        return

    # سحب قائمة الإيميلات من الملف
    try:
        with open("emails.txt", "r") as f:
            all_emails = [line.strip() for line in f.readlines() if line.strip()]
    except FileNotFoundError:
        print("❌ خطأ: ملف emails.txt غير موجود!")
        return

    # استهداف أول 100 جهة كما طلبت
    target_list = all_emails[:100]
    print(f"🚀 [العميد التقني]: بدء الإرسال لـ {len(target_list)} جهة قانونية...")

    for index, email in enumerate(target_list):
        success = send_marketing_email(email)
        if success:
            print(f"✅ [{index+1}/100] تم الإرسال بنجاح: {email}")
        
        # --- استراتيجية "التسلل" لمنع الحظر ---
        if index < len(target_list) - 1:
            # ننتظر بين 3 إلى 5 دقائق بين كل إيميل وإيميل (أمان قصوى)
            wait_time = random.randint(180, 300) 
            print(f"⏳ استراحة أمان لمدة {wait_time // 60} دقائق لمنع السبام...")
            time.sleep(wait_time)

    print("🏁 اكتملت العملية. تم إرسال الدفعة الأولى بنجاح!")

if __name__ == "__main__":
    run_campaign()
