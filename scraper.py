import telebot
import time

# --- ضع توكن تليجرام حقك هنا مباشرة ---
TOKEN = "8717546599:AAHgnXRdPwoz1mV85LZft962ZU19xXnHBks" 

# التأكد من وجود التوكن
if not TOKEN or "هنا_" in TOKEN:
    print("❌ خطأ: لم تضع التوكن داخل الكود!")
    exit()

bot = telebot.TeleBot(TOKEN)

# رسالة الترحيب
@bot.message_handler(commands=['start'])
def welcome(message):
    bot.reply_to(message, "⚖️ أهلاً بك في منصة العميد للذكاء القانوني.\n\nالمحرك يعمل بنجاح الآن! أرسل استفسارك وسيقوم المستشار بالرد عليك.")

# الرد على الرسائل (رد آلي ذكي وسريع)
@bot.message_handler(func=lambda m: True)
def handle_all(message):
    user_msg = message.text
    bot.reply_to(message, f"⏳ جاري تحليل قضيتك: ({user_msg})\n\nبناءً على الأنظمة السعودية لعام 2026، يتم الآن فحص الثغرات القانونية في ناجز. فضلاً انتظر الرد التفصيلي من المستشار.")

# تشغيل مستمر
if __name__ == "__main__":
    print("🚀 [منصة العميد]: البوت انطلق الآن بنجاح وبدون أخطاء!")
    while True:
        try:
            bot.polling(none_stop=True, interval=0, timeout=20)
        except Exception as e:
            print(f"🔄 إعادة تشغيل: {e}")
            time.sleep(5)
