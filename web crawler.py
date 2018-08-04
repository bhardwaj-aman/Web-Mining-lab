# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 20:07:13 2018

@author: justf
"""

import requests
from bs4 import BeautifulSoup

def crawler(maxpage):
    page=1
    while page<=maxpage:
        url = "https://en.wikipedia.org/wiki/Main_Page"
        source= requests.get(url)
        plain = source.text
        soup = BeautifulSoup(plain, "lxml")
        for link in soup.find_all('a'):
            if link.get('href') is not None:
                href = "https://en.wikipedia.org"+ link.get("href")
                print(href)
                page+=1
crawler(1)           