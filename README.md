# Finance
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import yfinance as yf


stock_symbol = "HDFCBANK.NS"


stock_data = yf.download(stock_symbol, start="2023-02-01", end="2023-05-01")

sma_period = 5
stock_data['SMA'] = stock_data['Close'].rolling(window=sma_period).mean()



ema_period = 5
stock_data['EMA'] = stock_data['Close'].ewm(span=ema_period, adjust=False).mean()


plt.figure(figsize=(12, 6))
plt.plot(stock_data.index, stock_data['Close'], label='Close Price')
plt.plot(stock_data.index, stock_data['SMA'], label='SMA')
plt.plot(stock_data.index, stock_data['EMA'], label='EMA')
plt.xlabel('Date')
plt.ylabel('Price')
plt.title(f"SMA Indicator for {stock_symbol}")
plt.legend()
plt.show()
