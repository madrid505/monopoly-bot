from telegram import Update
from telegram.ext import ContextTypes
from config import BANK_DEFAULT, ADMIN_BANK, OWNER_BANK, OWNER_ID

balances = {}

async def bank_game(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    
    if user_id == OWNER_ID:
        balances[user_id] = OWNER_BANK
    elif user_id in []:  # ضع هنا IDs المدراء والمشرفين، مثال: [12345678, 87654321]
        balances[user_id] = ADMIN_BANK
    else:
        balances[user_id] = BANK_DEFAULT
    
    await update.message.reply_text(f"رصيدك الحالي: {balances[user_id]}")
