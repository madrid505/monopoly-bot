# bot.py
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
from config import BOT_TOKEN, OWNER_ID, GROUP_IDS, BANK_DEFAULT, ADMIN_BANK, OWNER_BANK

# 🏦 بيانات الرصيد لكل مستخدم
user_balance = {}

# ------------------- وظائف البنك -------------------
async def balance(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    balance = user_balance.get(user_id, BANK_DEFAULT)
    await update.message.reply_text(f"رصيدك الحالي: {balance} 💰")

async def gift(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) != 2:
        await update.message.reply_text("استخدام: /gift <user_id> <amount>")
        return
    try:
        target_id = int(context.args[0])
        amount = int(context.args[1])
    except ValueError:
        await update.message.reply_text("الرجاء إدخال أرقام صحيحة.")
        return
    sender_id = update.effective_user.id
    sender_balance = user_balance.get(sender_id, BANK_DEFAULT)
    if sender_balance < amount:
        await update.message.reply_text("ليس لديك رصيد كافي لإرسال هذه الهديه.")
        return
    user_balance[sender_id] = sender_balance - amount
    user_balance[target_id] = user_balance.get(target_id, BANK_DEFAULT) + amount
    await update.message.reply_text(f"تم إرسال {amount} 💰 للمستخدم {target_id}.")

# ------------------- أوامر الإدارة -------------------
async def raise_rank(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("تم رفع الرتبة 🔼")

async def lower_rank(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("تم تنزيل الرتبة 🔽")

async def clear_rank(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("تم مسح الرتبة 🧹")

async def ban_user(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("تم حظر المستخدم ⛔")

async def mute_user(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("تم كتم المستخدم 🔇")

# ------------------- أوامر الألعاب -------------------
async def roll_dice(update: Update, context: ContextTypes.DEFAULT_TYPE):
    import random
    dice = random.randint(1, 6)
    await update.message.reply_text(f"نتيجة الزهر 🎲: {dice}")

# ------------------- تهيئة البوت -------------------
app = ApplicationBuilder().token(BOT_TOKEN).build()

# أوامر البنك
app.add_handler(CommandHandler("balance", balance))
app.add_handler(CommandHandler("gift", gift))

# أوامر الإدارة
app.add_handler(CommandHandler("raise", raise_rank))
app.add_handler(CommandHandler("lower", lower_rank))
app.add_handler(CommandHandler("clear", clear_rank))
app.add_handler(CommandHandler("ban", ban_user))
app.add_handler(CommandHandler("mute", mute_user))

# أوامر الألعاب
app.add_handler(CommandHandler("roll", roll_dice))

# ردود عربية على الأوامر بالإنجليزية
async def unknown_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("أمر غير معروف ❌")

app.add_handler(MessageHandler(filters.COMMAND, unknown_command))

# ------------------- تشغيل البوت -------------------
print("البوت شغال الآن ✅")
app.run_polling()
