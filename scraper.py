import smtplib
import os
import time
import random
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# إعدادات العميد
SENDER_EMAIL = "Alamid.Systems.2026@outlook.com"
APP_PASSWORD = os.getenv("MS_APP_PASS") 

def send_mail(target):
    try:
        msg = MIMEMultipart()
        # جعل الاسم يظهر بشكل فخم وموثوق
        msg['From'] = f"العميد | الأنظمة السعودية ⚖️ <{SENDER_EMAIL}>"
        msg['To'] = target
        msg['Subject'] = "تنبيه للمنشآت: تحديثات الأنظمة السعودية لعام 2026"

        body = f"""مرحباً،
تغيرات كبيرة طرأت على الأنظمة القانونية في المملكة هذا العام.
منصة "العميد" تستخدم الذكاء الاصطناعي لحماية أعمالكم من الثغرات القانونية.

🔗 ابدأ فحص قضاياك وعقودك الآن مجاناً:
https://t.me/Alamid_Bot

فريق العميد التقني."""
        
        msg.attach(MIMEText(body, 'plain', 'utf-8'))

        server = smtplib.SMTP("smtp.office365.com", 587)
        server.starttls()
        server.login(SENDER_EMAIL, APP_PASSWORD)
        server.send_message(msg)
        server.quit()
        return True
    except Exception as e:
        print(f"❌ لم يتم الإرسال لـ {target}")
        return False

if __name__ == "__main__":
    if not APP_PASSWORD:
        print("❌ تأكد من ضبط Secrets!")
    else:
        with open("emails.txt", "r") as f:
            # قراءة الإيميلات الجديدة فقط ومنع التكرار
            all_emails = list(set([line.strip() for line in f.readlines() if "@" in line]))
        
        # نرسل لـ 50 هدف فقط في كل جولة لضمان الأمان التام
        targets = all_emails[:50] 
        print(f"🚀 جاري مراسلة {len(targets)} هدف ذكي...")

        for email in targets:
            if send_mail(email):
                print(f"✅ تم الوصول لـ: {email}")
                # انتظار طويل وعشوائي بين كل إيميل (سر الأمان)
                time.sleep(random.randint(90, 180))
