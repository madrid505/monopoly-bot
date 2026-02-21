from telegram import Update
from telegram.ext import ContextTypes
from config import BANK_DEFAULT, ADMIN_BANK, OWNER_BANK

balances = {}

async def bank_game(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if user_id == OWNER_ID:
        balances[user_id] = OWNER_BANK
    elif user_id in [/* IDs المدراء والمشرفين */]:
        balances[user_id] = ADMIN_BANK
    else:
        balances[user_id] = BANK_DEFAULT
    await update.message.reply_text(f"رصيدك الحالي: {balances[user_id]} دينار 💰")
