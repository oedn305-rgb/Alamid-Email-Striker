import requests
import os
import time

# سحب المفتاح السري من إعدادات GitHub
API_KEY = os.getenv("ALAMID_API_KEY")

def fetch_all_saudi_domains():
    # قائمة النطاقات الذهبية (وزارات، كبار المكاتب، وشركات كبرى)
    target_domains = [
        # قطاع العدل والقانون
        "moj.gov.sa", "moj.sa", "sba.gov.sa", "mohr.gov.sa",
        # قطاع العقارات والمقاولات
        "nhc.sa", "redf.gov.sa", "saudibuild.com", "alkifah.com.sa",
        # قطاع الشركات والمدراء
        "aramco.com", "sabic.com", "stc.com.sa", "maaden.com.sa",
        # نطاقات عامة للشركات السعودية
        "chamber.org.sa", "riyadhchamber.com", "jeddahchamber.org.sa",
        # مكاتب استشارات كبرى (أمثلة)
        "al-adel.com.sa", "saudilegal.com", "alsabhan-alajlan.com"
    ]
    
    print(f"🚀 انطلاق رادار العميد لمسح {len(target_domains)} نطاق استراتيجي...")
    
    total_found = 0
    
    for domain in target_domains:
        # ملاحظة: الرابط مخصص لـ Hunter.io لأنه الأكثر استخداماً للنطاقات
        url = f"https://api.hunter.io/v2/domain-search?domain={domain}&api_key={API_KEY}"
        
        try:
            print(f"📡 فحص النطاق: {domain} ...")
            response = requests.get(url, timeout=10)
            data = response.json()
            
            if 'data' in data and data['data']['emails']:
                emails = [e['value'] for e in data['data']['emails']]
                with open("emails.txt", "a") as f:
                    for email in emails:
                        f.write(email + "\n")
                
                count = len(emails)
                total_found += count
                print(f"✅ تم صيد {count} إيميل رسمي من {domain}")
            else:
                print(f"➖ {domain}: لا توجد بيانات عامة متاحة حالياً.")
            
            # انتظار بسيط لتجنب ضغط الـ API
            time.sleep(1)
            
        except Exception as e:
            print(f"⚠️ خطأ في فحص {domain}: {e}")
            continue

    print(f"\n✨ انتهت المهمة! مجموع ما تم صيده: {total_found} هدف ذكي.")

if __name__ == "__main__":
    fetch_all_saudi_domains()
