#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pandas as pd


# In[2]:


dataset = pd.read_csv("haberman.csv")


# In[3]:


dataset.head()


# In[4]:


dataset.shape


# In[5]:


dataset.info()


# In[6]:


print(dataset.columns)


# In[19]:


import matplotlib.pyplot as plt
dataset.plot(kind='scatter', x='Axillary_Nodes', y='Age') 
plt.title("Age vs  Axillary_Nodes")
plt.xlabel("Age")
plt.ylabel("Axillary_Nodes")
plt.grid()
plt.show()


# In[20]:


import seaborn as sns
sns.FacetGrid(dataset, hue='Surival_status', height=4).map(plt.scatter, 'Axillary_Nodes', 'Age').add_legend()
plt.title("Age vs  Axillary_Nodes")
plt.show()


# In[22]:


import plotly.express as px
px.scatter_3d(dataset, x="Age", y="Operation_Age", z="Axillary_Nodes", color="Surival_status")


# In[28]:


sns.pairplot(dataset, hue="Surival_status", height=3, vars=["Age","Operation_Age", "Axillary_Nodes"])
plt.show()


# In[ ]:




