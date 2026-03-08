import smtplib
import time
import random
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASS = os.getenv("EMAIL_PASS")

def anti_block_strike():
    try:
        with open("emails.txt", "r", encoding="utf-8") as f:
            targets = [line.strip() for line in f if "@" in line]
    except Exception as e:
        print(f"❌ خطأ في الملف: {e}")
        return

    # كلمات للتبديل (عشان كل رسالة تطلع مختلفة شوي)
    greetings = ["السلام عليكم ورحمة الله", "تحية طيبة وبعد،", "مساء الخير،", "أهلاً بكم،"]
    closings = ["تحياتنا،", "مع التقدير،", "فريق العمل،", "شكراً لكم،"]

    print(f"🚀 بدء الإرسال الآمن لـ {len(targets)} هدف...")

    # إرسال فردي (إيميل لكل شخص) - هذا أضمن بكثير من الـ BCC للكميات الكبيرة
    for index, target in enumerate(targets):
        try:
            msg = MIMEMultipart()
            msg['From'] = f"العميد للتقنية <{EMAIL_USER}>"
            msg['To'] = target
            
            # تغيير العنوان بشكل عشوائي بسيط
            subjects = ["تطوير الأنظمة القانونية", "حلول الذكاء الاصطناعي للمحامين", "استفسار بخصوص الخدمات الرقمية"]
            msg['Subject'] = Header(random.choice(subjects), 'utf-8')

            # بناء نص متغير
            body = f"{random.choice(greetings)}\n\nنقدم لكم بوت العميد الذكي المتخصص في الأنظمة السعودية.\nجرب المستقبل هنا: [رابط البوت]\n\n{random.choice(closings)}"
            msg.attach(MIMEText(body, 'plain', 'utf-8'))

            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(EMAIL_USER, EMAIL_PASS)
            server.sendmail(EMAIL_USER, target, msg.as_string())
            server.quit()

            print(f"✅ تم الإرسال إلى {target} ({index+1}/{len(targets)})")

            # 🕒 استراحة "بشرية" (بين 20 إلى 45 ثانية بين كل إيميل)
            # هذا يخليك ترسل طول اليوم بدون ما تنكشف
            wait = random.randint(20, 45)
            time.sleep(wait)

            # كل 50 إيميل خذ استراحة طويلة (10 دقائق) عشان تبرد السيرفر
            if (index + 1) % 50 == 0:
                print("💤 استراحة طويلة لمدة 10 دقائق لضمان الأمان...")
                time.sleep(600)

        except Exception as e:
            print(f"⚠️ فشل مع {target}: {e}")
            time.sleep(60)
            continue

if __name__ == "__main__":
    anti_block_strike()
