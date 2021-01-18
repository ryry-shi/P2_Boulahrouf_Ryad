import requests
from bs4 import BeautifulSoup
from scrape_category import scrape_category
import os


def scrape_website(url):
    """ Fonction qui va d'abord créer deux dossier un
    data où il y aura les fichier csv et un autre img où il y aura les
    toutes les images télécharger. Il extrait le nom des catégorie
     et leur url et l'envois en url a la fonction
     scrape_catégorie qui extrait tout les book d'une catégorie
      et appele la fonction scrape_book
    pour extraire les information"""
    categories = []
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'lxml')
    # Parse toute les rubriques du site
    nav = soup.find('ul', {'class': 'nav nav-list'})
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
