import os
import telebot
import time

TOKEN = os.getenv("MS_APP_PASS")

if not TOKEN:
    print("❌ خطأ: لم يتم العثور على توكن تليجرام (MS_APP_PASS)!")
    exit(1)

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.reply_to(message, "⚖️ مرحباً بك في منصة العميد.\nتم الانتهاء من استقطاب العملاء، والمكتب مفتوح الآن لاستفساراتك.")

@bot.message_handler(func=lambda m: True)
def handle_case(message):
    bot.reply_to(message, f"⏳ جاري تحليل قضيتك: ({message.text})\nبناءً على الأنظمة السعودية لعام 2026، يتم استخراج الثغرات الآن...")

if __name__ == "__main__":
    print("🚀 [منصة العميد]: البوت يعمل الآن...")
    while True:
        try:
            bot.polling(none_stop=True)
        except Exception:
            time.sleep(5)
