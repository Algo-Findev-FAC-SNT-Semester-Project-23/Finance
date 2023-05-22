#!/usr/bin/env python
# coding: utf-8

# In[25]:


import pandas as pd
import seaborn as sns
import yfinance as yf
import numpy as np
import matplotlib as plt


# In[26]:


apple=yf.download('AAPL',
                  start='2023-02-22',
                  end='2023-05-21'
                  )
sma=apple.Close.mean()


# In[27]:


zero_data = np.zeros(shape=(len(apple),2))
sma1 = pd.DataFrame(zero_data)
sma1.index=apple.index


# In[28]:


for i in range (12,61):
    for j in range (0,12):
        sma1.iloc[i,0]=sma1.iloc[i,0]+apple.iloc[i+j-12,0]  
        
    sma1.iloc[i,0]=sma1.iloc[i,0]/12 

    sma1.iloc[i,1]=sma1.iloc[i,1]/26
for i in range(12,61):
    sma1.iloc[i,1]=apple['Close'][i-12]
    for j in range (0,12) :
        k=2/(j+1)
        sma1.iloc[i,1]=sma1.iloc[i,1]*(1-k)+apple['Close'][i+j-12] * k


# In[29]:


sns.lineplot(sma1.iloc[12:61,0],label='12 day sma')
sns.lineplot(apple["Close"],label='closing price')
sns.lineplot(sma1.iloc[12:61,1],label='12 day ema')


# In[ ]:




