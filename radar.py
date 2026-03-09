import os

EMAIL_FILE = "emails.txt"

def run_radar():
    if not os.path.exists(EMAIL_FILE):
        print("❌ ملف emails.txt غير موجود")
        return

    with open(EMAIL_FILE, "r") as f:
        lines = f.readlines()

    clean_emails = sorted(set(line.strip() for line in lines if "@" in line))

    with open(EMAIL_FILE, "w") as f:
        for email in clean_emails:
            f.write(email + "\n")

    print(f"✅ تم تنظيف القائمة. عدد الإيميلات: {len(clean_emails)}")

if __name__ == "__main__":
    run_radar()
