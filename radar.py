import os

EMAIL_FILE = "emails.txt"

def run_radar():
    """ينظف ملف emails.txt من التكرارات ويتأكد من وجود @"""
    if os.path.exists(EMAIL_FILE):
        with open(EMAIL_FILE, "r") as f:
            lines = f.readlines()

        clean_lines = sorted(set(line.strip() for line in lines if "@" in line))

        with open(EMAIL_FILE, "w") as f:
            for email in clean_lines:
                f.write(email + "\n")

        print(f"✅ الرادار جاهز. القائمة منقحة وتضم {len(clean_lines)} هدف.")
    else:
        print(f"⚠️ لم يتم العثور على الملف {EMAIL_FILE}.")

if __name__ == "__main__":
    run_radar()
