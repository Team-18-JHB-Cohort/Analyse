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
        items_length, sum_of_items  = 0, 0

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

        return {'mean':  float('%.2f' % mean), 'median':  float('%.2f' % median) , 'variance':  float('%.2f' % variance),
                'standard deviation':  float('%.2f' % standard_deviation) , 'min':  float('%.2f' % minimum) , 'max':  float('%.2f' % maximum)}

    except TypeError:
        return 'Enter a valid argument: argument must be a list of --> int or floats'  
### END FUNCTION
