
def stop_words_remover(df):
  """
  Usage:
   Should split string in a list in rows
   Should remove stop_words in the dictionary from the dataframe
   Should create a new column labeled "without_stop_words"
    
    Args:
        DataFrame
    Returns:
        a column labeled "Without_Stop_words" with stop words removed.
   """
    #split string and create new column.
    df['Without Stop Words'] = df['Tweets'].str.lower().str.split()
    main_list = []
    #removes words from the 'Tweets' column and deposits them into a new column called 'Without Stop Words'.
    for i in range(twitter_df['Without Stop Words'].count()):
        for entry in df['Without Stop Words'][i]:
            if entry not in stop_words_dict['stopwords']:
                new_list.append(entry)
               
        main_list.append(new_list)
    new_data = pd.Series(main_list)
    df['Without Stop Words'] = new_data 
    return twitter_df       

   
    
     
     








