from botDB import corpus
from random import choice


def read(minimum=20, maximum=200):
    book = choice(corpus)
    with open(f'corpus/{book}', 'r', encoding='utf-8') as f:
        content = f.read()
    content = content.splitlines()
    text = ''
    while len(text) < minimum:
        text += choice(content) + '\n\n'
        if len(text) > maximum:
            text = ''
    return text[:-2]
