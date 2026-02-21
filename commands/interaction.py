from telegram import Update
from telegram.ext import ContextTypes

async def handle_messages(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    # التاك
    if text.lower() == "تاك":
        await update.message.reply_text(f"{update.effective_user.first_name}، انت غير مخول للدخول الى الشبكات الخاصة ❌")
    # الردود
    elif text.lower() == "انطقي":
        await update.message.reply_text("هاه؟ 😎")
