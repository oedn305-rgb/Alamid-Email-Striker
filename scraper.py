import os
import telebot
import time

# المحرك يسحب التوكن المستقل من الملف السري (Secrets)
TOKEN = os.getenv("MS_APP_PASS")

if not TOKEN:
    print("❌ خطأ: لم يتم العثور على التوكن في السيكرتس. تأكد من اسم MS_APP_PASS")
    exit(1)

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    # رسالة الترحيب الاحترافية لعام 2026
    bot.reply_to(message, "⚖️ مرحباً بك في منصة العميد للاستشارات القانونية.\n\nتم تفعيل النظام بنجاح، ونحن الآن في طور تحليل البيانات واستقطاب العملاء.")

@bot.message_handler(func=lambda m: True)
def handle_messages(message):
    # الرد التلقائي لتحليل القضايا
    bot.reply_to(message, f"⏳ جاري فحص استفسارك: ({message.text})\nيتم الآن مطابقة الحالة مع الأنظمة السعودية الحديثة...")

if __name__ == "__main__":
    print("🚀 [منصة العميد]: البوت متصل الآن ويسحب البيانات من السيكرتس...")
    while True:
        try:
            bot.polling(none_stop=True)
        except Exception as e:
            print(f"🔄 إعادة محاولة الاتصال بسبب: {e}")
            time.sleep(5)
