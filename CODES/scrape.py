import requests
from bs4 import BeautifulSoup

url = 'https://www.youtube.com'
response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, 'html.parser')
print(soup.title.string)

products = soup.find_all('div', class_='product')

for product in products:
    name = product.find('div', class_='name').string
    price = product.find('div', class_='price').string

    print(name, price)

