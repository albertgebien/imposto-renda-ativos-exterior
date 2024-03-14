import yfinance as yf

etf = yf.Ticker("VT") 
nome_etf = etf.info['shortName']
print(nome_etf)