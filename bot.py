# bot.py
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from config import TOKEN, OWNER_ID, BANK_DEFAULT, ADMIN_BANK, OWNER_BANK

# تهيئة سجل الأحداث
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# قاعدة البيانات البسيطة للرصيد
balances = {}

# أمر الرصيد
async def bank_game(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if user_id == OWNER_ID:
        balances[user_id] = OWNER_BANK
    elif user_id in [OWNER_ID]:  # هنا يمكن إضافة IDs للمدراء والمشرفين
        balances[user_id] = ADMIN_BANK
    else:
        if user_id not in balances:
            balances[user_id] = BANK_DEFAULT
    await update.message.reply_text(f"رصيدك الحالي: {balances[user_id]} 💰")

# أمر رفع الرتبة (للمدير أو المالك)
async def raise_rank(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if user_id != OWNER_ID:
        await update.message.reply_text("❌ ليس لديك صلاحية تنفيذ هذا الأمر")
        return
    if len(context.args) < 2:
        await update.message.reply_text("استخدام: /رفع <user_id> <المبلغ>")
        return
    try:
        target_id = int(context.args[0])
        amount = int(context.args[1])
        balances[target_id] = balances.get(target_id, BANK_DEFAULT) + amount
        await update.message.reply_text(f"✅ تم إضافة {amount} إلى رصيد {target_id}")
    except ValueError:
        await update.message.reply_text("❌ المعرف أو المبلغ غير صحيح")

# بدء البوت
if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()

    # إضافة أوامر
    app.add_handler(CommandHandler("رصيد", bank_game))
    app.add_handler(CommandHandler("رفع", raise_rank))

    print("🚀 البوت شغال الآن...")
    app.run_polling()
