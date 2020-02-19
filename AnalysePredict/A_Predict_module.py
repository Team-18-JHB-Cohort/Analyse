### START FUNCTION
def dictionary_of_metrics(items):

    """
    Usage:
        Calculates the aggregates of a list

    Args:
        list: (containing non-string items)

    Returns:
        dict: {mean, median, variance, standard deviation, min, max} all rounded to 2 decimal places

    Example:
        >>> dictionary_of_metrics([1, 2, 3, 4])
        {'mean': 2.5, 'median': 2.5, 'variance': 1.25,
         'standard deviation': 1.11, 'min': 1,
         'max': 4}
    """
    try:
        items_length = 0
        sum_of_items = 0

        for item in items:
            sum_of_items += item  # Calculating the sum of the items in a list
            items_length += 1  # Calculating the length of a list

        # Sorting out the list
        for i in range(0, items_length):
            for j in range(1, items_length):
                if items[j - 1] > items[j]:
                    (items[j - 1], items[j]) = (items[j], items[j - 1])

        mean = (sum_of_items / items_length)   # Calculating the mean

        if items_length % 2 == 0:
            median1 = items[items_length // 2]  # finding the average of the two middlemost terms provided the items_length is even
            median2 = items[items_length // 2 - 1]
            median = (median1 + median2) / 2
        else:
            median = items[items_length // 2]

        variance = 0
        for i in range(items_length):
            variance += (items[i] - mean) ** 2 / (items_length - 1)

        standard_deviation = (variance ** 0.5)

        minimum = items[0]

        maximum = items[-1]

        return {'mean':  float('%.2f' % mean), 'median':  float('%.2f' % median) , 'var':  float('%.2f' % variance),
                'std':  float('%.2f' % standard_deviation) , 'min':  float('%.2f' % minimum) , 'max':  float('%.2f' % maximum)}

    except TypeError:
        return 'Enter a valid argument: argument must be a list of --> int or floats'


### START FUNCTION
def five_num_summary(items):
    from numpy import percentile

    """
    Calculates the five number summary

    Args:
        list (containing non-string items)

    Returns:
        dict: {max, median, min, q1, q3} all rounded to 2 decimal places

    Example:
        >>> five_num_summ([1, 2, 3, 4, 5])
        {'max': 5.0, 'median': 3.0, 'min': 1.0, 'q1': 2.0, 'q3': 4.0}

    """
    try:
        items_length = 0
        sum_of_items = 0

        for item in items:
            sum_of_items += item   # Calculating the sum of the items in a list
            items_length += 1  # Calculating the length of a list

        # Sorting out the list
        for i in range(items_length):
            for j in range(1,items_length):
                if items[j-1] > items[j]:
                    (items[j-1], items[j]) = (items[j], items[j-1])

        max_num = items[-1]
        min_num = items[0]
        quartiles = percentile(items, [25, 50, 75])

        return {'max':float('%.2f' % max_num), 'median':float('%.2f' % quartiles[1]), 'min':float('%.2f' % min_num), 'q1':float('%.2f' % quartiles[0]),'q3':float('%.2f' % quartiles[2])}

    except TypeError:
        return 'Enter a valid argument: argument must be a list of --> int or floats'


### END FUNCTION



### START FUNCTION
def date_parser(list_dates):
    """
    takes a list of datetime strings and converts it into a list of strings with only the date

    Args:
        list (containing datetime strings)

    Returns:
        list: with only the date

    Example:
        >>>date_parser(['2019-11-29 12:50:54',
                        '2019-11-29 12:46:53'])
        >>>['2019-11-29,
            '2019-11-29']
    """
    new_date_list = []
    for date_string in list_dates:
        new_date_list += (date_string.split(' '))

    return new_date_list[::2]
### END FUNCTION


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

    mun_dict = {
    '@CityofCTAlerts' : 'Cape Town',
    '@CityPowerJhb' : 'Johannesburg',
    '@eThekwiniM' : 'eThekwini' ,
    '@EMMInfo' : 'Ekurhuleni',
    '@centlecutility' : 'Mangaung',
    '@NMBmunicipality' : 'Nelson Mandela Bay',
    '@CityTshwane' : 'Tshwane'}

    for i in range(0, len(df['Tweets'])):
        for key in mun_dict.keys():
            if key in df['Tweets'][i]:
                df['municipality'][i] = mun_dict[key]
    main_list = []

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



### START FUNCTION
def number_of_tweets_per_day(df):
    """
    Returns a new dataframe, grouped by day, with the number of tweets for that day
    
    Args:
        Creates new dataframe
    
    Returns:
        Dataframe with two columns, Date and count of the Tweets for the date.
    
    Example:
        >>> Tweets and Date :[@BongaDlulane Please send an email to mediades...] [2019-11-29 12:50:54]
        
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

### END FUNCTION


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



### START FUNCTION
def stop_words_remover(df):    
    """
    Should split string in a list in rows
    Should remove stop_words in the dictionary from the dataframe
    Should create a new column labeled "without_stop_words"
    
    Args:
        DataFrame
    
    Returns:
        a column labeled "Without_Stop_words" with stop words removed.
    """ 
    
    df['Without Stop Words'] = df['Tweets'].str.lower().str.split()
    main_list = []
    #
    for i in range(0, len(df['Without Stop Words'])):
        new_list = []
        for entry in df['Without Stop Words'][i]:
            if entry not in stop_words_dict['stopwords']:
                new_list.append(entry)

        main_list.append(new_list)
    new_data = pd.Series(main_list)
    df['Without Stop Words'] = new_data
    return df

### END FUNCTION
