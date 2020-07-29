import requests
from requests.exceptions import MissingSchema, InvalidSchema
from bs4 import BeautifulSoup
import collections
import pprint
pp = pprint.PrettyPrinter(width=41, compact=True)
import time

seedURL = "https://www.classiccat.net/toplist.php"

URLs = collections.defaultdict(int)
URLs[seedURL] = 1

visitedURLs = []
downloadedFiles = []

proceed = 'y'

headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:73.0) Gecko/20100101 Firefox/73.0'}

def download(link):
    pass

def addLink(link):
    if link not in visitedURLs and link[0] != "/":
        try:
            URLs[link] += 1
        except:
            URLs[link] = 1

while URLs and proceed == 'y':
    URL = (max(URLs, key=URLs.get))
    # URL = URLs.pop(max(URLs, key=URLs.get))

    del URLs[URL]

    visitedURLs.append(URL)

    print(f"Scanning {URL}")
    try:
        page = requests.get(URL, headers=headers)

        # print(page)

        soup = BeautifulSoup(page.content, 'html.parser')

        URLSplit = URL.split('/')
        URLUpOneLevel = '/'.join(URLSplit[:-1])
        # print(URLUpOneLevel)
        URLUpTwoLevels = '/'.join(URLSplit[:-2])
        # print(URLUpTwoLevels)

        for a in soup.findAll('a'):

            link = a.get('href')
            if link:
                if link[-4:] == ".mp3" and link not in downloadedFiles:
                    print(f"... downloading {link}")
                    download(link)
                    time.sleep(60)

                else:
                    if link[:6] == "../../":
                        # print(f"{URL}")
                        # URL = URL.split("/")
                        # # print(f"{URL = }")
                        # URL = URL[:-1]
                        # URL = '/'.join(URL)
                        link = URLUpTwoLevels + link[5:]
                        # print(link)
                    
                    elif link[:3] == "../":
                        link = URLUpOneLevel + link[2:]
                    
                    addLink(link)


        print('')
        print(max(URLs, key=URLs.get))
        print('')
        break
        # for key in URLs.keys():
        #     print(key)

        proceed = False
        proceed = input("Press y to continue...")

    except (MissingSchema, InvalidSchema):
        print(f"Failed loading {URL}")