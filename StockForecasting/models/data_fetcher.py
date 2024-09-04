import yfinance as yf
import pandas as pd

def fetch_stock_data(ticker: str, period: str = '1y'):
    stock_data = yf.download(ticker, period=period)
    stock_data.reset_index(inplace=True)
    return stock_data
