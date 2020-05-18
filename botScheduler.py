from botTweet import tweet
from botSession import scheduler


def start():
    scheduler.add_job(tweet, 'cron', minute='*/30')
