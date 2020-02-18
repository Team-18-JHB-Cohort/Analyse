def stop_words_remover(df):
    
    #
    twitter_df['Without Stop Words'] = twitter_df['Tweets'].str.lower().str.split()
    
    #
    for i in range(twitter_df['Without Stop Words'].count()):
        for entry in df['Without Stop Words'][i]:
            if entry not in stop_words_dict['stopwords']:
                new_list.append(entry)
               
        main_list.append(new_list)
    new_data = pd.Series(main_list)
    df['Without Stop Words'] = new_data 
    return twitter_df       






