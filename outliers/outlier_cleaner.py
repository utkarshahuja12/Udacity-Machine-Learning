#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []
    ### your code goes here
    error = []
    for i in range(len(predictions)):
        error.append([predictions[i][0] - net_worths[i][0], i])
    error.sort()
    numberOfdata = 0.9 * len(predictions)
    numberOfdata = int(numberOfdata)
    for i in range(numberOfdata):
        cleaned_data.append((ages[error[i][1]][0], net_worths[error[i][1]][0], error[i][0]))
    return cleaned_data

#outlierCleaner([[1.00], [2.00],[3.00]], [[24],[56], [78]], [[67.00],[56.00],[89.00]])
