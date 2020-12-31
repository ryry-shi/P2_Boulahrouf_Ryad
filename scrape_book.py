# encoding: utf-8
import requests
from bs4 import BeautifulSoup
import argparse


def scrape_book(url):
    dict_data = {}
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'lxml')
    title = soup.find('div', {'class': 'col-sm-6 product_main'}).find('h1').text
    image_url = 'https://books.toscrape.com/'+soup.find('div', {'class': 'item active'}).find('img')['src'].replace('../', '')
    description_texte = soup.find('head').find('meta', {'name': 'description'})['content'].replace('\n', '').strip()
    product_information_1 = soup.find('table', {'class': 'table table-striped'}).findAll('th')
    upc = product_information_1[0].text
    product_type = product_information_1[1].text
    price_excl_tax = product_information_1[2].text
    price_incl_tax = product_information_1[3].text
    tax = product_information_1[4].text
    avaibility = product_information_1[5].text
    number_of_rewievs = product_information_1[6].text
    product_information_2 = soup.find('table', {'class': 'table table-striped'}).findAll('td')
    upc_un = product_information_2[0].text
    product_type_un = product_information_2[1].text
    liste_rating = soup.find("p", {"class": "star-rating"})
    num = 0

    if "One" in liste_rating['class'][1]:

        num = 1
    if "Two" in liste_rating['class'][1]:

        num = 2
    if "Three" in liste_rating['class'][1]:

        num = 3
    if "Four" in liste_rating['class'][1]:

        num = 4
    if "Five" in liste_rating['class'][1]:

        num = 5

    print(num)


    price_excl_tax_un = product_information_2[2].text
    price_incl_tax_un = product_information_2[3].text
    tax_un = product_information_2[4].text
    avaibility_un = product_information_2[5].text
    number_of_rewievs_un = product_information_2[6].text
    dict_data = {"UPC": upc, "Product Type": product_type, "price excl": price_excl_tax, "price incl": price_incl_tax,\
                "tax": tax, "avaibility": avaibility, "rewievs": number_of_rewievs,"etoile": num, "info_un":upc_un,\
                "info_deux": product_type_un, "info_trois": price_excl_tax_un, "info_quatre": price_incl_tax_un,\
                 "info_cinq": tax_un, "info_six": avaibility_un, "info_sept": number_of_rewievs_un,\
                 "texte": description_texte, "titre": title, "link_img": image_url}
    return dict_data


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--url')
    args = parser.parse_args()
    print(scrape_book(args.url))


if __name__ == '__main__':
    main()
