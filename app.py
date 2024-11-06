import requests
import json
from bs4 import BeautifulSoup

url = 'https://quotes.toscrape.com/page'
number_page, li_next = 1, True
list_quotes = []
while li_next:
    url_number = url + f'/{number_page}/'
    response = requests.get(url_number)
    if response.status_code == 200:
        print(f'Работа с {url_number}')
        soup = BeautifulSoup(response.text, 'lxml')
        quotes = soup.find_all('span', class_='text')
        authors = soup.find_all('small', class_='author')
        tags = soup.find_all('div', class_='tags')

        for i in range(len(quotes)):
            tags_for_quote = tags[i].find_all('a', class_='tag')

            list_quotes.append({
                'quote': quotes[i].text[1:-2],
                'author': authors[i].text,
                'tags': [tag.text for tag in tags_for_quote]
            })

        if soup.find('li', class_='next') == None:
            li_next = False
        else:
            number_page += 1
    else:
        print(f'Ошибка соединения со страницей {url_number}')
print('Процесс сохранения данных в JSON')
title_file = 'quotes.json'
with open(title_file, 'w') as write_file:
    json.dump(list_quotes, write_file)
print(f'Данные сохранены в {title_file}')
