from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
from config import BOT_TOKEN
from commands import admin, games, bank, interaction, auto_messages

app = ApplicationBuilder().token(BOT_TOKEN).build()

# إضافة أوامر الإدارة
app.add_handler(CommandHandler("رفع", admin.raise_rank))
app.add_handler(CommandHandler("تنزيل", admin.lower_rank))
# باقي أوامر الإدارة حسب الملفات

# إضافة الألعاب
app.add_handler(CommandHandler("روليت", games.roulette))
app.add_handler(CommandHandler("صور", games.photo_game))
# باقي الألعاب

# الردود والتفاعل
app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), interaction.handle_messages))

# الرسائل التلقائية
auto_messages.schedule_messages(app)

# تشغيل البوت
if __name__ == "__main__":
    print("البوت شغال 🔥")
    app.run_polling()
