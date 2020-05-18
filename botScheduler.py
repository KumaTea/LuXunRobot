from botSession import scheduler
from botTweet import tweet, morning, night


def start():
    scheduler.add_job(tweet, 'cron', hour='8-23,0-2', minute='*/30')
    scheduler.add_job(morning, 'cron', hour=7, minute=30)
    scheduler.add_job(night, 'cron', hour=2, minute=30)
