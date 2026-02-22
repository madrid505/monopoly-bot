from telegram import Update, ChatPermissions
from telegram.ext import ContextTypes

async def raise_rank(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ تم رفع الرتبة")

async def lower_rank(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("⬇️ تم تنزيل الرتبة")

async def clear_rank(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🗑️ تم مسح الرتبة")

async def ban_user(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message.reply_to_message:
        await update.message.reply_text("❌ لازم ترد على الشخص اللي بدك تحظره")
        return

    user_id = update.message.reply_to_message.from_user.id
    chat_id = update.effective_chat.id

    try:
        await context.bot.ban_chat_member(chat_id, user_id)
        await update.message.reply_text("🚫 تم حظر العضو")
    except Exception as e:
        await update.message.reply_text(f"❌ خطأ: {e}")

async def mute_user(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message.reply_to_message:
        await update.message.reply_text("❌ لازم ترد على الشخص اللي بدك تكتمه")
        return

    user_id = update.message.reply_to_message.from_user.id
    chat_id = update.effective_chat.id

    try:
        permissions = ChatPermissions(can_send_messages=False)
        await context.bot.restrict_chat_member(chat_id, user_id, permissions)
        await update.message.reply_text("🔇 تم كتم العضو")
    except Exception as e:
        await update.message.reply_text(f"❌ خطأ: {e}")
