def date_parser(dates):
    date_only = []
    for item in dates:
        date_only.append(item.split(" ")[0])
    
    return date_only