import requests
import re
import time

def scout():
    # كلمات بحث لجلب إيميلات سعودية حقيقية
    queries = [
        'site:sa "law" "@gmail.com"',
        'site:sa "عقار" "@outlook.com"',
        'site:sa "شركة" "@hotmail.com"'
    ]
    
    found = set()
    headers = {'User-Agent': 'Mozilla/5.0'}

    for q in queries:
        try:
            url = f"https://www.google.com/search?q={q}"
            res = requests.get(url, headers=headers, timeout=10)
            emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', res.text)
            for e in emails:
                if not e.lower().endswith(('png', 'jpg', 'jpeg')):
                    found.add(e.lower())
        except: continue
        time.sleep(2)

    if found:
        with open("emails.txt", "a") as f:
            for e in found: f.write(e + "\n")
        print(f"✅ تم صيد {len(found)} هدف جديد.")

if __name__ == "__main__":
    scout()
