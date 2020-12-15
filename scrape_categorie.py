# encoding: utf-8
import requests
from bs4 import BeautifulSoup
from scrape_book import scrape_book
import argparse
import os
import csv


def scrape_categorie(url, name):
    r = requests.get(url)
    os.mkdir(name)      #création de dossier pour le fichier csv
    os.mkdir(name + '/' + 'img')        #création d'un dossier image pour les image
    url = url.replace('index.html','')      #replace l'index.html
    soup = BeautifulSoup(r.content, 'lxml')
    caractère_speciaux = '!/:"*?'       # création d'une variable string pour supprimer les caractère spéciaux
    num = 0
    while True:
        all_book = soup.findAll('div', {'class': 'image_container'})    #Recupération de tout les lien de chaque book
        for book in all_book:
            all_book = 'https://books.toscrape.com/catalogue/' + book.find('a')['href'].replace('../', '')
            data = scrape_book(all_book)    #appele de la fonction scrape_book
            r = requests.get(data["link_img"])
            for char in caractère_speciaux:
                data['titre'] = data['titre'].replace(char,'')
            with open(os.path.join('C:/OpenClassroom/P2_Boulahrouf_Ryad/' + name + '/img', data['titre'] + '.png'), "wb") as f:
                f.write(r.content)
                f.close()

            with open(name + "/fichier.csv",'a',newline='') as f:
                writer = csv.writer(f, delimiter = ',')
                num=num+1
                if (num==1):
                    writer.writerow(data["caractéristique_name"])
                writer.writerow(data["caractéristique_info"])


        if soup.find('li', {'class': 'next'}):  # si le bouton next est là
            page_next = url + soup.find('li', {'class': 'next'}).find('a')['href']
            r = requests.get(page_next)
            soup = BeautifulSoup(r.content, 'lxml')

        if not soup.find('li', {'class': 'next'}): # si le bouton next n'est pas la fin de la boucle while
            print("fin de la rubrique")
            break


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--url')
    parser.add_argument('--name')
    args = parser.parse_args()
    print(scrape_categorie(args.url, args.name))


if __name__ == '__main__':
    main()

