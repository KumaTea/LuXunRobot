import botCache
from botRead import read
from botInfo import tg_id
from botDB import tg_start
from botMarkov import gen_length
from botSession import lx_tg, lx_model


def can_delete(chat_id):
    if chat_id in botCache.delete_privilege:
        return botCache.delete_privilege[chat_id]
    else:
        delete_status = lx_tg.get_chat_member(chat_id, tg_id).can_delete_messages
        botCache.delete_privilege[chat_id] = delete_status
        return delete_status


def start(update, context):
    message = update.message
    return message.reply_text(tg_start)


def say(update, context):
    message = update.message
    chat_id = message.chat_id
    message_id = message.message_id
    reply_info = message.reply_to_message
    text = message.text
    command = False

    if text and text.startswith('/'):
        command = True
    if command and can_delete(chat_id):
        lx_tg.delete_message(chat_id, message_id)

    if botCache.sentences:
        sen = botCache.sentences.pop()
    else:
        sen = gen_length(lx_model, 20, 140)

    if reply_info:
        if reply_info.from_user.id == tg_id and not command:
            return message.reply_text(sen)
        else:
            # is command
            return lx_tg.send_message(chat_id, sen, reply_to_message_id=reply_info.message_id)
    else:
        return message.reply_text(sen, quote=False)


def new(update, context):
    message = update.message
    reply_to_message = message.reply_to_message
    if reply_to_message.from_user.id != tg_id:
        return False
    chat_id = message.chat_id
    message_id = message.message_id
    # user_id = message.from_user.id
    command = True

    if command and can_delete(chat_id):
        lx_tg.delete_message(chat_id, message_id)

    if botCache.sentences:
        sen = botCache.sentences.pop()
    else:
        sen = gen_length(lx_model, 20, 140)
    return lx_tg.edit_message_text(sen, chat_id, reply_to_message.message_id)


def luxun(update, context):
    message = update.message
    chat_id = message.chat_id
    message_id = message.message_id
    reply_info = message.reply_to_message
    text = message.text
    command = False

    if text and text.startswith('/'):
        command = True
    if command and can_delete(chat_id):
        lx_tg.delete_message(chat_id, message_id)

    sen = read()

    if reply_info:
        if reply_info.from_user.id == tg_id and not command:
            return message.reply_text(sen)
        else:
            # is command
            return lx_tg.send_message(chat_id, sen, reply_to_message_id=reply_info.message_id)
    else:
        return message.reply_text(sen, quote=False)
