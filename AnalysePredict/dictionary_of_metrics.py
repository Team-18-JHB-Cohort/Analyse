def dictionary_of_metrics(items):

    """
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
        for j in range(1, items_length):
            if items[j - 1] > items[j]:
                (items[j - 1], items[j]) = (items[j], items[j - 1])

        mean = int((sum_of_items / items_length) * 100) / 100  # Calculating the mean

        if items_length % 2 == 0:
            median1 = items[
                items_length // 2]  # finding the average of the two middlemost terms provided the num_item is even
            median2 = items[items_length // 2 - 1]
            median = int(((median1 + median2) / 2) * 100) / 100
        else:
            median = int(items[items_length // 2] * 100) / 100

        variance = 0
        for i in range(items_length):
            variance += (items[i] - mean) ** 2 / (items_length - 1)

        standard_deviation = int((variance ** 0.5) * 100) / 100

        minimum = int(items[0] * 100) / 100

        maximum = int(items[-1] * 100) / 100

        return {'mean': mean, 'median': median, 'variance': int(variance * 100) / 100,
                'standard deviation': standard_deviation, 'min': minimum, 'max': maximum}

    except TypeError:
        return 'Enter a valid argument: argument must be a list of --> int or floats'
