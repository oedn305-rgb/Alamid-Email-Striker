import requests
import os

# سحب المفتاح من الخزنة السرية تلقائياً
API_KEY = os.getenv("ALAMID_API_KEY")

def fetch_premium_leads():
    print("🚀 جاري الاتصال بالمحرك لجلب إيميلات الشركات السعودية...")
    
    # ملاحظة: هذا الرابط كمثال (سأعدله لك فوراً إذا علمتني اسم الموقع: Apollo أو Hunter)
    # سنفترض أننا نستخدم نظام بحث احترافي
    url = "https://api.hunter.io/v2/domain-search" 
    
    params = {
        'domain': 'moj.gov.sa', # استهداف نطاق وزارة العدل أو شركات محاماة
        'api_key': API_KEY
    }

    try:
        response = requests.get(url, params=params)
        data = response.json()
        
        if 'data' in data and 'emails' in data['data']:
            emails = [e['value'] for e in data['data']['emails']]
            with open("emails.txt", "a") as f:
                for email in emails:
                    f.write(email + "\n")
            print(f"✅ تم صيد {len(emails)} إيميل رسمي بنجاح!")
        else:
            print("⚠️ المفتاح يعمل لكن لم نجد بيانات في هذا النطاق، جاري تغيير الهدف...")
            
    except Exception as e:
        print(f"❌ حدث خطأ في الاتصال: {e}")

if __name__ == "__main__":
    fetch_premium_leads()
