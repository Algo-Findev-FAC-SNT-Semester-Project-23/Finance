#!/usr/bin/env python
# coding: utf-8

# In[1]:


import yfinance as yf
import pandas as pd
import pandas_ta as ta
import matplotlib.pyplot as plt

# Downloading historical data for ZOMATO.NS
data = yf.download("ZOMATO.NS", start="2023-01-01", end="2023-04-30")

# Displaying the data
print(data.head())

#Now we will calculate the SMA for this data by using pandas library(the rolling function)
sma = data['Close'].rolling(window=3).mean()

#now we will calculate the EMA for this data same as we calculate SMA 
ema = ta.ema(data['Close'],length=3)

#now we have SMA and EMA for this zomato data, we can easilt plot them using matplot library
plt.figure(figsize=(12,6))
plt.plot(data.index,data['Close'],label='Closing Price')
plt.plot(data.index,sma,label='SMA (3 months)')
plt.plot(data.index,ema,label='EMA (3 months)')
plt.xlabel('Data')
plt.ylabel('Price')
plt.title('Moving Average Indicator for ZOMATO.NS')
plt.legend()
plt.grid(True)
plt.show()







