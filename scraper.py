import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

# تأكد أنك وضعت هذه البيانات في Settings > Secrets في مستودعك
EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASS = os.getenv("EMAIL_PASS")

def strike_one_shot():
    # 1. قراءة الـ 1,000 إيميل من ملف emails.txt
    try:
        with open("emails.txt", "r") as f:
            # تنظيف القائمة والتأكد من وجود إيميلات حقيقية
            targets = [line.strip() for line in f if "@" in line]
    except FileNotFoundError:
        print("❌ خطأ: ملف emails.txt غير موجود!")
        return

    if not targets:
        print("❌ ملف الإيميلات فارغ!")
        return

    print(f"🚀 جاري تجهيز الهجوم لـ {len(targets)} هدف قانوني...")

    # 2. إعداد الرسالة (عرض العميد الصاعق)
    msg = MIMEMultipart()
    msg['From'] = f"Alamid AI <{EMAIL_USER}>"
    msg['To'] = EMAIL_USER  # ترسلها لنفسك وتضع الباقي مخفي
    msg['Subject'] = "⚖️ دعوة للنخبة: بوت المحامي السعودي الذكي - مستقبل القانون"

    body = """
    السلام عليكم ورحمة الله وبركاته،
    
    يسرنا دعوتكم لتجربة "بوت العميد الذكي" 🇸🇦.
    أول نظام ذكاء اصطناعي متخصص في الأنظمة السعودية لخدمة المحامين والمستشارين.
    
    ✅ صياغة مذكرات وعقود في ثوانٍ.
    ✅ استشارات قانونية فورية بناءً على الأنظمة المحدثة.
    ✅ توفير 90% من وقت البحث في "ناجز" واللوائح.
    
    جرب البوت الآن مجاناً عبر الرابط التالي:
    [ضع رابط بوتك هنا]
    
    تحياتنا،
    فريق تطوير العميد 🦾
    """
    msg.attach(MIMEText(body, 'plain'))

    # 3. تنفيذ "الضربة الواحدة" (BCC)
    try:
        # الاتصال بسيرفر Gmail
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(EMAIL_USER, EMAIL_PASS)
        
        # إرسال الرسالة للكل دفعة واحدة (مخفي)
        server.sendmail(EMAIL_USER, targets, msg.as_string())
        server.quit()
        
        print(f"✅ كفو! تم إرسال العرض لـ {len(targets)} شخص في رسالة واحدة بنجاح.")
        
    except Exception as e:
        print(f"❌ فشل الإرسال: {e}")

if __name__ == "__main__":
    strike_one_shot()
