### START FUNCTION
def five_num_summary(items):
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
    quartiles = np.percentile(items, [25, 50, 75])
    # calculate min/max
    data_min, data_max = min(items), max(items)

    return {'max':float('%.2f' % max_num), 'median':float('%.2f' % median(items)), 'min':float('%.2f' % min_num), 'q1':float('%.2f' % q1),'q3':float('%.2f' % q3)}    
### END FUNCTION
