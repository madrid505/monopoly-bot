import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from config import BOT_TOKEN, OWNER_ID, BANK_DEFAULT, ADMIN_BANK, OWNER_BANK
from commands import admin, games, bank, interaction, auto_messages

# إعداد logging لملف bot.log
logging.basicConfig(
    filename='bot.log',
    filemode='a',  # يضيف في الملف بدل ما يمسح القديم
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

balances = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logging.info(f"/start triggered by user {update.effective_user.id}")
    await update.message.reply_text("مرحباً! البوت شغال.")

# مثال على اللعبة البنكية
async def bank_game(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        user_id = update.effective_user.id
        if user_id == OWNER_ID:
            balances[user_id] = OWNER_BANK
        elif user_id in []:  # ضع هنا IDs المدراء والمشرفين
            balances[user_id] = ADMIN_BANK
        else:
            balances[user_id] = BANK_DEFAULT
        await update.message.reply_text(f"رصيدك الحالي: {balances[user_id]}")
        logging.info(f"User {user_id} balance: {balances[user_id]}")
    except Exception as e:
        logging.error(f"Error in bank_game: {e}")

async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logging.warning(f"Unknown command from user {update.effective_user.id}: {update.message.text}")
    await update.message.reply_text("آسف، لا أفهم هذا الأمر.")

def main():
    try:
        app = ApplicationBuilder().token(BOT_TOKEN).build()

        # تسجيل الأوامر
        app.add_handler(CommandHandler("start", start))
        app.add_handler(CommandHandler("bank", bank_game))
        app.add_handler(MessageHandler(filters.COMMAND, unknown))

        logging.info("Bot started successfully")
        app.run_polling()
    except Exception as e:
        logging.critical(f"Bot failed to start: {e}")

if __name__ == "__main__":
    main()
