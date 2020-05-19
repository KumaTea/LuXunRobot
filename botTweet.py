import botCache
from botInfo import me
from botMarkov import gen_length
from botSession import lx, lx_model
from botDB import images, blacklist


def tweet():
    sen = gen_length(lx_model, 100, 140)
    result = lx.update_status(sen)
    print(f'Generated: {result.text}\n\n')
    return True


def morning():
    return lx.update_status('呐，早安。', media_ids=[images['greet']['morning']['id']])


def night():
    return lx.update_status('呐，晚安。', media_ids=[images['greet']['night']['id']])


def process_mention():
    tl = lx.mentions_timeline()
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
            result = lx.update_status(sen, in_reply_to_status_id=mentioned_tweet.id, auto_populate_reply_metadata=True)
            print(f'Generated: {result.text}\n\n')
            return True
    for item in delete:
        if item in mentioned_tweet.text.lower():
            if mentioned_tweet.in_reply_to_status_id:
                my_tweet = lx.get_status(mentioned_tweet.in_reply_to_status_id)
                if my_tweet.author.id == me and my_tweet.in_reply_to_status_id:
                    source_tweet = lx.get_status(my_tweet.in_reply_to_status_id)
                    if source_tweet.author.id == mentioned_tweet.author.id:
                        lx.destroy_status(my_tweet.id)
                        print(f'Deleted: {my_tweet.id}')
    return None
