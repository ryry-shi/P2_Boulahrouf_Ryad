import requests
from bs4 import BeautifulSoup
import argparse
from scrape_categorie import scrape_categorie


def scrape_website(url):
    categories = []
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'lxml')
    nav = soup.find('ul', {'class': 'nav nav-list'})
    links = nav.findAll('a')
    for link in links:
        url = 'https://books.toscrape.com/'+link['href']
        name = link.contents[0].replace('\n', '').strip()
        category = {'url': url, 'name': name}
        categories.append(category)
        scrape_categorie(url, name)
    return categories


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--url')
    args = parser.parse_args()
    print(scrape_website(args.url))


if __name__ == '__main__':
    main()
