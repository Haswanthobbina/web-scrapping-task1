import requests
from bs4 import BeautifulSoup
import csv

base_url = 'https://quotes.toscrape.com'
url = '/'

quotes = []

while url:
    full_url = base_url + url
    response = requests.get(full_url)
    soup = BeautifulSoup(response.content, 'html.parser')

    
    quote_divs = soup.find_all('div', class_='quote')
    for quote in quote_divs:
        quote_text = quote.find('span', class_='text').get_text()
        author = quote.find('small', class_='author').get_text()
        quotes.append([quote_text, author])
        print(f"Quote: {quote_text}")
        print(f"Author: {author}")

    next_button = soup.find('li', class_='next')
    url = next_button.find('a')['href'] if next_button else None

with open('quotes.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Quote', 'Author'])
    writer.writerows(quotes)














#1st time with sample implementation
'''import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://quotes.toscrape.com/page/1/'
pages = requests.get(url)
soup = BeautifulSoup(pages.content, 'html.parser')

text = soup.find_all('div', class_='quote')
quotes = []

for quote in text:
    quote_text = quote.find('span', class_='text').get_text()
    author = quote.find('small', class_='author').get_text()
    quotes.append({'Quote': quote_text, 'Author': author})

    print(f"Quote: {quote_text}")
    print(f"Author: {author}")

df = pd.DataFrame(quotes)

df.to_excel("quotes_output.xlsx", index=False )'''

#second time implementation 
'''import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv

url = 'https://quotes.toscrape.com/'
pages = requests.get(url)
soup = BeautifulSoup(pages.content, 'html.parser')

text = soup.find_all('div', class_='quote')
quotes = []
for quote in text:
    quote_text = quote.find('span', class_='text').get_text()
    author = quote.find('small', class_='author').get_text()
    tags = [tag.get_text() for tag in quote.find_all('a', class_='tag')]
    quotes.append([quote_text, author])

    print(f"Quote: {quote_text}")
    print(f"Author: {author}")  

with open('quotes.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Quote', 'Author'])
    for quote in quotes:
        writer.writerow(quote)   '''