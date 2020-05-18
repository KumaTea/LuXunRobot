from botMarkov import gen_length
from botSession import lx, lx_model


def tweet():
    sen = gen_length(lx_model)
    result = lx.update_status(sen)
    print(f'Generated: {result.text}')
    return True
