#this is just a play area for me to test out soup
import urllib
import urllib.request
from bs4 import BeautifulSoup

def make_soup(url):
    thepage = urllib.request.urlopen(url)
    soupdata = BeautifulSoup(thepage, "html.parser")
    return soupdata

soup = make_soup('https://finance.yahoo.com/quote/aes/financials')
rev_17 = soup('table')[0].findAll('tr')[1].findAll('td')[1].string
rev_16 = soup('table')[0].findAll('tr')[1].findAll('td')[2].string
print(rev_17)
print(rev_16)


