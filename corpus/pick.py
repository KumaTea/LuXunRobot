import os
import json


config_file = 'corpus.json'


def get_articles():
    books = os.listdir()
    articles = []
    for book in books:
        if '.' not in book:
            articles.append([f'{book}/{article}' for article in os.listdir(book) if 'txt' in article])
    return articles


def pick_articles():
    config = []
    articles = get_articles()
    for book in articles:
        for article in book:
            with open(article, 'r', encoding='utf-8') as f:
                text = f.read()
            print(os.path.basename(article))
            print(text)
            print(f'\n\n\n\n{os.path.basename(article)}\n')
            decision = input('Accept? [Y/n]') or 'Y'

            config.append({
                'path': article,
                'pick': decision.upper() != 'N'
            })

    with open(config_file, 'w', encoding='utf-8') as f:
        json.dump(config, f)

    return True


if __name__ == '__main__':
    pick_articles()
