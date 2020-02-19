#!/usr/bin/env python
# coding: utf-8

# In[ ]:


### START FUNCTION
def word_splitter(df):
    """
    Splits the sentences in a dataframe's column into a list of the separate words.

    Args:
        Adds new column to data.

    Returns:

        list: with only the date.

    Example:
            >>>Tweets and Date (Tweets Date
            @BongaDlulane Please send an email to mediades...
            2019-11-29)

            >>>Split Tweets [@bongadlulane, please, send, an, email, to, m...@saucy_mamiie Pls log a call on 0860037566
            2019-11-29 [@saucy_mamiie, pls, log, a, call, on, 0860037...]
    """
    #Create column, split and make strings lowercase.
    df['Split Tweets'] = df['Tweets'].str.lower().str.split() 
    return df

### END FUNCTION

