#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


# Importing the transactions data from the sales data

trans=pd.read_excel(r'C:\Users\Data\ecommerce_Sales_data.xlsx', "Transaction Values")
trans.head()


# In[3]:


# We will first check the datatype of the variables as we are dealing with date time 

trans.dtypes


# In[4]:


# Since time is an "object" type, we need to convert it into "datetime" format
import datetime

trans["time"]=pd.to_datetime(trans["time"], format="%H:%M:%S")


# In[5]:


# We will check the dtype for the time column again to see if it got converted

trans.dtypes


# In[6]:


trans["time"].dt.hour


# In[7]:


# Computing gap between the current and previous transaction

trans["gap"]=trans["Dates"].diff().dt.days
trans


# In[8]:


# Computing the Day, hour and week of transactions

trans["day"] = trans["Dates"].dt.day
trans["hour"]= trans["time"].dt.hour
trans["week"]= trans["Dates"].dt.week
trans      


# In[9]:


# We want to look at 2013 January data. First we need the Datetime index

trans.set_index("Dates", inplace=True)


# In[10]:


# the index is DateTimeIndex

trans.index


# In[11]:


trans


# In[12]:


trans["2013-01"]


# In[13]:


# Average value in Feb 2013

trans["2013-02"].value.mean()


# In[14]:


# Average value in the 1st week of 2013

trans["2013-01-01":"2013-01-07"].value.mean()


# In[15]:


# Plotting the sum of Day wise values 

trans["value"].resample("D").sum().plot(kind="line")


# In[16]:


# Plotting the hours

trans["hour"].plot()


# In[30]:


# Computing the ratio of transaction value and the gap between current and previous transaction

trans["ratio"]=round(trans["value"]/trans["gap"],2)
trans


# In[35]:


import seaborn as sns
import matplotlib.pyplot as plt


sns.scatterplot(x=trans["gap"], y=trans["value"])


# We can observe that it doesnt happen that if gap was higher people will do high amount of transaction to make average buying per day constant. That doesn't happen. More regular the customer , higher amount of purchases they make.

# In[20]:


# Importing Sales data
import pandas as pd

sales=pd.read_excel(r'C:\Users\Data\ecommerce_Sales_data.xlsx', "Sales data")
s1=pd.read_excel(r'C:\Users\Data\ecommerce_Sales_data.xlsx', "Sales data")
sales.head()


# In[21]:


# Creating a function which will impute all the missing values to be the median sales

sales.set_index("Product", inplace=True)


# In[22]:


sales.head()


# In[5]:


sales.dtypes


# In[23]:


# Since our df contains missing values, we need to impute the same. We can impute with Median but since there are blank values here
# we need to fill it out with np.nan for further calculations

import numpy as np

for i in sales.index:
    for j in sales.columns:
        if sales.loc[i,j]==" ":
            sales.loc[i,j]=np.nan
            



# In[24]:


sales


# In[25]:


sales.drop(columns="Category", inplace=True)


# In[26]:


# Median values are easily calculated in columns hence transposing the data sets to get the product data in columns

sales=sales.transpose()


# In[27]:


sales=sales.fillna(sales.median())
sales


# In[28]:


# getting the original df back 

sales1=sales.transpose()


# Missing values have been replaced by the median values

# In[29]:


sales1


# In[12]:


# Creating an input button which given a product name prints summary statistics for the same across all weeks. Summary statistics required here are mean, max, min, median, standard deviation.
# Input for the macro :product name

a=input()


sales[a].describe()


# In[30]:


# We need the Category column back for further analysis

s1.set_index("Product", inplace=True)


# In[31]:


d=s1["Category"]


# In[32]:


new=pd.concat([sales1,d], axis=1)


# In[33]:


new.head()


# In[44]:


# Creating a button which creates binary dummy variable for any given category for this particular data. 
# Input for the button would be the variable name


a=input()

dummy=pd.get_dummies(new[a], drop_first=True, prefix="rating")

dummy


# In[ ]:




