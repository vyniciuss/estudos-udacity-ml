#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    """
    Solucao 1
    cleaned_data = []
    errors = []

    for i in range(len(predictions)):
        errors.append(net_worths[i] - predictions[i])

    s_errors = sorted(errors)
    start = int(len(errors) * 0.1)

    for i in range(start, len(errors)):
        index = errors.index(s_errors[i])
        cleaned_data.append((ages[index], net_worths[index], errors[index]))

    return cleaned_data
    """
    ## solucao 2
    ### your code goes here
    import numpy as np
    #We get a matrix of len (ages) columns by 3 rows
    b = np.reshape([ages, net_worths, (predictions-net_worths)**2],(3,len(ages)))
    #We convert the previous matrix into its transpose. In this way we obtain a matrix of len (ages) rows by 3 columns
    c = b.reshape(3,len(ages)).T
    #Finally, we eliminate 10% of rows with the greatest error from the matrix
    while(len(c) > int(len(ages) * 0.9)):
        c = np.delete(c, c.argmax(axis = 0)[2], axis = 0)
    return c

"""

"""