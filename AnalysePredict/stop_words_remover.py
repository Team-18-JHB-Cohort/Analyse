#!/usr/bin/env python
# coding: utf-8

# In[3]:


def stop_words_remover(df):
    
    #
    twitter_df['Without Stop Words'] = twitter_df['Tweets'].str.lower().str.split()
    
    #
    for i in range(twitter_df['Without Stop Words'].count()):
        for stop_word in stop_words_dict['stopwords']:
            if stop_word in twitter_df['Without Stop Words'][i]:
                twitter_df['Without Stop Words'][i].remove(stop_word)
            for item in (twitter_df['Without Stop Words'][i]):
                if str(item[0:5]) == "https":
                    twitter_df['Without Stop Words'][i].remove(item)       
            
    return twitter_df       


# In[ ]:




