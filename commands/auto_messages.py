import schedule, time
from telegram.ext import ApplicationBuilder

def schedule_messages(app: ApplicationBuilder):
    # مثال: نشر اذكار كل ربع ساعة
    def send_adhkar():
        for group_id in [ -1002695848824, -1003721123319, -1002052564369 ]:
            app.bot.send_message(chat_id=group_id, text="اذكار 💫")
    schedule.every(15).minutes.do(send_adhkar)
