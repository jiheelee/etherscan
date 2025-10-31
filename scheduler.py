from apscheduler.schedulers.blocking import BlockingScheduler
from main import run_job

def start_scheduler():
    scheduler = BlockingScheduler()
    scheduler.add_job(run_job, "interval", hours=1)
    scheduler.start()
