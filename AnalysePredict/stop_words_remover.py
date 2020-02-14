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
        a column labeled "Without_Stop_words" with stop words removed.
    
     
    """

def stop_words_remover(df):
    
    #Split string into list and create new column
    df['Without Stop Words'] = df['Tweets'].str.lower().str.split()
    
    #Remove stopwords from the new column
    for i in range(df['Without Stop Words'].count()):
        for stop_word in stop_words_dict['stopwords']:
            if stop_word in df['Without Stop Words'][i]:
                df['Without Stop Words'][i].remove(stop_word)
                   
            
    return df       


# In[ ]:




