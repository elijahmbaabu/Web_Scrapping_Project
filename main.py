from bs4 import BeautifulSoup
import requests
from csv import writer

url = 'https://www.pararius.com/apartments/amsterdam-duivendrecht?ac=1'

page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
lists = soup.find_all('section', class_="listing-search-item")
with open('rentals.csv', 'w', encoding='utf8', newline='') as f:
    The_writer = writer(f)
    Header = ['Title', 'Location', 'Price', 'Area', 'Rooms', 'Construction Period']
    The_writer.writerow(Header)

for list in lists:
    title = list.find('a', class_="listing-search-item__link--title").text
    location = list.find('div', class_="listing-search-item__location").text
    price = list.find('div', class_="listing-search-item__price").text
    area = list.find('li', class_="illustrated-features__item--surface-area").text
    rooms = list.find('li', class_="illustrated-features__item--number-of-rooms").text
    construction = list.find('li', class_="illustrated-features__item--construction-period").text
    info = [title, location, price, area, rooms, construction]
    The_writer.writerow(Header)

