import requests
from bs4 import BeautifulSoup
import urllib3
def crawler(maxpage):
    page=1
    while page<=maxpage:
        url = "https://en.wikipedia.org/wiki/Main_Page"
        source= requests.get(url)
        plain = source.text
        soup = BeautifulSoup(plain, "lxml")
        for link in soup.find_all('a'):
            x=10
            if link.get('href') is not None:
                href = "https://en.wikipedia.org"+ link.get("href")
                x=x+1
                http = urllib3.PoolManager()
                r = http.request('get', href)
                with open('C:\Aman\padhaii\sem 5\web mining\page list\page %d .html' %x, 'wb') as fid:
                    fid.write(r.data)
                page+=1
crawler(1)