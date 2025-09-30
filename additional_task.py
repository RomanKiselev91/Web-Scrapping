import requests
from bs4 import BeautifulSoup

headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36",
           "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
           "accept-language": "en-RU,en;q=0.9",
           "sec-fetch-site": "same-origin",
           }

KEYWORDS = ['дизайн', 'фото', 'web', 'python', 'linux', 'ии', 'maintenance', 'суперсила', 'межзвёздные']

url = 'https://habr.com/ru/articles/'

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.text, 'lxml')
article_all = soup.find_all('article', class_='tm-articles-list__item')


for i in article_all:
    # print(i.attrs['id'])
    url_article = f'https://habr.com/ru/articles/{i.attrs['id']}'
    r = requests.get(url_article, headers=headers)
    soup = BeautifulSoup(r.text, 'lxml')
    text_article = soup.find('div', class_='article-formatted-body article-formatted-body article-formatted-body_version-2').find_all('p')
    if set(KEYWORDS) & set(i.find('div', class_='article-formatted-body article-formatted-body article-formatted-body_version-2').text.lower().split()):
        print(i.find('time').attrs['title'], i.find('a', class_='tm-title__link').text,
              'https://habr.com' + i.find('a', class_='tm-title__link').get('href'))
    


