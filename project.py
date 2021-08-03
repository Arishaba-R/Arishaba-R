#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import Quandl as q


# In[ ]:


q.ApiConfig.api_key = "SoUsdH6em6gXrDiUnqzv"


# In[ ]:


msft_data = q.get("EOD/MSFT", start_date = "2010-01-01", end_date = "2019-01-01")


# In[ ]:


msft_data.head()


# In[ ]:


msft_data.info()


# In[ ]:


msft_data.describe()


# In[ ]:


msft_data.resample('M').mean()


# In[ ]:


msft_data.resample('M').mean().head()


# In[ ]:


import numpy as np


# In[ ]:


daily_close = msft_data[['Adj_Close']]


# In[ ]:


daily_close = daily_close.pct_change()


# In[ ]:


daily_return.fillna(0, inplace = True)


# In[ ]:


daily_return = daily_close.pct_change()


# In[ ]:


daily_return.fillna(0, inplace = True)


# In[ ]:


print(daily_return)


# In[ ]:


mdata = msft_data.resample('M').apply(lambda x:x[-1])


# In[ ]:


monthly_return = mdata.pct_change()


# In[ ]:


adj_pricesadj_price = msft_data['Adj_Close']


# In[ ]:


mav = adj_pricesadj_price.rolling(window=50).mean()


# In[ ]:


mav = adj_pricesadj_price.rolling(window=50).mean()


# In[ ]:


print(mav[-10:])


# In[ ]:


import matplotlib.pyplot as plt


# In[ ]:


import matplotlib.pyplot as pyplot


# In[ ]:


mav[-10:].plot()


# In[ ]:


adj_price.plot()


# In[ ]:


tsla_data = q.get("EOD/TSLA", start_date = "2010-01-01", end_date = "2020-01-01")


# In[ ]:





# In[ ]:





# In[1]:


import Quandl as q


# In[ ]:




