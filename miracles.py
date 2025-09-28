

import requests
import re
from bs4 import BeautifulSoup

url = 'https://habr.com/ru/articles/'

KEYWORDS = ['дизайн', 'фото', 'web', 'python', 'ИИ', 'Valve', 'галлюцинации', 'функции', 'разработчик', 'программирование', 'язык', 'selenium' ]
headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36",
           "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
           "accept-language": "en-RU,en;q=0.9",
           "sec-fetch-site": "same-origin",
           }
r = requests.get(url, headers=headers)

soup = BeautifulSoup(r.text, 'lxml')


findon_title1 = soup.find_all('article', class_='tm-articles-list__item')

for i in findon_title1:
    if set(KEYWORDS) & set(i.find('div', class_='article-formatted-body article-formatted-body article-formatted-body_version-2').text.lower().split()):
        print(i.find('time').attrs['title'], i.find('a', class_='tm-title__link').text, 'https://habr.com' + i.find('a', class_='tm-title__link').get('href'))
