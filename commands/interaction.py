from telegram import Update
from telegram.ext import ContextTypes

async def handle_messages(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if text.lower() == "انطقي":
        await update.message.reply_text("هاه؟ 😎")
