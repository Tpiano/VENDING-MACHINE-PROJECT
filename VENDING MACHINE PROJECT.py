#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


df = pd.read_csv('C:/Users/USER/Downloads/vending_machine_sales.csv')


# In[3]:


df.head()


# In[4]:


to_drop =['Device ID',
        'TransDate',
        'RCoil',
        'MCoil',
        'Prcd Date']
df.drop(to_drop, inplace=True, axis=1)


# In[5]:


df.info()


# In[6]:


df.isna().sum()


# In[7]:


Category_mode = df['Category'].mode()
Product_mode = df['Product'].mode()
Mprice_mean = df['MPrice'].mean()

print(Category_mode,
Product_mode, 
Mprice_mean)


# In[8]:


df['Category'] = df['Category'].fillna(df['Category'].mode()[0]) 
df['Product'] = df['Product'].fillna(df['Product'].mode()[0]) 
df['MPrice'] = df['MPrice'].fillna(df['MPrice'].mean()) 


# In[9]:


df.isna().sum()


# In[10]:


df.describe()


# In[11]:


max_Transanted_products = df.sort_values(by='MQty', ascending=False)
max_Transanted_products['Product' ].head(10)


# In[12]:


category = df.groupby('Category').count()


# In[13]:


category = df.groupby('Category').count()
plt.pie(category['TransTotal'], labels = category.index.values)
plt.title('HIGHEST SOLD CATEGORY')
plt.show()


# In[14]:


status = df.groupby('Status').count()
plt.bar(status.index.values, status['TransTotal'])
plt.title('')
plt.show()


Status_Table = df.groupby('Status')
Status_Table['Status'].count()


# In[15]:


Type = df.groupby('Type').count()
plt.bar(Type.index.values, Type['TransTotal'])
plt.title('MODE OF TRANSACTION')
plt.show()


# In[16]:


Location = df.groupby('Location').count()
plt.pie(Location['TransTotal'], labels = Location.index.values)
plt.title('LOCATION WITH HIGHEST SALE')
plt.show()


# In[17]:


Machine = df.groupby('Machine').count()
plt.bar(Machine.index.values, Machine['TransTotal'])
# plt.bar(orientation='horizontal')
plt.title('MACHINE WITH THE HIGHEST SALES')
plt.xticks(rotation=75)
plt.show()

