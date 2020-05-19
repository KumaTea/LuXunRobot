from botDB import images
from botMarkov import gen_length
from botSession import lx, lx_model


def tweet():
    sen = gen_length(lx_model, 100, 140)
    result = lx.update_status(sen)
    print(f'Generated: {result.text}\n\n')
    return True


def morning():
    return lx.update_status('呐，早安。', media_ids=[images['greet']['morning']['id']])


def night():
    return lx.update_status('呐，晚安。', media_ids=[images['greet']['night']['id']])
