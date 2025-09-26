import requests
import re

from bs4 import BeautifulSoup

url = 'https://habr.com/ru/articles/'
KEYWORDS = ['дизайн', 'фото', 'web', 'python', 'linux', 'ии', 'space','путеводитель', 'вспышка']

r = requests.get(url)

soup = BeautifulSoup(r.text, 'lxml')
findon_title = soup.find_all('article', class_='tm-articles-list__item')


for title in findon_title:
    if set(KEYWORDS) & set(title.find('a', class_='tm-title__link').text.lower().split()):
        print(title.find('time').attrs['title'], title.find('a', class_='tm-title__link').text,
            'https://habr.com' + title.find('a', class_='tm-title__link').get('href'))
