# encoding: utf-8
import requests
from bs4 import BeautifulSoup
from scrape_book import scrape_book
import argparse
import os
import csv


def scrape_categorie(url, name):
    r = requests.get(url)
    os.mkdir(name)                  # création de dossier pour le fichier csv
    os.mkdir(name + '/' + 'img')                # création d'un dossier image pour les image
    url = url.replace('index.html', '')             # replace l'index.html
    soup = BeautifulSoup(r.content, 'lxml')
    caractère_speciaux = '!/:,"*?'               # création d'une variable string pour supprimer les caractère spéciaux
    num = 0
    with open(name + "/fichier.csv", 'a', newline='', encoding="utf-8") as f:
        writer = csv.writer(f, delimiter=';')

        while True:
            all_book = soup.findAll('div', {'class': 'image_container'})      # recupération de tout les lien de chaque book
            for book in all_book:
                end_book = book.find('a')['href'].replace('../', '')
                all_book = 'https://books.toscrape.com/catalogue/' + end_book
                data = scrape_book(all_book)            # appele de la fonction scrape_book
                r = requests.get(data["link_img"])
                for char in caractère_speciaux:
                    data['titre'] = data['titre'].replace(char, '')
                i = ""
                if data['link_img'] =="https://books.toscrape.com/media/cache/ac/1a/ac1a0546d9cdf6cd82ab7712a6c418df.jpg":
                    print("img")
                    i = "(1)"
                with open(os.path.join('C:/OpenClassroom/P2_Boulahrouf_Ryad/' + name + '/img', data['titre'] + i +'.png'), "wb") as f:
                    f.write(r.content)
                    f.close()


                    num = num+1
                    #print(num)
                    if(num == 1):
                        print(all_book)
                        writer.writerow(data["caractéristique_name"])
                    writer.writerow([data["caractéristique_info"]] + [data["titre"]]+ [data['link_img']] + [data["texte"]])

            if soup.find('li', {'class': 'next'}):      #si le bouton next est là
                end_link = soup.find('li', {'class': 'next'}).find('a')['href']
                page_next = url + end_link
                print(page_next)
                r = requests.get(page_next)
                soup = BeautifulSoup(r.content, 'lxml')
            elif not soup.find('li', {'class': 'next'}):
                print("fin de la rubrique " +  (name) )
                break



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--url')
    parser.add_argument('--name')
    args = parser.parse_args()
    print(scrape_categorie(args.url, args.name))


if __name__ == '__main__':
    main()
