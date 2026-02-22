from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from commands import admin, games, bank, interaction, auto_messages
from config import TOKEN  # تأكد إنه عندك TOKEN في config.py

app = ApplicationBuilder().token(TOKEN).build()

# =========================
# أوامر إدارية
# =========================
app.add_handler(CommandHandler("raise", admin.raise_rank))   # رفع رتبة
app.add_handler(CommandHandler("ban", admin.ban_user))       # حظر مستخدم
app.add_handler(CommandHandler("unban", admin.unban_user))   # فك حظر

# =========================
# أوامر اللعبة
# =========================
app.add_handler(CommandHandler("bank", bank.bank_game))      # رصيدك
app.add_handler(CommandHandler("play", games.start_game))   # بدء اللعبة

# =========================
# رسائل تفاعلية
# =========================
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, interaction.handle_message))

# =========================
# رسائل تلقائية
# =========================
app.add_handler(CommandHandler("auto", auto_messages.send_auto_messages))

# =========================
# تشغيل البوت
# =========================
print("Bot is running...")
app.run_polling()
