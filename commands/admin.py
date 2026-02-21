from telegram import Update
from telegram.ext import ContextTypes

async def raise_rank(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("تم رفع الرتبة ✅")

async def lower_rank(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("تم تنزيل الرتبة ✅")

async def clear_rank(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("تم مسح الرتبة ✅")

async def ban(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("تم حظر العضو ❌")

async def mute(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("تم كتم العضو 🔇")
