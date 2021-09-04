#!/usr/bin/env python
# coding: utf-8

# # importing pandas

# In[1]:


import pandas as pd


# In[2]:


names = ["id","title","year","rating","votes","length","genres"]


# In[3]:


data = pd.read_csv("imdb_top_10000.txt", "\t",names=names,index_col=0)


# In[4]:


data


# # Exploring Our Data

# In[5]:


data.head()


# In[6]:


data.tail()


# In[7]:


data.describe()


# In[8]:


data.info()


# # Exporting Data to .csv file

# In[9]:


data.to_csv('test.csv', header=True, index=True, sep=',')


# # Sorting Data by rating in ascending order

# In[10]:


data.sort_values(by="rating", ascending=False)


# # Creating Data Frames from Scratch

# In[11]:


sample_data = {
   'tv': [230.1, 44.5, 17.2],
   'radio': [37.8, 39.3, 45.9],
   'news': [69.2, 45.1, 69.3],
   'sales': [22.1, 10.4, 9.3]
}


# In[12]:


data2 = pd.DataFrame(sample_data)


# In[13]:


data2


# # Deleting Data Frame

# In[14]:


del data2


# # Selecting Data

# In[15]:


data['title']


# In[16]:


data[['title','rating']]


# # calculating mean,min and max of rating

# In[17]:


data['rating'].mean()


# In[18]:


data['rating'].max()


# In[19]:


data['rating'].min()


# # finding unique genres 

# In[20]:


data['genres'].unique()


# # finding no of movies based on rating

# In[21]:


data['rating'].value_counts()


# In[22]:


data['rating'].value_counts().sort_index()


# # Enabling Matplotlib

# In[23]:


get_ipython().run_line_magic('matplotlib', 'inline')


# # Ploting

# In[24]:


data.plot()


# In[25]:


data.plot(kind='scatter', x='rating', y='votes')


# # Import Seaborn

# In[26]:


import seaborn as sns


# # Seaborn pairplot 

# In[27]:


sns.pairplot(data)


# # importing statsmodels

# In[28]:


import statsmodels.api as sm


# In[29]:


results= sm.OLS(data["votes"], data["rating"]).fit()


# # displaying summary of OLS Regression

# In[30]:


results.summary()


# # Advanced Data Selection using Pandas

# In[31]:


data[data['year'] > 1995]


# In[32]:


data[(data['year'] > 1995) & (data['year'] < 2000)]


# # top rated movies from 1996 through 1999.

# In[33]:


data[(data['year'] > 1995) & (data['year'] < 2000)].sort_values(by='rating', ascending=False).head(10)


# # Pandas Groupby

# In[34]:


data.groupby(data['year'])['rating'].mean()


# In[35]:


data.groupby(data['year'])['rating'].max()


# # What was the highest scoring movie in 1996?

# In[72]:


titlereq = data[data['year']==1996].sort_values(by='rating', ascending=False).head(1).title


# In[73]:


titlereq


# # In what year was the highest rated movie of all time made?

# In[79]:


data[data['rating'] == data['rating'].max()]


# # What five movies have the most votes ever?

# In[80]:


data.sort_values(by='votes', ascending=False).head()


# # What year in the 1960s had the highest average movie rating?

# In[81]:


data[(data['year'] >= 1960) & (data['year'] <= 1970)].groupby(data['year'])['rating'].mean()


# # deleting years in title

# In[82]:


data['formatted title'] = data['title'].str[:-7] 


# In[84]:


data


# # Let's keep cleaning up our data set

# In[103]:


data['formated length']=data['length'].str.split().str.get(0).astype('int') 


# In[104]:


data


# # drawing pairplots again

# In[105]:


sns.pairplot(data)


# In[ ]:




