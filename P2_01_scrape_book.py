# encoding: utf-8
import argparse

import requests
from bs4 import BeautifulSoup


def removeprefix(self: str, prefix: str, /) -> str:
    if self.startswith(prefix):
        return self[len(prefix):]
    else:
        return self[:]


def removesuffix(self: str, suffix: str, /) -> str:
    if self.endswith(suffix):
        return self[:-len(suffix)]
    else:
        return self[:]


def scrape_book(url):
    """ Fonction qui prend en argument l'url du site
     et en extrait les données et les return """
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'lxml')
    title = soup.find('div', {'class': 'col-sm-6 product_main'})\
        .find('h1').text
    image_url = 'https://books.toscrape.com/' + \
                soup.find('div', {'class': 'item active'})\
        .find('img')['src'].replace('../', '')
    product_description = soup.find('head')\
        .find('meta', {'name': 'description'})['content'].replace('\n', '').strip()
    category = soup.find('ul', {'class': 'breadcrumb'}).findAll('a')[2].text
    product_information = soup.find('table', {'class': 'table table-striped'})\
        .findAll('td')
    universal_product_code = product_information[0].text
    product_page_url = url
    price_including_tax = product_information[2].text
    price_excluding_tax = product_information[3].text
    tax = product_information[4].text
    a = product_information[5].text
    number_available = removeprefix(a, "In stock (")
    number_available = removesuffix(number_available, "available)")
    number_of_reviews = product_information[6].text
    review_rating = soup.find("p", {"class": "star-rating"})['class'][1]
    liste_rating = ["One", "Two", "Three", "Four", "Five"].index(review_rating)+1
    return {"product_page_url": product_page_url, "universal_product_code": universal_product_code,
            "title": title, "price_including_tax": price_including_tax,
            "price_excluding_tax": price_excluding_tax, "tax": tax, "number_available": number_available,
            "number_of_reviews": number_of_reviews, "product_description": product_description,
            "category": category, "review_rating": liste_rating, "image_url": image_url}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--url')
    args = parser.parse_args()
    print(scrape_book(args.url))


if __name__ == '__main__':
    main()
