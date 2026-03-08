import smtplib
import time
import random
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

# جلب البيانات من Secrets بأمان
EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASS = os.getenv("EMAIL_PASS")

def daily_safe_strike():
    # 1. قراءة الإيميلات
    try:
        with open("emails.txt", "r", encoding="utf-8") as f:
            all_targets = [line.strip() for line in f if "@" in line]
    except Exception as e:
        print(f"❌ خطأ في الملف: {e}")
        return

    # 2. تحديد "أول 100 هدف" فقط لليوم
    daily_limit = 100
    targets = all_targets[:daily_limit]

    print(f"🎯 مستعد لإرسال الدفعة اليومية ({len(targets)} هدف) بأمان تام...")

    # نصوص متنوعة لكسر نمط الآلي
    greetings = ["السلام عليكم ورحمة الله،", "تحية طيبة وبعد،", "مساء الخير،"]
    subjects = ["بخصوص حلول الذكاء الاصطناعي القانونية", "دعوة لتجربة نظام العميد الذكي 🇸🇦", "تطوير الخدمات الرقمية للمحامين"]

    for index, target in enumerate(targets):
        try:
            msg = MIMEMultipart()
            msg['From'] = f"العميد للتقنية <{EMAIL_USER}>"
            msg['To'] = target
            msg['Subject'] = Header(random.choice(subjects), 'utf-8')

            body = f"{random.choice(greetings)}\n\nنقدم لكم بوت العميد الذكي، المساعد التقني الأول المتوافق مع الأنظمة السعودية وصياغة العقود.\n\nيمكنكم تجربة البوت هنا: [رابط بوتك هنا]\n\nشكراً لوقتكم،\nفريق تطوير العميد 🦾"
            msg.attach(MIMEText(body, 'plain', 'utf-8'))

            # تنفيذ الإرسال
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(EMAIL_USER, EMAIL_PASS)
            server.sendmail(EMAIL_USER, target, msg.as_string())
            server.quit()

            print(f"✅ [{index+1}/100] تم الإرسال إلى: {target}")

            # 🕒 استراحة "بشرية" متغيرة (بين 45 و 90 ثانية)
            # هذا هو السر عشان إيميلك ما ينحظر أبداً
            wait_time = random.randint(45, 90)
            print(f"💤 استراحة أمان لمدة {wait_time} ثانية...")
            time.sleep(wait_time)

        except Exception as e:
            print(f"⚠️ خطأ مع {target}: {e}")
            time.sleep(30)
            continue

    print("🏁 كفو! تم الانتهاء من إرسال الـ 100 إيميل المخصصة لليوم.")

if __name__ == "__main__":
    daily_safe_strike()
