import time
import urllib
from urllib.request import urlopen
import pandas as pd
from bs4 import BeautifulSoup

sp500 = []

def scrape_sp500():
    data = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    table = data[0]
    sliced_table = table[1:]
    header = table.iloc[0]
    corrected_table = sliced_table.rename(columns=header)
    tickers = corrected_table['Symbol'].tolist()
    return tickers

def make_soup(url):
    thepage = urllib.request.urlopen(url)
    soupdata = BeautifulSoup(thepage, "html.parser")
    return soupdata    

def yahooKeyStats(stock):    
    try:
        soup = make_soup('https://finance.yahoo.com/quote/' + stock +'/key-statistics')
        rev_growth = soup('table')[4].findAll('tr')[2].findAll('td')[1].string
        rev_growth = float(rev_growth[:-1].replace(',','')) #truncate the % before typecasting to float
        earning_growth = soup('table')[4].findAll('tr')[7].findAll('td')[1].string
        earning_growth = float(earning_growth[:-1].replace(',',''))
        pe = soup('table')[0].findAll('tr')[2].findAll('td')[1].string
        pe = float(pe[:-1].replace(',',''))
        
        if earning_growth > 20 or rev_growth > 20:
            if pe < 45:
                soup = make_soup('https://finance.yahoo.com/quote/'+ stock + '/financials')
                rev_17 = soup('table')[0].findAll('tr')[1].findAll('td')[1].string
                rev_16 = soup('table')[0].findAll('tr')[1].findAll('td')[2].string
                if float(rev_17.replace(',',''))/float(rev_16.replace(',','')) > 1.2:
                    print(stock)
                    print('Revenue growth: ' + str(rev_growth))
                    print('Earning growth: ' + str(earning_growth))
                    print('PE: ' + str(pe))
                    print('rev_17: ' + str(rev_17))
                    print('rev_16: ' + str(rev_16) + '\n')                    
        
    except Exception as e: 
        x=0              

sp500 = scrape_sp500()

for stock in sp500:
    yahooKeyStats(stock)

