import requests
import re
import time
import random

def alamid_earthquake_scraper():
    # كلمات البحث "المفخخة" لجلب الإيميلات من قلب المواقع السعودية
    queries = [
        'site:sa "محامي" "@gmail.com"',
        'site:sa "مكتب محاماة" "@outlook.com"',
        'site:sa "عقارات" "الرياض" "@gmail.com"',
        'site:sa "مدير" "شركة" "@gmail.com"',
        'site:linkedin.com/in/ "Saudi" "Lawyer" "@gmail.com"',
        'site:twitter.com "المحامي" "السعودية" "@gmail.com"',
        'site:instagram.com "مكتب محاماة" "@gmail.com"',
        '"@pro.com.sa" محاماة',
        '"@legals.sa" شركة'
    ]
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
    }
    
    all_found = set()
    print("🌪️ بدأ إعصار العميد.. جاري سحب الملايين من قلب الإنترنت...")

    for q in queries:
        try:
            # استخدام محرك بحث Google (بدون API) لسحب النتائج
            url = f"https://www.google.com/search?q={q}&num=100"
            response = requests.get(url, headers=headers, timeout=15)
            
            # استخراج الإيميلات من نص الصفحة بالكامل
            emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', response.text)
            
            clean_emails = {e.lower() for e in emails if not e.lower().endswith(('png', 'jpg', 'jpeg', 'gif', 'svg', 'js'))}
            all_found.update(clean_emails)
            
            print(f"🔎 فحص: {q} ... تم صيد {len(clean_emails)} هدف.")
            
            # انتظار عشوائي ذكي عشان جوجل ما يزعل
            time.sleep(random.randint(15, 30))
            
        except Exception as e:
            print(f"⚠️ واجهنا مطب، لكن العميد ما يتوقف!")
            continue

    if all_found:
        with open("emails.txt", "a") as f:
            for email in all_found:
                f.write(email + "\n")
        print(f"\n✅ كفو! تم حصد {len(all_found)} إيميل حقيقي ومباشر من السوق السعودي.")
    else:
        print("🌑 يبدو أن جوجل يحجب النتائج حالياً، جرب تشغيل الـ Action مرة أخرى بعد قليل.")

if __name__ == "__main__":
    alamid_earthquake_scraper()
