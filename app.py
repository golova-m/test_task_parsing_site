import requests
from bs4 import BeautifulSoup

url = 'https://quotes.toscrape.com/page'
number_page = 1
url_number = url + f'/{number_page}/'
print(url_number)
response = requests.get(url_number)
status_code = response.status_code
print(status_code)
while status_code == 200:
    print('Start')
    soup = BeautifulSoup(response.text, 'lxml')
    quotes = soup.find_all('span', class_='text')
    authors = soup.find_all('small', class_='author')
    tags = soup.find_all('div', class_='tags')

    for i in range(len(quotes)):
        print(quotes[i].text)
        print(f'by {authors[i].text}')
        tags_for_quote = tags[i].find_all('a', class_='tag')
        print(f'Tags:', end=' ')
        for tag in tags_for_quote:
            print(tag.text, end=' ')
        print('\n')
    
    number_page += 1
    url_number = url + f'/{number_page}/'
    print(url_number)
    response = requests.get(url_number)
    status_code = response.status_code
    if soup.find('li', class_='next') == None:
        status_code = 0
        print('Stop')
