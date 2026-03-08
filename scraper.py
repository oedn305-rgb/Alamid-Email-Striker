import os

def run_radar():
    print("📡 [الرادار]: جاري فحص تحديثات ملف الإيميلات...")
    if os.path.exists("emails.txt"):
        with open("emails.txt", "r") as f:
            count = len(f.readlines())
        print(f"✅ الرادار أكد وجود {count} هدف في ملفك الحالي.")
    else:
        print("⚠️ الرادار لم يجد أهدافاً جديدة.")

if __name__ == "__main__":
    run_radar()
