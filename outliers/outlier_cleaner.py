#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """

    from operator import itemgetter
    cleaned_data = []
    error = []
    for i in range(0, len(ages)):
        cleaned_data.append((ages[i], net_worths[i], abs(net_worths[i] - predictions[i])))
    ### your code goes here
    cleaned_data.sort(key = itemgetter(2))
    # print(cleaned_data)
    cleaned_data = cleaned_data[:int(.9*len(cleaned_data))]  
     
    return cleaned_data

