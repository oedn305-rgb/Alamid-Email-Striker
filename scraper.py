import requests
import os

# توكن المحرك (تاخذه مجاناً من Hunter.io)
HUNTER_API_KEY = "ضع_هنا_مفتاح_API" 

def auto_hunt_direct():
    # استهداف شركات في السعودية (تقدر تغير الكلمة لأي قطاع)
    # البحث هنا يعتمد على "الدومينات" يعني يعطيك إيميلات رسمية @company.com
    domains = ["moj.gov.sa", "saudilegal.com", "mci.gov.sa"] # أمثلة لجهات قانونية/تجارية
    
    print("🎯 جاري استخراج إيميلات حقيقية من المحرك الدايركت...")
    
    found_leads = []
    for domain in domains:
        url = f"https://api.hunter.io/v2/domain-search?domain={domain}&api_key={HUNTER_API_KEY}"
        try:
            response = requests.get(url)
            data = response.json()
            for email_data in data['data']['emails']:
                found_leads.append(email_data['value'])
        except:
            continue

    if found_leads:
        with open("emails.txt", "a") as f:
            for email in set(found_leads):
                f.write(email + "\n")
        print(f"✅ تم صيد {len(found_leads)} إيميلات رسمية بنجاح!")

if __name__ == "__main__":
    auto_hunt_direct()
