import logging  
import pandas as pd  
import os  
from telegram import Update  
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext  

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)  
logger = logging.getLogger(__name__)  

# 7727157587:AAHqAw42V1D1C9A1usCvIqAHz5NPUaKvYdg  
TOKEN = os.environ['TELEGRAM_TOKEN']  

# بارگذاری داده‌های اکسل  
file_path = 'your_file.xlsx'  # نام فایل اکسل خود را قرار دهید  
df = pd.read_excel(file_path)  

def start(update: Update, context: CallbackContext) -> None:  
    logger.info("Start command received.")  
    update.message.reply_text('سلام! لطفا سوال خود را بپرسید.')  

def search_data(update: Update, context: CallbackContext) -> None:  
    query = " ".join(context.args)  
    logger.info(f"Search query: {query}")  
    results = df[df.apply(lambda row: row.astype(str).str.contains(query).any(), axis=1)]  
    if not results.empty:  
        update.message.reply_text(results.to_string(index=False))  
    else:  
        update.message.reply_text("هیچ داده‌ای پیدا نشد.")  

def main():  
    updater = Updater(TOKEN, use_context=True)  
    dispatcher = updater.dispatcher  
    dispatcher.add_handler(CommandHandler("start", start))  
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, search_data))  
    updater.start_polling()  
    logger.info("Bot is polling...")  
    updater.idle()  

if __name__ == '__main__':  
    main()  
