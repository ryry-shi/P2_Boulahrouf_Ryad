import requests
from bs4 import BeautifulSoup
import argparse


def scrape_book(url):
    dict_data = []
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'lxml')
    title = soup.find('div', {'class': 'col-sm-6 product_main'}).find('h1')
    image_url = 'https://books.toscrape.com/'+soup.find('div', {'class':'item active'}).find('img')['src'].replace('../', '')
    print(image_url)
    image_alt = soup.find('div', {'class': 'item active'}).find('img')['alt']
    dict_data.append(title)
    dict_data.append(image_url)
    return dict_data


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--url')
    args = parser.parse_args()
    print(scrape_book(args.url))


if __name__ == '__main__':
    main()
