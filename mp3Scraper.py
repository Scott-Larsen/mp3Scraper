# A script for downloading non-copyrighted classical music mp3s

import requests
from requests.exceptions import MissingSchema, InvalidSchema
from bs4 import BeautifulSoup
import collections
import time
import urllib.request
import os.path
from urllib import parse
from urllib.parse import quote, unquote, urljoin
from urllib.error import HTTPError, URLError
import random

seedURL = "https://www.classiccat.net/toplist.php"
saveLocation = "/Users/Scott/Downloads/"
projectLocation = "/Users/Scott/Desktop/DATA/SORT/CodingProgrammingPython/mp3Scraper/"
visitedURLsFileName = "visitedURLs.txt"
downloadedFilesFileName = "downloadedFiles.txt"
URLsToScrapeFileName = "URLsToScrape.txt"


def readInReturnDelimitedTextFileToDataStructure(directory, filename):
    listFromFile = []
    dictionaryFromFile = {}

    if os.path.exists(directory + filename):
        print(f"Opening {filename} and writing it into a data structure....\n")

        with open(directory + filename, "r") as filehandle:
            for line in filehandle:
                currentLine = line[:-1]
                if " " in currentLine:
                    currentLine = currentLine.split()
                    try:
                        dictionaryFromFile[currentLine[0]] = int(currentLine[1])
                    except:
                        pass
                else:
                    listFromFile.append(currentLine)
    if len(listFromFile) >= len(dictionaryFromFile):
        dataStructureToReturn = listFromFile
    else:
        dataStructureToReturn = dictionaryFromFile
    print(f"Loaded in {filename}.\n")
    return dataStructureToReturn


def writeOutDataStructureToReturnDelimitedTextFile(
    directory, filename, dataStructureToBeWrittenOut
):
    if os.path.exists(directory + filename):
        print(f"Writing out list to {filename}....\n")
        with open(directory + filename, "w") as filehandle:
            if isinstance(dataStructureToBeWrittenOut, list):
                filehandle.writelines(
                    f"{item}\n" for item in dataStructureToBeWrittenOut
                )
            elif isinstance(dataStructureToBeWrittenOut, dict):
                filehandle.writelines(
                    f"{key} {dataStructureToBeWrittenOut[key]}\n"
                    for key in dataStructureToBeWrittenOut.keys()
                )


def download(link):
    fileName = link.split("/")[-1]
    fileName = unquote(fileName)

    if os.path.exists(saveLocation + fileName):
        print(f"{fileName} is already downloaded.")
        time.sleep(1)
    else:
        try:
            urllib.request.urlretrieve(link, saveLocation + fileName)
            print(f"{fileName} downloaded.")
        except (urllib.error.HTTPError, urllib.error.URLError) as err:
            try:
                print(f"{err.code} Error downloading {link}")
            except:
                pass
            pass
        time.sleep(random.randint(10, 60))


def addLink(link):
    if link not in visitedURLs and link not in URLsToScrape and link[0] not in "/#":
        URLsToScrape.append(link)


print("")

visitedURLs = readInReturnDelimitedTextFileToDataStructure(
    projectLocation, visitedURLsFileName
)
downloadedFiles = readInReturnDelimitedTextFileToDataStructure(
    projectLocation, downloadedFilesFileName
)
URLsToScrape = readInReturnDelimitedTextFileToDataStructure(
    projectLocation, URLsToScrapeFileName
)

if len(URLsToScrape) == 0:
    URLsToScrape = [seedURL]

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:73.0) Gecko/20100101 Firefox/73.0"
}

while URLsToScrape:
    URL = URLsToScrape.pop(0)

    visitedURLs.append(URL)

    print(f"\nScanning {URL}\n")
    try:
        page = requests.get(URL, headers=headers)

        soup = BeautifulSoup(page.content, "html.parser")

        for a in soup.findAll("a"):
            link = a.get("href")
            link = urljoin(URL, link)

            scheme, netloc, path, query, fragment = parse.urlsplit(link)
            path = unquote(path)
            path = quote(path)
            link = parse.urlunsplit((scheme, netloc, path, query, fragment))

            if link:
                if link in visitedURLs:
                    pass

                if link[-4:] == ".mp3" and link not in downloadedFiles:
                    try:
                        download(link)
                    except:
                        pass
                    downloadedFiles.append(link)
                elif (
                    link[:5] in ("index", "javas", "regis", "login")
                    or "blog" in link
                    or "facebook" in link
                    or "zendesk" in link
                    or "articles" in link
                    or "bbb.org" in link
                    or "oper" in link
                    or "vocal" in link
                    or "choir" in link
                    or "choe" in link
                    or "chor" in link
                    or "coro" in link
                    or "coral" in link
                    or "koor" in link
                    or "kant" in link
                    or "voca" in link
                    or "sing" in link
                    or "song" in link
                    or "teat" in link
                    or "theat" in link
                ):
                    pass
                else:
                    addLink(link)

        writeOutDataStructureToReturnDelimitedTextFile(
            projectLocation, visitedURLsFileName, visitedURLs
        )
        writeOutDataStructureToReturnDelimitedTextFile(
            projectLocation, downloadedFilesFileName, downloadedFiles
        )
        writeOutDataStructureToReturnDelimitedTextFile(
            projectLocation, URLsToScrapeFileName, URLsToScrape
        )

        time.sleep(random.randint(1, 5))

    except (MissingSchema, InvalidSchema):
        print(f"Failed loading {URL}")
