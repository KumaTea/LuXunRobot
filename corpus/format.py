import os
import re
import unicodedata
from pick import get_articles


space_before_paragraph = '\u3000'
remove_characters = ['·', '・']


def format_article(file):
    with open(file, 'r', encoding='utf-8') as f:
        text = f.read()
    text += '\n'

    text = text.replace(space_before_paragraph, '')
    for character in remove_characters:
        text = text.replace(character, '')
    text = text.replace(
        f'{os.path.basename(file)[os.path.basename(file).find("_")+1:os.path.basename(file).find(".")]}\n', '')

    text = re.sub(r'^〔.+\n', '', text, flags=re.MULTILINE)
    text = re.sub(r'〔.{1,3}〕', '', text)

    text = unicodedata.normalize('NFKC', text)

    text = text.replace('\n\n', '\n')

    with open(file, 'w', encoding='utf-8') as f:
        f.write(text)
    return print('Done:', file)


if __name__ == '__main__':
    articles = get_articles()
    for book in articles:
        for article in book:
            format_article(article)
