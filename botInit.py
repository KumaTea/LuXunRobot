import botCache
from botSession import scheduler
from botScheduler import start_cron


def read_mention():
    with open('mention.log', 'r') as log:
        botCache.latest_mention = int(log.read())
    return botCache.latest_mention


def initialize():
    try:
        read_mention()
    except:
        pass
    start_cron()
    print('Initialized. Starting scheduler...')
    scheduler.start()
