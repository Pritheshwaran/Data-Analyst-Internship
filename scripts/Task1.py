#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import nltk
from nltk.corpus import stopwords
import string


# In[8]:


apps_df = pd.read_csv("Play Store Data.csv")
reviews_df = pd.read_csv("User Reviews.csv")


# In[9]:


health_apps = apps_df[apps_df["Category"] == "HEALTH_AND_FITNESS"]["App"]


# In[10]:


health_reviews = reviews_df[reviews_df["App"].isin(health_apps)]


# In[11]:


positive_reviews = health_reviews[health_reviews["Sentiment"] == "Positive"]["Translated_Review"].dropna()
nltk.download("stopwords")
stop_words = set(stopwords.words("english")) | set(string.punctuation)


# In[12]:


words = " ".join(positive_reviews).lower().split()
filtered_words = [word for word in words if word not in stop_words]
wordcloud = WordCloud(width=800, height=400, background_color="white").generate(" ".join(filtered_words))


# In[13]:


plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()


# In[ ]:




