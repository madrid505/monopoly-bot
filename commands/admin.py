from telegram import Update
from telegram.ext import ContextTypes

async def raise_rank(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("تم رفع الرتبة ✅")

async def lower_rank(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("تم تنزيل الرتبة ✅")
