#!/usr/bin/env python
# coding: utf-8

# In[78]:


from sklearn import datasets
from sklearn.tree import DecisionTreeClassifier
import time
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score


# In[5]:


for i in dir(datasets):
 print(i)
 time.sleep(2)


# In[6]:


[i for i in dir(datasets) if 'load' in i]


# In[8]:


from sklearn.datasets import load_iris


# In[15]:


#loading iris data only
iris=load_iris()


# In[16] :


dir(iris)


# In[17]:


iris.DESCR


# In[20]:


iris.feature_names


# In[21]:


#labels or answers
iris.target_names


# In[22]:


#actual data with attribute
features=iris.data


# In[23]:


features


# In[25]:


features.shape


# In[26]:


type(features)


# In[27]:


features[ 3,1        ]


# In[30]:


#now time for label data that will be exactly same as no of feature data
label=iris.target


# In[31]:


label.shape


# In[33]:


sl=features[0:,0]


# In[34]:


sw=features[0:,1]


# In[41]:


plt.xlabel("Sepal_length")
plt.ylabel("sepal_width")
plt.scatter(sl,sw,label="sepal_data")
plt.scatter(features[0:,2],features[0:,3],label="petel_data")
plt.legend()


# In[42]:


#now sepersting data into two cat.
#1--->training data
#testing data
from sklearn.model_selection import train_test_split


# In[45]:


train_data,test_data,label_train,label_test=train_test_split(features,label,test_size=0.1)


# In[46]:


clf=DecisionTreeClassifier()


# In[48]:


trained=clf.fit(train_data,label_train)


# In[49]:


predicted_flower=trained.predict(test_data)


# In[50]:


predicted_flower


# In[74]:


label_test


# In[76]:


accuracy_score(label_test,predicted_flower)


# In[ ]:




