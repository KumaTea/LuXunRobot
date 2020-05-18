from botMarkov import gen_length
from botSession import lx, lx_model


def tweet():
    sen = gen_length(lx_model)
    return lx.update_status(sen)
