#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd


# In[6]:


data=pd.read_csv("spam.csv", encoding="latin-1")


# In[7]:


data.head(5)


# In[8]:


data.columns


# In[9]:


data.drop(['Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4'], axis=1, inplace=True)


# In[10]:


data.head()


# In[11]:


data['v1']=data["v1"].map({'ham':0, 'spam':1})


# In[12]:


data.head()


# In[20]:


from sklearn.feature_extraction.text import CountVectorizer


# In[21]:


cv=CountVectorizer()


# In[22]:


x=data['v2']
y=data['v1']


# In[23]:


x.shape


# In[24]:


y.shape


# In[25]:


x=cv.fit_transform(x)


# In[26]:


x


# In[27]:


from sklearn.model_selection import train_test_split


# In[30]:


x_train, x_test, y_train, y_test=train_test_split(x, y, test_size=0.2)


# In[32]:


x_train.shape


# In[34]:


from sklearn.naive_bayes import MultinomialNB


# In[35]:


model=MultinomialNB()


# In[36]:


model.fit(x_train, y_train)


# In[37]:


model.score(x_test, y_test)


# In[38]:


result=model.score(x_test, y_test)


# In[39]:


result=result*100


# In[40]:


result


# In[41]:


import pickle


# In[42]:


pickle.dump(model, open("spam.pkl","wb"))


# In[43]:


pickle.dump(cv, open("vectorizer.pkl","wb"))


# In[44]:


clf=pickle.load(open("spam.pkl","rb"))


# In[45]:


clf


# In[47]:


msg="Hello there"
data=[msg]
vect=cv.transform(data).toarray()
result=model.predict(vect)
print(result)


# In[ ]:




