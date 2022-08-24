# This file will contain functions for scraping data from the various sites we need to pull data from.

# from time import sleep
# from requests_html import HTMLSession
# import json
# from pprint import pprint
# from alive_progress import alive_bar
# from pathlib import Path
# import html5lib
# from bs4 import BeautifulSoup

headers = {
    "Host" : "gwasi.com",
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0",
    "Accept" : "*/*",
    "Accept-Language" : "en-US,en;q=0.5",
    "Accept-Encoding" : "gzip, deflate, br",
    "Referer" : "https://gwasi.com/",
    "X-KL-Ajax-Request" : "Ajax_Request",
    "DNT" : "1",
    "Connection" : "keep-alive",
    "Sec-Fetch-Dest" : "empty",
    "Sec-Fetch-Mode" : "cors",
    "Sec-Fetch-Site" : "same-origin",
    "TE" : "trailers"
}