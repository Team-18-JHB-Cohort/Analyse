#!/usr/bin/env python
# coding: utf-8

# In[3]:

 """
   Should split string in a list in rows
   Should remove stop_words in the dictionary from the dataframe
   Should create a new column labeled "without_stop_words"
    
    Args:
        DataFrame
    
    Returns:
        a culumn labeled "Without_Stop_words" with stop words removed.
    
     
    """

def stop_words_remover(df):
    
    #
    twitter_df['Without Stop Words'] = twitter_df['Tweets'].str.lower().str.split()
    
    #
    for i in range(twitter_df['Without Stop Words'].count()):
        for stop_word in stop_words_dict['stopwords']:
            if stop_word in twitter_df['Without Stop Words'][i]:
                twitter_df['Without Stop Words'][i].remove(stop_word)
                   
            
    return twitter_df       


# In[ ]:




