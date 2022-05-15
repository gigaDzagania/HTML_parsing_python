import requests
from bs4 import BeautifulSoup
import csv
from time import sleep
from random import randint

f = open('laptop.csv', 'w', newline='\n')
file = csv.writer(f)
file.writerow(["BRAND", "PRICE", "IMAGE"])

for i in range(1, 5):
    url = f"https://alta.ge/notebooks-page-{i}.html"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    sub_soup = soup.find('div', class_='grid-list')
    all_laptops = sub_soup.find_all('div', class_='ty-column3')
    for laptop in all_laptops:
        brand = (laptop.find('a', class_="product-title")).text
        brand = brand[:int(brand.find(" ", 10))]
        price = (laptop.find('span', class_="ty-price-num")).text
        image = (laptop.find('img', class_="ty-pict")).attrs.get('src')
        print(price)
        file.writerow([brand, price, image])

    sleep(randint(15, 20))

f.close()
