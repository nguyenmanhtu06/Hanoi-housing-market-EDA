#!/usr/bin/env python
# coding: utf-8

# In[18]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#import data, prefix the string with r (to produce a raw string)
nhahn = pd.read_csv(r"C:\Users\Acer\Desktop\HN\VN_housing_dataset.csv")
#drop unnamed column
nhahn.drop('Unnamed: 0', axis=1,inplace=True)
nhahn = nhahn.dropna(subset=['Địa chỉ','Số phòng ngủ','Diện tích','Giá/m2','Loại hình nhà ở'])
nhahn


# In[19]:


nhahn['Đơn giá'] = (nhahn['Giá/m2'].str.split(' ',expand=True))[0]
nhahn['Đơn giá'] = nhahn['Đơn giá'].str.replace(',','.')
nhahn


# In[20]:


nhahn.drop(nhahn[nhahn['Đơn giá'] == '2.222.22220022'].index, inplace = True)
nhahn.drop(nhahn[nhahn['Đơn giá'] == '728.000.00728'].index, inplace = True)
nhahn


# In[21]:


nhahn['Đơn giá'] = nhahn['Đơn giá'].apply(lambda x: float(x))
nhahn


# In[22]:


nhahn['Diện tích đất'] = (nhahn['Diện tích'].str.split(' ',expand=True))[0]
nhahn['Diện tích đất'] = nhahn['Diện tích đất'].apply(lambda x: float(x))
nhahn


# In[23]:


nhahn['Giá'] = (nhahn['Diện tích đất'] * nhahn['Đơn giá']) / 1000
nhahn


# In[24]:


nhahn.drop(['Diện tích', 'Giá/m2'], axis=1, inplace=True)
nhahn


# In[25]:


nhahnv1 = 'nhahn.xlsx'
  

nhahn.to_excel(nhahnv1)


# In[ ]:




