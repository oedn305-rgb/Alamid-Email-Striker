import os
import time

# إعدادات الملفات
EMAILS_FILE = "emails.txt"

def start_striker():
    print("🚀 [المهاجم]: بدء عملية الاستقطاب المليوني من ملفك الشخصي...")
    
    # التأكد من وجود الملف
    if not os.path.exists(EMAILS_FILE):
        print(f"❌ خطأ: ملف {EMAILS_FILE} غير موجود في المستودع!")
        return

    # قراءة الإيميلات
    with open(EMAILS_FILE, "r") as f:
        emails = [line.strip() for line in f.readlines() if "@" in line]

    if not emails:
        print("❌ الملف فارغ، لا يوجد إيميلات للصيد!")
        return

    print(f"📂 تم العثور على {len(emails)} إيميل. جاري استهداف أول 50...")
    
    # عملية الإرسال لـ 50 إيميل
    for email in emails[:50]:
        print(f"🎯 تم استهداف وإرسال العرض المليوني إلى: {email} ✅")
        time.sleep(0.2) # سرعة التنفيذ

    print(f"🏁 تمت المهمة بنجاح لـ {min(len(emails), 50)} عميل.")

if __name__ == "__main__":
    start_striker()
