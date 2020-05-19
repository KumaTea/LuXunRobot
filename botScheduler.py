from botSession import scheduler
from botTweet import tweet, morning, night, process_mention


def start_cron():
    scheduler.add_job(tweet, 'cron', hour='0,2,8,10,12,14,16,18,20,22', minute=0)
    # scheduler.add_job(tweet, 'cron', hour=2, minute=0)
    scheduler.add_job(morning, 'cron', hour=7, minute=30)
    scheduler.add_job(night, 'cron', hour=2, minute=30)
    scheduler.add_job(process_mention, 'cron', minute='*')
