from telegram import Update
from telegram.ext import ContextTypes

async def my_balance(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("رصيدك: 5000 دينار")
