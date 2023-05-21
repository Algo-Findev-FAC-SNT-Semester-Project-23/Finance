#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install numpy matplotlib seaborn yfinance')


# In[2]:


import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import yfinance as yf


# In[3]:


ticker = "HDFCBANK.NS"


# In[4]:


data = yf.download(ticker, start="2023-01-01", end="2023-04-01", interval="1d")
print (data);


# In[5]:


avg_arr = [0]*62;
for i in range(0,58):
    avg_arr[i+4] = (data.Close[i]+data.Close[i+1]+data.Close[i+2]+data.Close[i+3]+data.Close[i+4])/5

print(avg_arr)


# In[17]:


keys=data.Close.keys()
plt.plot(keys[4:],avg_arr[4:],label='SMA')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.grid(True)


# In[54]:





# In[7]:


ema_arr= [0]*62
a=data.Close[0];
for i in range(0,62):
    a= data.Close[i]*(2/6)+a*(1-(2/6));
    ema_arr[i]= a;
    
print(ema_arr)

    


# In[19]:


plt.plot(keys,ema_arr,label='EMA')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.grid(True)


# In[16]:


plt.figure(figsize=(12, 6))
plt.plot(keys,data.Close, label='Close')
plt.plot(keys[4:],avg_arr[4:], label='SMA')
plt.plot(keys,ema_arr, label='EMA')
plt.xlabel('Date')
plt.ylabel('Price')
plt.title ('SMA and EMA Calculation')
plt.legend()
plt.grid(True)
plt.show()


# In[ ]:




