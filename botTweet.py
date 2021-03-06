import botCache
from botInfo import twi_id
from botMarkov import gen_length
from botDB import images, blacklist
from botWallpaper import send_wallpaper
from botSession import lx_twi, lx_model, logger


def tweet(desired=None):
    if desired:
        sen = desired
    else:
        if botCache.sentences:
            sen = botCache.sentences.pop()
        else:
            sen = gen_length(lx_model, 100, 140)
    result = lx_twi.update_status(sen)
    logger.info(f'Generated: {result.text}\n\n')
    return True


def morning():
    logger.info(f'Sending morning greeting...')
    return send_wallpaper()


def night():
    logger.info(f'Sending night greeting...')
    return lx_twi.update_status('呐，晚安。', media_ids=[images['greet']['night']['id']])


def process_mention():
    tl = lx_twi.mentions_timeline()
    task = []
    if botCache.latest_mention:
        for item in tl:
            if item.id == botCache.latest_mention:
                break
            else:
                task.append(item)
        if task:
            for item in task:
                mention(item)
            botCache.latest_mention = task[0].id
            with open('mention.log', 'w') as log:
                log.write(str(botCache.latest_mention))
            return True
        return None
    else:
        botCache.latest_mention = tl[0].id
        return None


def mention(mentioned_tweet):
    keywords = ['say', 'speak', 'generate', '说', '生成', '讲', '言', '批', '，骂']
    delete = ['del', '删']
    if mentioned_tweet.author.id in blacklist:
        return False
    for item in keywords:
        if item in mentioned_tweet.text.lower():
            sen = gen_length(lx_model, 20, 140)
            result = lx_twi.update_status(sen, in_reply_to_status_id=mentioned_tweet.id, auto_populate_reply_metadata=True)
            logger.info(f'Generated: {result.text}\n\n')
            return True
    for item in delete:
        if item in mentioned_tweet.text.lower():
            if mentioned_tweet.in_reply_to_status_id:
                my_tweet = lx_twi.get_status(mentioned_tweet.in_reply_to_status_id)
                if my_tweet.author.id == twi_id and my_tweet.in_reply_to_status_id:
                    source_tweet = lx_twi.get_status(my_tweet.in_reply_to_status_id)
                    if source_tweet.author.id == mentioned_tweet.author.id:
                        lx_twi.destroy_status(my_tweet.id)
                        logger.warn(f'Deleted: {my_tweet.id}')
    return None
