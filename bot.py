# bot.py
import os, random, asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from config import TOKEN, OWNER_ID, ADMINS, BANK_DEFAULT, ADMIN_BANK, OWNER_BANK, ROLLET_DEFAULT_BET, IMAGE_GAME_PATH, AUTO_MESSAGES

# =====================
# بيانات البنك
balances = {}

# =====================
# أوامر البنك
async def bank_game(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if user_id == OWNER_ID:
        balances[user_id] = OWNER_BANK
    elif user_id in ADMINS:
        balances[user_id] = ADMIN_BANK
    else:
        balances[user_id] = balances.get(user_id, BANK_DEFAULT)
    await update.message.reply_text(f"رصيدك الحالي: {balances[user_id]}")

# =====================
# أمر رفع الرتب
async def raise_rank(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if user_id != OWNER_ID:
        await update.message.reply_text("فقط صاحب البوت يمكنه رفع الرتب!")
        return
    # مثال: إضافة معرف جديد للمدراء
    try:
        new_admin = int(context.args[0])
        if new_admin not in ADMINS:
            ADMINS.append(new_admin)
            await update.message.reply_text(f"تم رفع رتبة المستخدم {new_admin} إلى مشرف.")
        else:
            await update.message.reply_text("هذا المستخدم مشرف بالفعل.")
    except:
        await update.message.reply_text("استخدم: /رفع <معرف المستخدم>")

# =====================
# رسالة ترحيب
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"مرحبا {update.effective_user.first_name}!\nاستخدم /bank لمعرفة رصيدك.")

# =====================
# لعبة الروليت
async def roulette(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if user_id not in balances:
        balances[user_id] = BANK_DEFAULT
    bet = int(context.args[0]) if context.args else ROLLET_DEFAULT_BET
    if bet > balances[user_id]:
        await update.message.reply_text("رصيدك لا يكفي للمراهنة.")
        return
    outcome = random.choice(["win", "lose"])
    if outcome == "win":
        balances[user_id] += bet
        await update.message.reply_text(f"مبروك! ربحت {bet} رصيد 🎉\nرصيدك الحالي: {balances[user_id]}")
    else:
        balances[user_id] -= bet
        await update.message.reply_text(f"خسرت {bet} رصيد 😢\nرصيدك الحالي: {balances[user_id]}")

# =====================
# لعبة الصور
async def image_game(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not os.path.exists(IMAGE_GAME_PATH):
        await update.message.reply_text("مجلد الصور غير موجود.")
        return
    images = os.listdir(IMAGE_GAME_PATH)
    if not images:
        await update.message.reply_text("لا توجد صور للعبة حالياً.")
        return
    chosen_image = random.choice(images)
    await update.message.reply_photo(open(os.path.join(IMAGE_GAME_PATH, chosen_image), "rb"))

# =====================
# الرسائل التلقائية
async def auto_messages_task(app):
    while True:
        for msg in AUTO_MESSAGES:
            for chat_id in balances.keys():
                try:
                    await app.bot.send_message(chat_id=chat_id, text=msg)
                except:
                    pass
            await asyncio.sleep(3600)  # كل ساعة
        await asyncio.sleep(3600)

# =====================
# حماية البوت
async def filter_messages(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()
    if any(word in text for word in ["سب", "كفر", "اباحي"]):
        await update.message.delete()
        await update.message.reply_text("🚫 ممنوع هذا الكلام!")

    if "http" in text and update.effective_user.id not in ADMINS + [OWNER_ID]:
        await update.message.delete()
        await update.message.reply_text("🚫 ممنوع نشر الروابط!")

# =====================
# تشغيل البوت
app = ApplicationBuilder().token(TOKEN).build()

# تسجيل الأوامر
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("bank", bank_game))
app.add_handler(CommandHandler("رفع", raise_rank))
app.add_handler(CommandHandler("روليت", roulette))
app.add_handler(CommandHandler("صور", image_game))
app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), filter_messages))

# تشغيل الرسائل التلقائية
asyncio.create_task(auto_messages_task(app))

# تشغيل البوت
print("البوت شغال الآن...")
app.run_polling()
