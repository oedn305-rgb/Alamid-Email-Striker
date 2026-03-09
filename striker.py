import os
import smtplib
import time
from email.message import EmailMessage

EMAIL_FILE = "emails.txt"

def start_striker():

    EMAIL = os.getenv("GMAIL_USER")
    PASSWORD = os.getenv("GMAIL_PASS")

    if not EMAIL or not PASSWORD:
        print("❌ Secrets ناقصة")
        return

    if not os.path.exists(EMAIL_FILE):
        print("❌ ملف emails.txt غير موجود")
        return

    with open(EMAIL_FILE, "r") as f:
        targets = [line.strip() for line in f if "@" in line]

    print(f"📡 سيتم الإرسال إلى {len(targets)} إيميل")

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:

            smtp.login(EMAIL, PASSWORD)

            for
