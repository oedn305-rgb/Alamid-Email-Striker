import os

def run_radar():
    """ينظف ملف emails.txt من التكرارات ويتأكد من صحة الإيميلات"""
    file_path = "emails.txt"

    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            lines = f.readlines()

        # تنظيف: إزالة الفراغات، التأكد من وجود @، وإزالة التكرارات
        clean_lines = sorted(set(line.strip() for line in lines if "@" in line))

        # إعادة كتابة الملف بالقائمة المنقحة
        with open(file_path, "w") as f:
            for email in clean_lines:
                f.write(email + "\n")

        print(f"✅ الرادار جاهز. القائمة منقحة وتضم {len(clean_lines)} هدف.")
    else:
        print(f"⚠️ لم يتم العثور على الملف {file_path}. الرجاء التأكد من وجوده.")

if __name__ == "__main__":
    run_radar()
