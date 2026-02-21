from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from config import BOT_TOKEN
from commands import admin, games, bank, interaction, auto_messages

app = ApplicationBuilder().token(BOT_TOKEN).build()

# إدارة
app.add_handler(CommandHandler("رفع", admin.raise_rank))
app.add_handler(CommandHandler("تنزيل", admin.lower_rank))
app.add_handler(CommandHandler("مسح", admin.clear_rank))
app.add_handler(CommandHandler("حظر", admin.ban))
app.add_handler(CommandHandler("كتم", admin.mute))
# باقي أوامر الإدارة مشابهة

# الألعاب
app.add_handler(CommandHandler("روليت", games.roulette))
app.add_handler(CommandHandler("صور", games.photo_game))
app.add_handler(CommandHandler("تحدي", games.challenges))
app.add_handler(CommandHandler("حظ", games.luck_game))
app.add_handler(CommandHandler("بنك", bank.bank_game))
# باقي الألعاب حسب الملفات

# التفاعل والردود
app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), interaction.handle_messages))

# الرسائل التلقائية
auto_messages.schedule_messages(app)

# تشغيل البوت
if __name__ == "__main__":
    print("البوت شغال 🔥")
    app.run_polling()
