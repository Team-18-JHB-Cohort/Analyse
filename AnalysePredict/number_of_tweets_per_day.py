#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def number_of_tweets_per_day(df):
    """
    Returns a new dataframe, grouped by day, with the number of tweets for that day
    
    Args:
        Creates new dataframe
    
    Returns:
        Dataframe with two columns, Date and count of the Tweets for the date.
    
    Example:
        >>> Tweets and Date :@BongaDlulane Please send an email to mediades...2019-11-29 12:50:54
        
        >>> Date and Tweets :2019-11-20 18

    """
    #Create open list for return result.
    dates_table = {}
    
    #Create dates list with list comprehension to select the first ten characters of the dataframe.
    dates = [x[:10] for x in df['Date']]
    
    #For loop with if statement to select item in dates and if statement to count frequency of each item in dates_table.
    for item in dates:
        
        if item in dates_table:
            dates_table[item] += 1 
        else:
            dates_table[item] = 1  
            
    new_dataframe = pd.DataFrame(sorted(dates_table.items()))
    
    new_dataframe.columns = ['Date', 'Tweets']
    
    new_dataframe.set_index('Date', inplace=True)
            
    return new_dataframe

