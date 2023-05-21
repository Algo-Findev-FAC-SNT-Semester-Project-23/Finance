# Finance
# importing all the python libraries needed
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import yfinance as yf

# Now I have choosen RELIANCE as stock symbol out of all the NIFTY 50 stocks and dowlaoded its data from yahoo in time frame from 2023-01-01 to 2023-04-30.

stock_symbol = "RELIANCE.NS" 
stock_data = yf.download(stock_symbol, start="2023-01-01", end="2023-04-30")
stock_data

# extracting close prices because it represents the final traded price of the stock for a given trading day. 

close_prices = stock_data["Close"]
close_prices

# calculating sma by adding up the last sma period's closing prices and then dividing that number by sma period.

sma_period = 5
sma_values = np.empty_like(close_prices)
sma_values[:sma_period] = np.nan
sma_values

# Calculate SMA for each index using a window of size sma_period

for i in range(sma_period, len(close_prices)):
    sma_values[i] = np.mean(close_prices[i - sma_period : i])

stock_data["SMA"] = sma_values
stock_data

# calculating ema 

ema_period = 5  
weights = np.exp(-np.arange(ema_period) / ema_period)
weights /= np.sum(weights)
weights

# claculating smoothing factor and ema for each index using formula EMA = Closing price x multiplier + EMA (previous day) x (1-multiplier)


smoothing_factor = 2 / (ema_period + 1)

ema_values = np.zeros(len(close_prices))
ema_values[:ema_period - 1] = np.nan

ema_values[ema_period - 1] = np.mean(close_prices[:ema_period]) 
for i in range(ema_period, len(close_prices)):
    ema_values[i] = ema_values[i - 1] * smoothing_factor + close_prices[i] * (1 - smoothing_factor)

stock_data["EMA"] = ema_values
stock_data

# plotting the graph 
# deciding size of figure
plt.figure(figsize=(12, 6))   
# defining different names for different types of averages 
plt.plot(stock_data["Close"], label="Close")
plt.plot(stock_data["SMA"], label="SMA")
plt.plot(stock_data["EMA"], label="EMA")
# labelling the axes and giving titles
plt.xlabel("Date")
plt.ylabel("Price")
plt.title(f"{stock_symbol} - Moving Average Indicators")
plt.legend()
plt.grid(True)
plt.show()


