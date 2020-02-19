#!/usr/bin/env python
# coding: utf-8

# In[ ]:


### START FUNCTION
def extract_municipality_hashtags(df):
    """
    Returns a new dataframe with two new columns municipality and hashtags.
    
    Args:
        Create new dataframe.
      
    Return:
        Dataframe with two columns, municipality that reflects the municipality and hashtags separately.
    
    """
    df['municipality'] = np.nan
    df['hashtags'] = np.nan
    
    #Creating a column with all the mentioned municipalities.
    for i in range(0, len(df['Tweets'])):
        for key in mun_dict.keys():
            if key in df['Tweets'][i]:
                df['municipality'][i] = mun_dict[key]
    main_list = []         
    
    #Create column with all hashtags.
    for i in range(0, len(df['Tweets'])):
        new_list = [] 
        for entry in twitter_df['Tweets'][i].split():
            if entry[0] == '#':
                new_list.append(entry.lower())
                
        if len(new_list) < 1:   
            main_list.append(np.nan) 
        else:
            main_list.append(new_list)
        
    new_data = pd.Series(main_list)
    df['hashtags'] = new_data
    
    return df

### END FUNCTION

