from botTelegram import *
from botSession import dp, scheduler
from botTweet import tweet, morning, night, process_mention
from telegram.ext import MessageHandler, CommandHandler, Filters


def start_cron():
    scheduler.add_job(tweet, 'cron', hour='0,2,8,10,12,14,16,18,20,22', minute=0)
    # scheduler.add_job(tweet, 'cron', hour=2, minute=0)
    scheduler.add_job(morning, 'cron', hour=7, minute=30)
    scheduler.add_job(night, 'cron', hour=2, minute=30)
    scheduler.add_job(process_mention, 'cron', minute='*/10')


def handlers():
    dp.add_handler(CommandHandler(['say', 'speak', 'generate'], say))
    dp.add_handler(CommandHandler(['read', 'origin', 'luxun'], luxun))
    dp.add_handler(CommandHandler(['start'], start, filters=Filters.private))
    dp.add_handler(CommandHandler(['new', 'ano', 'change'], new))
    dp.add_handler(MessageHandler((~ Filters.command), say))
