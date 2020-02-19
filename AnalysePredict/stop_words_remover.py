
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
  stop_words_dict = {'stopwords':['where', 'done', 'if', 'before', 'll', 'very', 'keep', 'something', 'nothing', 'thereupon', 'may',
                                  'why', '’s', 'therefore', 'you', 'with', 'towards', 'make', 'really', 'few', 'former', 'during',
                                  'mine', 'do', 'would', 'of', 'off', 'six', 'yourself', 'becoming', 'through', 'seeming', 'hence',
                                  'us', 'anywhere', 'regarding', 'whole', 'down', 'seem', 'whereas', 'to', 'their', 'various', 
                                  'thereafter', '‘d', 'above', 'put', 'sometime', 'moreover', 'whoever', 'although', 'at', 'four', 
                                  'each', 'among', 'whatever', 'any', 'anyhow', 'herein', 'become', 'last', 'between', 'still', 'was', 
                                  'almost', 'twelve', 'used', 'who', 'go', 'not', 'enough', 'well', '’ve', 'might', 'see', 'whose', 
                                  'everywhere', 'yourselves', 'across', 'myself', 'further', 'did', 'then', 'is', 'except', 'up', 
                                  'take', 'became', 'however', 'many', 'thence', 'onto', '‘m', 'my', 'own', 'must', 'wherein', 
                                  'elsewhere', 'behind', 'becomes', 'alone', 'due', 'being', 'neither', 'a', 'over', 'beside', 
                                  'fifteen', 'meanwhile', 'upon', 'next', 'forty', 'what', 'less', 'and', 'please', 'toward', 'about', 
                                  'below', 'hereafter', 'whether', 'yet', 'nor', 'against', 'whereupon', 'top', 'first', 'three', 
                                  'show', 'per', 'five', 'two', 'ourselves', 'whenever', 'get', 'thereby', 'noone', 'had', 'now', 
                                  'everyone', 'everything', 'nowhere', 'ca', 'though', 'least', 'so', 'both', 'otherwise', 'whereby', 
                                  'unless', 'somewhere', 'give', 'formerly', '’d', 'under', 'while', 'empty', 'doing', 'besides', 
                                  'thus', 'this', 'anyone', 'its', 'after', 'bottom', 'call', 'n’t', 'name', 'even', 'eleven', 'by', 
                                  'from', 'when', 'or', 'anyway', 'how', 'the', 'all', 'much', 'another', 'since', 'hundred', 
                                  'serious', '‘ve', 'ever', 'out', 'full', 'themselves', 'been', 'in', "'d", 'wherever', 'part', 
                                  'someone', 'therein', 'can', 'seemed', 'hereby', 'others', "'s", "'re", 'most', 'one', "n't", 
                                  'into', 'some', 'will', 'these', 'twenty', 'here', 'as', 'nobody', 'also', 'along', 'than', 
                                  'anything', 'he', 'there', 'does', 'we', '’ll', 'latterly', 'are', 'ten', 'hers', 'should', 'they', 
                                  '‘s', 'either', 'am', 'be', 'perhaps', '’re', 'only', 'namely', 'sixty', 'made', "'m", 'always', 
                                  'those', 'have', 'again', 'her', 'once', 'ours', 'herself', 'else', 'has', 'nine', 'more', 
                                  'sometimes', 'your', 'yours', 'that', 'around', 'his', 'indeed', 'mostly', 'cannot', '‘ll', 'too', 
                                  'seems', '’m', 'himself', 'latter', 'whither', 'amount', 'other', 'nevertheless', 'whom', 'for', 
                                  'somehow', 'beforehand', 'just', 'an', 'beyond', 'amongst', 'none', "'ve", 'say', 'via', 'but', 
                                  'often', 're', 'our', 'because', 'rather', 'using', 'without', 'throughout', 'on', 'she', 'never', 
                                  'eight', 'no', 'hereupon', 'them', 'whereafter', 'quite', 'which', 'move', 'thru', 'until', 
                                  'afterwards', 'fifty', 'i', 'itself', 'n‘t', 'him', 'could', 'front', 'within', '‘re', 'back', 
                                  'such', 'already', 'several', 'side', 'whence', 'me', 'same', 'were', 'it', 'every', 'third', 
                                  'together']}
    #split string and create new column.

    df['Without Stop Words'] = df['Tweets'].str.lower().str.split()
    main_list = []
    #removes words from the 'Tweets' column and deposits them into a new column called 'Without Stop Words'.
    for i in range(df['Without Stop Words'].count()):
        for entry in df['Without Stop Words'][i]:
            if entry not in stop_words_dict['stopwords']:
                new_list.append(entry)
               
        main_list.append(new_list)
    new_data = pd.Series(main_list)
    df['Without Stop Words'] = new_data 
    return df       


   
    
     
     








