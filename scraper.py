import smtplib
import time
import random
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# إعدادات Mailjet (التي نعتمد عليها الآن)
SMTP_SERVER = "in-v3.mailjet.com"
SMTP_PORT = 587

# جلب المفاتيح من الخزنة (تأكد أن الأسماء مطابقة لما وضعته في Secrets)
API_KEY = os.getenv("MAILJET_API_KEY") 
SECRET_KEY = os.getenv("MAILJET_SECRET_KEY")
SENDER_EMAIL = "Alamid.Systems.2026@outlook.com"

def send_lawyer_email(target_email):
    try:
        msg = MIMEMultipart()
        msg['From'] = f"منصة العميد - ذكاء قانوني ⚖️ <{SENDER_EMAIL}>"
        msg['To'] = target_email
        msg['Subject'] = "⚠️ تنبيه نظامي: هل أعمالكم محمية من ثغرات 2026؟"

        body = """
مرحباً بك،

عالم الأنظمة السعودية يتطور بسرعة، ومنصة "العميد" تمنحك القوة القانونية عبر الذكاء الاصطناعي.
