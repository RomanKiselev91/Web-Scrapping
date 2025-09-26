

import requests
import re
from bs4 import BeautifulSoup

url = 'https://habr.com/ru/articles/'

KEYWORDS = ['дизайн', 'фото', 'web', 'python', 'ИИ', 'Valve', 'галлюцинации', 'функции']
r = requests.get(url)

soup = BeautifulSoup(r.text, 'lxml')

findon_title = soup.find_all('div', class_='article-formatted-body article-formatted-body article-formatted-body_version-2')
findon_title1 = soup.find_all('article', class_='tm-articles-list__item')

for i in findon_title1:
    # title = ''i.find(class_='article-formatted-body article-formatted-body article-formatted-body_version-2').text''
    # if set(KEYWORDS) & set(i.find('div', class_='article-formatted-body article-formatted-body article-formatted-body_version-2').text.lower().split()):
    #     print(i.find('time').attrs['title'], i.find('a', class_='tm-title__link').text, 'https://habr.com' + i.find('a', class_='tm-title__link').get('href'))
    print(i.find('div', class_='article-formatted-body article-formatted-body article-formatted-body_version-2'))
    # print(i)
    # for y in i:
    #     print(y.find())
# print(findon_title)