# bot.py
import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters
from config import TOKEN, OWNER_ID, GROUP_IDS, BANK_DEFAULT, ADMIN_BANK, OWNER_BANK

# ----- بيانات البنك -----
user_balances = {}

async def bank_game(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    balance = user_balances.get(user_id, BANK_DEFAULT)
    await update.message.reply_text(f"رصيدك الحالي: {balance} 💰")

# ----- أوامر الإدارة -----
class AdminCommands:
    @staticmethod
    async def raise_rank(update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text("تم رفع الرتبة ✅")

    @staticmethod
    async def lower_rank(update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text("تم تنزيل الرتبة ✅")

    @staticmethod
    async def clear_rank(update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text("تم مسح الرتبة ✅")

    @staticmethod
    async def ban(update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text("تم حظر العضو ❌")

    @staticmethod
    async def mute(update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text("تم كتم العضو 🔇")

admin = AdminCommands()

# ----- معالجة الرسائل بالعربية -----
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if text == "/رصيد":
        await bank_game(update, context)
    elif text == "/رفع":
        await admin.raise_rank(update, context)
    elif text == "/تنزيل":
        await admin.lower_rank(update, context)
    elif text == "/مسح":
        await admin.clear_rank(update, context)
    elif text == "/حظر":
        await admin.ban(update, context)
    elif text == "/كتم":
        await admin.mute(update, context)
    else:
        await update.message.reply_text("أمر غير معروف ❌")

# ----- تشغيل البوت -----
async def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    # تعيين MessageHandler لجميع الرسائل
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("البوت شغّال الآن 🟢")
    await app.start()
    await app.updater.start_polling()
    await app.updater.idle()

if __name__ == "__main__":
    asyncio.run(main())
