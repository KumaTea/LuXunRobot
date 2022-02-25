import os
import json
from localRules import escape_word

train_file = 'train.json'
min_length = 20


def get_articles():
    books = os.listdir()
    articles = []
    for book in books:
        if '.' not in book:
            articles.append([f'{book}/{article}' for article in os.listdir(book) if 'txt' in article])
    return articles


def pick_articles():
    train_data = []
    articles = get_articles()
    for book in articles:
        book_content = ''
        for article in book:
            with open(article, 'r', encoding='utf-8', errors='ignore') as f:
                text = f.read()
            lines = text.splitlines()
            if '年' in lines[-1] and '月' in lines[-1]:
                lines = lines[:-1]
            text = ''
            for line in lines:
                if len(line) > min_length and escape_word not in line:
                    text += line + '\n'
            book_content += text
        if bc := book_content[:-1]:
            train_data.append(bc)

    with open(train_file, 'w', encoding='utf-8') as f:
        json.dump(train_data, f)
    return True


if __name__ == '__main__':
    pick_articles()
