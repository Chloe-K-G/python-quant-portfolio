import yfinance as yf

def get_data(tickers, start="2020-01-01"):
    data = yf.download(tickers, start=start)["Close"]
    return data.dropna()