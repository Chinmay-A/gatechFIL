import os

file_path='./sec-edgar-filings/MSFT/10-K/0001032210-00-001961/full-submission.txt'

def to_html(file_path,to_path):
    
    with open(file_path,'r') as inputfile:

        docs=inputfile.read()

    with open(to_path,'w') as htmlfile:

        htmlfile.write(docs)

tickers=['TSLA','TRU','TWLO']


for ticker in tickers:

    n_filling=0
    
    base_url=f'./sec-edgar-filings/{ticker}/10-K'
    
    folders=os.listdir(base_url)

    for folder in folders:

        print(folder)
        to_html(f'{base_url}/{folder}/full-submission.txt',f'./sec-edgar-filings/{ticker}/htmlfillings/{ticker}{str(n_filling)}.html')
        n_filling+=1
    
