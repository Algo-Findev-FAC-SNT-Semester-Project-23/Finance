#!/usr/bin/env python
# coding: utf-8

# In[12]:


import pandas as pd
import seaborn as sns
import yfinance as yf
import numpy as np
import matplotlib as plt


# In[13]:


amazon=yf.download('AMZN',
                  start='2023-02-22',
                  end='2023-05-21'
                  )
sma=amazon.Close.mean()
print(sma)


# In[14]:


sns.lineplot(data=amazon['Close'],label="Close")
sns.lineplot(data=amazon['Open'],label="open")


# In[15]:


#sma1=pd.DataFrame({'five_day_sma':[]})
#sma1.five_day_sma.astype('float64')
#print(sma1)
zero_data = np.zeros(shape=(len(amazon),3))
sma1 = pd.DataFrame(zero_data)
sma1.index=amazon.index


# In[16]:


for i in range (12,61):
    for j in range (0,12):
        sma1.iloc[i,0]=sma1.iloc[i,0]+amazon.iloc[i+j-12,0]  
        #print(sma1.iloc[i,0])
        #print(j)
        #print(i)
    sma1.iloc[i,0]=sma1.iloc[i,0]/12 
for i in range (26,61):
    for j in range (0,26):
        sma1.iloc[i,1]=sma1.iloc[i,1]+amazon.iloc[i+j-26,1]  
        #print(sma1.iloc[i,0])
        #print(j)
        #print(i)
    sma1.iloc[i,1]=sma1.iloc[i,1]/26
for i in range(12,61):
    sma1.iloc[i,2]=amazon['Close'][i-12]
    for j in range (0,12) :
        k=2/(j+1)
        sma1.iloc[i,2]=sma1.iloc[i,2]*(1-k)+amazon['Close'][i+j-12] * k
    
    #print(sma1.iloc[i,0])
    #print (i)


# In[17]:


sns.lineplot(sma1.iloc[12:61,0],label='12 day sma')
sns.lineplot(amazon["Close"],label='closing price')
sns.lineplot(sma1.iloc[26:61,1],label='26 day sma')
sns.lineplot(sma1.iloc[12:61,2],label='12 day ema')
