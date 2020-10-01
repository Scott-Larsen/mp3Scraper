## mp3Scraper

A script for downloading mp3 files form the web.

## Motivation

I like to listen to classical music while I code and recently found out that streaming music online was resource intensive so I decided to download a library of royalty-free (for personal use) mp3s so I wouldn't have to stream.

## Language

Python 3 script

## Code style

Formatted with the code formatter Black.

## Installation

This is to be run from your terminal (`python3 mp3Scraper.py`). I'm using a Mac so filenames are formatted accordingly. Most all of the settings are just below the import statements in `mp3Scraper.py` with a few text filters to try to rule out music with singing about three quarters of the way down the script. I used `https://www.classiccat.net/toplist.php` as my _seed_ URL because it's a great compendium of classical mp3s available online. You might be able to adapt it to another URL if you're seeking another type of music. Assuming you'll want a fresh start, I would delete the contents of `downloadedFiles.txt`, `URLsToScrape.txt` and `visitedURLs.txt`.

## Tests

None

## License

MIT © [Scott Larsen](https://ScottLarsen.com)
