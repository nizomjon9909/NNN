#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt
plt.show()


# In[10]:


data= pd.read_csv("top50.csv") 


# In[13]:


data.columns


# In[17]:


data.head(10)


# In[14]:


data.isnull().sum()


# In[16]:


data.info()


# In[19]:


data.tail(10)


# In[20]:


data.shape


# In[22]:


sns.heatmap(data.isnull())


# In[24]:


data.describe()


# In[25]:


data.columns


# In[44]:


data[data["Popularity"]>=90]["Track.Name"]


# In[ ]:





# In[ ]:





# In[ ]:




