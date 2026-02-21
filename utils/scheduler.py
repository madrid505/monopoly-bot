import schedule, threading, time

def start_schedule(job_func, interval_minutes):
    schedule.every(interval_minutes).minutes.do(job_func)
    def run():
        while True:
            schedule.run_pending()
            time.sleep(1)
    threading.Thread(target=run).start()
