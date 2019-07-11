#!/usr/bin/env python
# coding: utf-8

# In[123]:


import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt




#thuis is for apple and orange
features=[ [100,0], [120,0],[130,1],[150,1]   ]
#here 0 means for smooth and 1 for bumpy




label=['apple','apple','orange','orange']


# In[6]:


#callling Decisiontreeclassifier
clf=DecisionTreeClassifier()


# In[12]:


#now time for training data
trained=clf.fit(features,label)


# In[128]:


#now predicting
trained.predict([[10,1]])


# In[ ]:





# In[ ]:





# In[ ]:




