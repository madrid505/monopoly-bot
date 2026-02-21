import schedule, threading, time
from config import GROUP_IDS

def schedule_messages(app):
    def send_adhkar():
        for gid in GROUP_IDS:
            app.bot.send_message(chat_id=gid, text="اذكار 💫")

    def send_azkar_and_hikam():
        for gid in GROUP_IDS:
            app.bot.send_message(chat_id=gid, text="حكم وأدعية 📿")

    schedule.every(15).minutes.do(send_adhkar)
    schedule.every(15).minutes.do(send_azkar_and_hikam)

    def run_scheduler():
        while True:
            schedule.run_pending()
            time.sleep(1)

    thread = threading.Thread(target=run_scheduler)
    thread.start()
