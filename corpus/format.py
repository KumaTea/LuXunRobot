import os
import re
import unicodedata
from pick import get_articles


space_before_paragraph = '\u3000'
remove_characters = ['·', '・', '※']


def is_word(char):
    cp = ord(char)
    if 0x00 <= cp <= 0x7F:
        return True
    return False


def is_chinese(char):
    cp = ord(char)
    if 0x4E00 <= cp <= 0x9FFF or 0x3000 <= cp <= 0x33FF\
            or 0xFF00 <= cp <= 0xFFEF or 0x2000 <= cp <= 0x20FF\
            or cp == 0x25CB:  # ○
        return True
    return False


def format_article(file):
    with open(file, 'r', encoding='utf-8') as f:
        text = f.read()
    text += '\n'

    text = text.replace(space_before_paragraph, '')
    for character in remove_characters:
        text.replace(character, '')

    for character in text:
        if not (is_chinese(character) or is_word(character)):
            text = text.replace(character, '')
            print('Remove:', character)
    text = text.replace(
        f'{os.path.basename(file)[os.path.basename(file).find("_")+1:os.path.basename(file).find(".")]}\n', '')

    text = re.sub(r'^〔.+\n', '', text, flags=re.MULTILINE)
    text = re.sub(r'〔.{1,3}〕', '', text)

    text = unicodedata.normalize('NFKC', text)

    while '\n\n' in text:
        text = text.replace('\n\n', '\n')

    with open(file, 'w', encoding='utf-8') as f:
        f.write(text)
    return print('Done:', file)


if __name__ == '__main__':
    articles = get_articles()
    for book in articles:
        for article in book:
            print(f'Processing: {article}')
            format_article(article)
