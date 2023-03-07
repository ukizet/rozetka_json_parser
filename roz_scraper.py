import requests
from bs4 import BeautifulSoup
import json

def get_titles_and_prices(element_class, title_class, value_class, symbols_to_replace_with_space):
    for item in soup.find_all('div', class_=element_class):
        name = item.find('span', class_=title_class)

        price = item.find('span', class_=value_class)
        price = price.text.replace(symbols_to_replace_with_space, ' ')

        prices[name.text.strip()] = price

    pass

def save_to_json(file_name):
    with open(file_name, 'w', encoding="utf-8") as file:
        json.dump(prices, file, indent=4, ensure_ascii=False)
        pass

def main():
    # Вставляємо лінку

    url = 'https://rozetka.com.ua/ua/mobile-phones/c80003/'

    response = requests.get(url)

    global soup
    soup = BeautifulSoup(response.text, 'html.parser')

    global prices
    prices = {}

    # Проходимося по кожному товару на сторінці та зберігаємо його назву й ціну в словник

    get_titles_and_prices('goods-tile__inner', 'goods-tile__title', 'goods-tile__price-value', '\xa0')

    # Зберігаємо словник в json файл

    save_to_json('ex1.json')

if __name__ == '__main__':
    main()
