import yfinance as yf

data = yf.download("AAPL", start="2020-12-01", end="2021-01-01")
print(data.head())