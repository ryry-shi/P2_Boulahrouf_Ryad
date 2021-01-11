import requests
from bs4 import BeautifulSoup
from scrape_category import scrape_category
import os


def scrape_website(url):
    categories = []
    os.mkdir("data")        # Creation d'un dossier pour les fichier.csv
    os.mkdir("img")         # Creation d'un dossier pour les image
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'lxml')
    nav = soup.find('ul', {'class': 'nav nav-list'})        # Parse toute les rubriques du site
    links = nav.findAll('a')
    for link in links:
        url = 'https://books.toscrape.com/'+link['href']
        name = link.contents[0].replace('\n', '').strip()
        category = {'url': url, 'name': name}
        categories.append(category)
        scrape_category(url, name)


def main():

    print(scrape_website("https://books.toscrape.com/index.html"))


if __name__ == '__main__':
    main()
