from sec_edgar_downloader import Downloader

def get_fillings(ticker):

    downloader=Downloader('Test Company','test@testmail.com')
    downloader.get("10-K",ticker,after="1995-01-01",before="2024-01-01")

tickers=['TSLA','TRU','TWLO']

for ticker in tickers:

    get_fillings(ticker)