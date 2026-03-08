import telebot
import time
from duckduckgo_search import DDGS

# --- ضع توكن تليجرام حقك هنا مباشرة (بين علامتي التنصيص) ---
TOKEN = "8717546599:AAHgnXRdPwoz1mV85LZft962ZU19xXnHBks"

# التحقق من وجود التوكن لتجنب الخطأ القاتل
if not TOKEN or "هنا_" in TOKEN:
    print("❌ خطأ: لم تضع التوكن داخل الكود! يرجى وضعه ليعمل البوت.")
    exit()

bot = telebot.TeleBot(TOKEN)

# دالة الذكاء الاصطناعي (مجانية وبدون مفتاح قوقل)
def get_ai_answer(text):
    try:
        with DDGS() as ddgs:
            prompt = f"أنت المحامي العميد، خبير قانوني سعودي 2026. حلل هذه القضية بسرد فخم وثقة: {text}"
            return ddgs.chat(prompt, model='gpt-4o-mini')
    except:
        return "⏳ المستشار مشغول بمراجعة الأنظمة، حاول ثانية."

# الأوامر
@bot.message_handler(commands=['start'])
def welcome(message):
    bot.reply_to(message, "⚖️ أهلاً بك في منصة العميد.\nبوتي يعمل الآن بنجاح، أرسل قضيتك لتحليلها.")

@bot.message_handler(func=lambda m: True)
def handle_all(message):
    wait = bot.reply_to(message, "⏳ جاري السرد والتحليل القانوني...")
    answer = get_ai_answer(message.text)
    bot.edit_message_text(answer, message.chat.id, wait.message_id)

# تشغيل نهائي ومستمر
if __name__ == "__main__":
    print("🚀 [منصة العميد]: المحرك يعمل الآن غصب عن الظروف!")
    while True:
        try:
            bot.polling(none_stop=True, interval=0, timeout=20)
        except Exception:
            time.sleep(5)
