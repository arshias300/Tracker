import telebot
import pandas as pd

TOKEN =7727157587:AAHqAw42V1D1C9A1usCvIqAHz5NPUaKvYdg
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
روی Commit changes کلیک کن تا ذخیره شود.
4. اتصال GitHub به Railway برای اجرای ربات
به Railway برو و ثبت‌نام کن.
گزینه New Project را بزن.
گزینه Deploy from GitHub repo را انتخاب کن.
مخزن ExcelTelegramBot خودت را انتخاب کن.
در Railway وارد Settings شو و در قسمت Environment Variables این مقدار را اضافه کن:
TOKEN = توکن ربات تلگرام
به Deployments برو و گزینه Deploy را بزن.
5. آپلود فایل اکسل و تست ربات
در GitHub گزینه Add file → Upload file را بزن.
فایل data.xlsx را آپلود کن (این همان فایلی است که ربات جستجو می‌کند).
در تلگرام، ربات را Start کن و یک مقدار بفرست تا نتیجه را بگیری.
این روش باعث می‌شود ربات همیشه آنلاین باشد و با فایل اکسل کار کند. هر تغییری که در GitHub بدهی، روی Railway اجرا می‌شود. اگر سوالی داشتی، بپرس!










Search

Reason

ChatGPT can make
