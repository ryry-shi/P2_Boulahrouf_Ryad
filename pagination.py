import requests
from bs4 import BeautifulSoup
import argparse


def pagination(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'lxml')
    url = r.url
    index = url.rfind('/')
    url = url[0:index+1]
    while soup.find('li', {'class': 'next'}):
        end_link = soup.find('li', {'class': 'next'}).find('a')['href']
        page_next = url + str(end_link)
        print(page_next)
        return page_next


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--url')
    args = parser.parse_args()
    print(args.url)
    print(pagination(args.url))


if __name__ == '__main__':
    main()
