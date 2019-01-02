#scrape russel3000 index from a text file
tickers = []

def parse_rus3000():
    try:
        readFile = open('Russel3000_tickers.txt').read()
        splitFile = readFile.split('\n')
        for eachline in splitFile:
            splitLine = eachline.split(' ')
            ticker = splitLine[-1]
            if ticker:     #gets rid of white space
                tickers.append(ticker)
        print(tickers)                
    except Exception as e:
        print(e)

parse_rus3000()




