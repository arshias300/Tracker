import telebot
import pandas as pd

TOKEN = "7727157587:AAHqAw42V1D1C9A1usCvIqAHz5NPUaKvYdg"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "سلام! لطفاً مقدار مورد نظر را ارسال کنید تا جستجو کنم.")

@bot.message_handler(func=lambda message: True)
def search_excel(message):
    try:
        df = pd.read_excel("data.xlsx")  # نام فایل اکسل
        query = message.text.strip()
        
        # جستجو در اکسل
        result = df[df.apply(lambda row: row.astype(str).str.contains(query, case=False).any(), axis=1)]
        
        if not result.empty:
            response = result.to_string(index=False)
        else:
            response = "موردی پیدا نشد!"
        
        bot.reply_to(message, response)
    
    except Exception as e:
        bot.reply_to(message, f"خطا: {str(e)}")

bot.polling()
