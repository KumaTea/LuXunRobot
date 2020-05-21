import botCache
from botSession import scheduler, logger
from botRegister import start_cron, handlers


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
    handlers()
    logger.info('Initialized. Starting scheduler...')
    scheduler.start()
