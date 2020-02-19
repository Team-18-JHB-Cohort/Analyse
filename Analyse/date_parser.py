def date_parser(dates):
    """
    This function takes a list containing the date and time strings and 
    splits them, then only returns the list of dates without the time.

    for example:
         
    dates = ['2019-11-29 12:50:54',
         '2019-11-29 12:46:53',
         '2019-11-29 12:46:10',
         '2019-11-29 12:33:36',
         '2019-11-29 12:17:43',
         '2019-11-29 11:28:40']

    date_parser(dates) == ['2019-11-29',
                       '2019-11-29',
                       '2019-11-29',
                       '2019-11-29',
                       '2019-11-29',
                       '2019-11-29']
    """
    date_only = []
    for item in dates:
        date_only.append(item.split(" ")[0])
    
    return date_only
