import requests
from bs4 import BeautifulSoup
from scrape_book import scrape_book
from pagination import pagination
import argparse
import os
import csv


def scrape_categorie(url,name):
    r = requests.get(url)
    os.mkdir(name)#Création de dossier pour écriture de fichier csv
    soup = BeautifulSoup(r.content, 'lxml')
    all_book = soup.findAll('div', {'class': 'image_container'})
    #categorie = soup.findAll('ul', {'nav nav-list'})
    #print(categorie)
    if soup.find('li', {'class': 'next'}):#Écriture de fichier pour les rubrique avec plusieur page
        while soup.find('li', {'class': 'next'}):
            for book in all_book:
                all_book = 'https://books.toscrape.com/catalogue/'+book.find('a')['href'].replace('../', '')
                img_url = 'https://books.toscrape.com/' + book.find('img')['src'].replace('../', '')
                with open(name, 'w') as file_url:
                    url = img_url
                    r = requests.(url)


               # with open(name+"/fichier.csv", 'a', newline='') as f:

                #    spamwriter = csv.writer(f, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
       #             spamwriter.writerow(scrape_book(all_book))

                #page_next = pagination(url)
                #r = requests.get(page_next)
                #soup = BeautifulSoup(r.content, 'lxml')
                #all_book = soup.findAll('div', {'class': 'image_container'})
                #url = page_next
    else:#Écriture de fichier pour les rubrique avec une seule page
        for book in all_book:
            all_book = 'https://books.toscrape.com/catalogue/' + book.find('a')['href'].replace('../', '')
            img_url = 'https://books.toscrape.com/'+book.find('img')['src'].replace('../','')

            with open(name,'wb') as file_url:
                r = requests.get(img_url)
                file_url.write(r.content)
            with open(name + "/fichier.csv", 'a', newline='') as f:
                spamwriter = csv.writer(f, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                spamwriter.writerow(scrape_book(all_book))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--url')
    parser.add_argument('--name')
    args = parser.parse_args()
    print(scrape_categorie(args.url,args.name))


if __name__ == '__main__':
    main()
