import requests
import re
import time
import random
import os

EMAIL_FILE = "emails.txt"

def scout_for_leads():
    """جمع الإيميلات من محركات البحث"""
    search_queries = [
        'site:sa "law" "@gmail.com"',
        'site:sa "محاماة" "@outlook.com"',
        'site:linkedin.com/in/ "CEO" "Saudi Arabia" "@gmail.com"',
        'site:linkedin.com/in/ "مدير" "السعودية" "@outlook.com"',
        'site:twitter.com "محامي" "السعودية" "@gmail.com"',
        'site:sa "عقارات" "@hotmail.com"',
        'site:sa "شركة" "الرياض" "@gmail.com"'
    ]

    found_emails = set()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
    }

    print("📡 بدأ جمع الإيميلات...")

    for query in search_queries:
        try:
            url = f"https://www.google.com/search?q={query}"
            response = requests.get(url, headers=headers, timeout=15)
            emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', response.text)
            for email in emails:
                if not email.lower().endswith(('png','jpg','jpeg','gif','pdf','svg')):
                    found_emails.add(email.lower())
            print(f"🔍 تم فحص: {query} ... وجدنا {len(emails)} إيميل")
            time.sleep(random.randint(5, 10))
        except Exception as e:
            print(f"⚠️ خطأ في البحث: {e}")
            continue

    # قراءة القوائم القديمة
    existing_emails = set()
    if os.path.exists(EMAIL_FILE):
        with open(EMAIL_FILE, "r") as f:
            existing_emails = set(line.strip().lower() for line in f)

    new_emails = found_emails - existing_emails
    if new_emails:
        with open(EMAIL_FILE, "a") as f:
            for email in new_emails:
                f.write(email + "\n")
        print(f"✅ تم صيد {len(new_emails)} إيميل جديد.")
    else:
        print("🌑 لم يتم العثور على إيميلات جديدة.")

if __name__ == "__main__":
    scout_for_leads()
