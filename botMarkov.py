import markovify


def gen_model(file='split.txt'):
    with open(file, encoding='utf-8') as f:
        model = markovify.Text(f, retain_original=False)
    return model


def gen_sentences(model, num=1):
    if num == 1:
        return model.make_sentence().replace(' ', '')
    else:
        sen = ''
        for i in range(num):
            sen += model.make_sentence().replace(' ', '') + '\n\n'
        return sen[:-2]


def gen_length(model, minimum=25, maximum=70):
    sen = ''
    while len(sen) < minimum:
        sen += model.make_sentence().replace(' ', '') + '\n\n'
        if len(sen) > maximum:
            sen = ''
    return sen[:-2]
