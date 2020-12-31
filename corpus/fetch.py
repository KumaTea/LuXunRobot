import os
import requests
from bs4 import BeautifulSoup


corpus_source = 'https://www.marxists.org'
path = 'chinese/reference-books/luxun'
index_page = '000.htm'
books_count = 24
books_links = []
for book in range(books_count):
    books_links.append(f'{corpus_source}/{path}/{book+1:02d}/{index_page}')


def fetch_book(url):
    url_root = os.path.dirname(url)  # https://www.marxists.org/chinese/reference-books/luxun/01
    url_content = requests.get(url)
    url_content.encoding = url_content.apparent_encoding  # GB2312
    url_code = url_content.text
    soup = BeautifulSoup(url_code, features='lxml')
    title = soup.find('title').text
    print(f'Fetching book: {title}, {url}')
    try:
        os.mkdir(title)
    except FileExistsError:
        pass

    articles = [{'name': article.text, 'url': url_root + '/' + article['href']}
                for article in soup.find_all('table')[1].find_all('a')]
    article_index = 1

    for article in articles:
        print(f'    Fetching article: {article["name"]}')
        article_content = requests.get(article['url'])
        article_content.encoding = article_content.apparent_encoding  # GB2312
        article_code = article_content.text
        soup = BeautifulSoup(article_code, features='lxml')

        finder = []
        finder.extend(soup.find_all('p'))
        finder.extend(soup.find_all('td'))
        article_text = str(max([item.text for item in finder], key=len))
        article_text = '\n'.join([paragraph for paragraph in article_text.split('\n') if len(paragraph) > 10])

        with open(f'{title}/{article_index:02d}_{article["name"]}.txt', 'w', encoding='utf-8') as file:
            file.write(article_text)

        article_index += 1

    return True


if __name__ == '__main__':
    for link in books_links:
        fetch_book(link)
