import telebot
import time
import os

# --- ضع توكن تليجرام حقك هنا مباشرة ---
TOKEN = "8717546599:AAHgnXRdPwoz1mV85LZft962ZU19xXnHBks" 

# --- اسم ملف الإيميلات اللي عندك في المستودع ---
EMAILS_FILE = "emails.txt" 

bot = telebot.TeleBot(TOKEN)

def load_emails():
    """وظيفة لسحب الإيميلات من ملفك"""
    if os.path.exists(EMAILS_FILE):
        with open(EMAILS_FILE, "r") as f:
            emails = [line.strip() for line in f.readlines() if "@" in line]
            return emails
    return []

@bot.message_handler(commands=['start'])
def welcome(message):
    emails = load_emails()
    count = len(emails)
    bot.reply_to(message, f"⚖️ منصة العميد جاهزة!\n\n📂 تم العثور على {count} إيميل في ملفك.\n🚀 المحرك جاهز لبدء عملية الاستقطاب.")

@bot.message_handler(commands=['strike'])
def start_strike(message):
    emails = load_emails()
    if not emails:
        bot.reply_to(message, "❌ لم أجد إيميلات في الملف! تأكد من وجود ملف باسم emails.txt")
        return
    
    bot.reply_to(message, f"🚀 بدأنا الصيد.. جاري مراسلة {len(emails)} عميل نخبة.")
    for email in emails:
        print(f"🎯 جاري استقطاب: {email}")
        # هنا تحط كود الإرسال الفعلي
        time.sleep(1) # تأخير بسيط لتجنب الحظر

# تشغيل مستمر
if __name__ == "__main__":
    print("🚀 [منصة العميد]: محرك الاستقطاب من ملفاتك يعمل الآن!")
    while True:
        try:
            bot.polling(none_stop=True, interval=0, timeout=20)
        except Exception as e:
            time.sleep(5)
