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
from urllib.parse import urljoin

seedURL = "https://www.classiccat.net/toplist.php"
saveLocation = "/Users/Scott/Downloads/"
projectLocation = "/Users/Scott/Desktop/DATA/SORT/CodingProgrammingPython/mp3Scraper/"
visitedURLsFileName = "visitedURLs.txt"
downloadedFilesFileName = "downloadedFiles.txt"
URLsToScrapeFileName = "URLsToScrape.txt"


URLsToScrape = collections.defaultdict(int)

def readInReturnDelimitedTextFileToDataStructure(directory, filename):
    listFromFile = []
    dictionaryFromFile = {}
        
    if os.path.exists(directory + filename):
        print(f"Opening {filename} and writing it into a data structure....\n")

        # open file and read the content in a list
        with open(directory + filename, 'r') as filehandle:
            # print("hola")
            # print(f"hello {filehandle[0]}")
            for line in filehandle:
                # print(line)
                # remove linebreak which is the last character of the string
                currentLine = line[:-1]
                if " " in currentLine:
                    print(f"Before split, {currentLine = }")
                    currentLine = currentLine.split()
                    # currentLineSplit = currentLine.split()
                    print(f"After split, {currentLine = }")
                    try:
                        dictionaryFromFile[currentLine[0]] = int(currentLine[1])
                    except:
                        pass
                else:
                    # add item to the list
                    listFromFile.append(currentLine)
    if len(listFromFile) >= len(dictionaryFromFile):
        dataStructureToReturn = listFromFile
    else:
        dataStructureToReturn = dictionaryFromFile
    print(f"Loaded in the following from file....\n{dataStructureToReturn}\n")
    return dataStructureToReturn

def writeOutDataStructureToReturnDelimitedTextFile(directory, filename, dataStructureToBeWrittenOut):
    # i = "y"
    if os.path.exists(directory + filename):
    #     i = False
    #     i = input(f"Overwrite {filename}?  y/n? ")
    # if i in "yY":
        print(f"Writing out list to {filename}....\n")
        with open(directory + filename, 'w') as filehandle:
            if isinstance(dataStructureToBeWrittenOut, list):
                filehandle.writelines(f"{item}\n" for item in dataStructureToBeWrittenOut)
            elif isinstance(dataStructureToBeWrittenOut, dict):
                filehandle.writelines(f"{key} {dataStructureToBeWrittenOut[key]}\n" for key in dataStructureToBeWrittenOut.keys())

def download(link):
    fileName = link.split('/')[-1]

    if os.path.exists(saveLocation + fileName):
        print(f"{fileName} is already downloaded.")
        time.sleep(1)
    else:
        try:
            urllib.request.urlretrieve(link, saveLocation + fileName)
            print(f"{fileName} downloaded.")
        except HTTPError:
            pass
        time.sleep(60)

# download("http://d19bhbirxx14bg.cloudfront.net/bach-bwv938-breemer.mp3")

def addLink(link):
    if link not in visitedURLs and link[0] not in "/#":
        # print(link)
        try:
            URLsToScrape[link] += 1
        except:
            URLsToScrape[link] = 1


print('') 

# Read in downloadedFiles list if it exists
visitedURLs = readInReturnDelimitedTextFileToDataStructure(projectLocation, visitedURLsFileName)
downloadedFiles = readInReturnDelimitedTextFileToDataStructure(projectLocation, downloadedFilesFileName)
URLsToScrape = readInReturnDelimitedTextFileToDataStructure(projectLocation, URLsToScrapeFileName)

if len(URLsToScrape) == 0:# and seedURL not in visitedURLs:
    URLsToScrape = collections.defaultdict(int)
    URLsToScrape[seedURL] = 1

# downloadedFiles = [6,7,8]
# downloadedFiles = {"a": 1, "b": 2}

# # Write out downloadedFiles list to file
# writeOutDataStructureToReturnDelimitedTextFile(projectLocation, downloadedFilesFileName, downloadedFiles)

# proceed = 'y'

headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:73.0) Gecko/20100101 Firefox/73.0'}

while URLsToScrape:# and proceed == 'y':
    # URL = (max(URLsToScrape, key=URLsToScrape.get))
    URL = URLsToScrape.pop(0)

    del URLsToScrape[URL]

    visitedURLs.append(URL)

    print(f"Scanning {URL}")
    try:
        page = requests.get(URL, headers=headers)

        # print(page)

        soup = BeautifulSoup(page.content, 'html.parser')



        # URLSplit = URL.split('/')
        # URLUpOneLevel = '/'.join(URLSplit[:-1])
        # # print(URLUpOneLevel)
        # URLUpTwoLevels = '/'.join(URLSplit[:-2])
        # # print(URLUpTwoLevels)

        for a in soup.findAll('a'):
            # print(a)
            link = a.get('href')
            # print(f"link before join:\n{link}")
            link = (urljoin(URL, link))
            # print(f"link after join:\n{link}")
            # print(link)

            # try:
            #     print(link[:4])
            # except:
            #     pass

            if link:
                if link in visitedURLs:
                    # print("Link in visitedURLs")
                    pass

                if link[-4:] == ".mp3" and link not in downloadedFiles:
                    # print(f"... downloading {link}")
                    download(link)
                    downloadedFiles.append(link)
                elif link[:5] in ("index", "javas", "regis", "login") or "blog" in link or "facebook" in link or 'zendesk' in link or "articles" in link or "bbb.org" in link or "oper" in link or "vocal" in link or "choir" in link or "choe" in link or "chor" in link or "coro" in link or "koor" in link or "kant" in link or "voca" in link or "sing" in link or "song" in link or "teat" in link or "theat" in link:# or link[:4] != 'http':
                    # print(f"{link} - Link in unique qualifiers")
                    pass
                else:
                    # print(link)
                    addLink(link)

            # break

        # Write out visitedURLs and downloadedFiles lists to files
        writeOutDataStructureToReturnDelimitedTextFile(projectLocation, visitedURLsFileName, visitedURLs)
        writeOutDataStructureToReturnDelimitedTextFile(projectLocation, downloadedFilesFileName, downloadedFiles)
        writeOutDataStructureToReturnDelimitedTextFile(projectLocation, URLsToScrapeFileName, URLsToScrape)
        
        # for key in URLsToScrape.keys():
            # print(type(URLsToScrape[key]))
            # try:
            #     if URLsToScrape[key].isalpha():
            #         print(key, URLsToScrape[key])
            # except:
            #     pass
            
        print('')
        tempURLList = sorted(URLsToScrape.keys(), key=lambda key: URLsToScrape[key], reverse = True)[:10]
        for address in tempURLList:
            print(URLsToScrape[address], address)
        print('')
        # print(tempURLs[:5])
        # for key in URLs.keys():
        #     print(key, URLs[key])

        print('')
        # proceed = False
        # proceed = input("Press y to continue...")
        print('')

        time.sleep(1)

    except (MissingSchema, InvalidSchema):
        print(f"Failed loading {URL}")