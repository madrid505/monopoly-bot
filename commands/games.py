from telegram import Update
from telegram.ext import ContextTypes

async def roulette(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("بدأت لعبة الروليت 🎲")

async def photo_game(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("لعبة الصور شغالة 🖼️")
