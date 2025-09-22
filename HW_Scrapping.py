import requests
import re

from bs4 import BeautifulSoup

url = 'https://habr.com/ru/articles/'
KEYWORDS = ['дизайн', 'фото', 'web', 'python', 'linux', 'ии']

r = requests.get(url)

soup = BeautifulSoup(r.text, 'lxml')
findon_all = soup.find_all('a', class_='tm-title__link')
# find_a_by_text = soup.find('a', string=re.compile(''))

for i in findon_all:
    if set(KEYWORDS) & set(i.text.lower().split()):
        print(i.text, 'https://habr.com' + i.get('href'))


