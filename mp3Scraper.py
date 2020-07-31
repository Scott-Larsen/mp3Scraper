# A script for downloading non-copyrighted classical music mp3s

import requests
from requests.exceptions import MissingSchema, InvalidSchema
from bs4 import BeautifulSoup
import collections
# import pprint
# pp = pprint.PrettyPrinter(width=41, compact=True)
import time
import urllib.request
import os.path
# from os import path

seedURL = "https://www.classiccat.net/toplist.php"
saveLocation = "/Users/Scott/Downloads/"
projectLocation = "/Users/Scott/Desktop/DATA/SORT/CodingProgrammingPython/mp3Scraper/"
visitedURLsFileName = "visitedURLs.txt"
downloadedFilesFileName = "downloadedFiles.txt"

URLs = collections.defaultdict(int)
URLs[seedURL] = 1

visitedURLs = []

def readInReturnDelimitedTextFileToList(directory, filename):
    if os.path.exists(directory + filename):
        print(f"Opening {filename} and writing it into a list....\n")

        listFromFile = []
        # open file and read the content in a list
        with open(directory + filename, 'r') as filehandle:
            for line in filehandle:
                # remove linebreak which is the last character of the string
                currentLine = line[:-1]

                # add item to the list
                listFromFile.append(currentLine)
    print(f"Loaded in the following from file....\n{listFromFile}\n")
    return listFromFile

def writeOutListToReturnDelimitedTextFile(directory, filename, listToBeWrittenOut):
    if os.path.exists(directory + filename):
        print(f"Writing out list to {filename}....\n")
        with open(directory + filename, 'w') as filehandle:
            filehandle.writelines("%s\n" % item for item in listToBeWrittenOut)

l = [1,2,3]
writeOutListToReturnDelimitedTextFile(projectLocation, downloadedFilesFileName, l)

# print('') 

# try:
#     downloadedFiles = readInReturnDelimitedTextFileToList(projectLocation, downloadedFilesFileName)
# except:
#     pass
#     # downloadedFiles = []








# proceed = 'y'

# headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:73.0) Gecko/20100101 Firefox/73.0'}

# def download(link):
#     fileName = link.split('/')[-1]

#     if os.path.exists(saveLocation + fileName):
#         print(f"{fileName} is already downloaded.")
#         time.sleep(1)
#     else:
#         try:
#             urllib.request.urlretrieve(link, saveLocation + fileName)
#             print(f"{fileName} downloaded.")
#         except HTTPError:
#             pass
#         time.sleep(60)

# # download("http://d19bhbirxx14bg.cloudfront.net/bach-bwv938-breemer.mp3")

# def addLink(link):
#     if link not in visitedURLs and link[0] not in "/#":
#         try:
#             URLs[link] += 1
#         except:
#             URLs[link] = 1

# while URLs and proceed == 'y':
#     URL = (max(URLs, key=URLs.get))
#     # URL = URLs.pop(max(URLs, key=URLs.get))

#     del URLs[URL]

#     visitedURLs.append(URL)

#     print(f"Scanning {URL}")
#     try:
#         page = requests.get(URL, headers=headers)

#         # print(page)

#         soup = BeautifulSoup(page.content, 'html.parser')

#         URLSplit = URL.split('/')
#         URLUpOneLevel = '/'.join(URLSplit[:-1])
#         # print(URLUpOneLevel)
#         URLUpTwoLevels = '/'.join(URLSplit[:-2])
#         # print(URLUpTwoLevels)

#         for a in soup.findAll('a'):

#             link = a.get('href')
#             if link:
#                 if link[-4:] == ".mp3" and link not in downloadedFiles:
#                     # print(f"... downloading {link}")
#                     download(link)
#                 elif "sheetmusicplus" in link or link[:5] in ("index", "javas", "regis", "login"):
#                     pass
#                 else:
#                     if link[:6] == "../../":
#                         # print(f"{URL}")
#                         # URL = URL.split("/")
#                         # # print(f"{URL = }")
#                         # URL = URL[:-1]
#                         # URL = '/'.join(URL)
#                         link = URLUpTwoLevels + link[5:]
#                         # print(link)
                    
#                     elif link[:3] == "../":
#                         link = URLUpOneLevel + link[2:]
                    
#                     addLink(link)
        
#         print('')
#         tempURLList = sorted(URLs.keys(), key=lambda key: URLs[key], reverse = True)[:10]
#         for address in tempURLList:
#             print(URLs[address], address)
#         print('')
#         # print(tempURLs[:5])
#         # for key in URLs.keys():
#         #     print(key, URLs[key])

#         print('')
#         proceed = False
#         proceed = input("Press y to continue...")
#         print('')

#     except (MissingSchema, InvalidSchema):
#         print(f"Failed loading {URL}")