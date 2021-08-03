#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import quandl as q


# In[2]:


q.ApiConfig.api_key = "SoUsdH6em6gXrDiUnqzv"


# In[4]:


msft_data = q.get("EOD/MSFT", start_date = "2010-01-01", end_date = "2019-01-01")


# In[5]:


msft_data.head()


# In[6]:


msft_data.info()


# In[7]:


msft_data.describe()


# In[8]:


msft_data.resample('M').mean()


# In[9]:


msft_data.resample('M').mean().head()


# In[10]:


import numpy as np


# In[ ]:


daily_close = msft_data

