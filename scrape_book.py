# encoding: utf-8
import requests
from bs4 import BeautifulSoup
import argparse


def scrape_book(url):
    dict_data = {}
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'lxml')
    title = soup.find('div', {'class': 'col-sm-6 product_main'}).find('h1').text
    image_url = 'https://books.toscrape.com/'+soup.find('div', {'class': 'item active'})\
        .find('img')['src'].replace('../', '')
    description_texte = soup.find('head').find('meta', {'name': 'description'})
    if not soup.find('head').find('meta', {'name': 'description'}):
        description_texte = 'pas de description'
    image_alt = soup.find('div', {'class': 'item active'}).find('img')['alt']
    t_name = soup.find('table', {'class': 'table table-striped'}).find_all('th')
    carac_name = []
    for t in t_name:
        t_name = t.text
        carac_name.append(t_name)
    t_info = soup.find('table', {'class': 'table table-striped'}).find_all('td')
    carac_info = []
    for t in t_info:
        t_info = t.text
        carac_info.append(t_info)

    dict_data = {"caractéristique_name": carac_name, "caractéristique_info": carac_info,"titre":title , "link_img":image_url,
                 "texte": description_texte}

    return dict_data


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--url')
    args = parser.parse_args()
    print(scrape_book(args.url))


if __name__ == '__main__':
    main()
