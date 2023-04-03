import numpy as np

# GRADED FUNCTION: DO NOT EDIT THIS LINE
def cov_naive(X):
    """Compute the sample covariance for a dataset by iterating over the dataset.
    
    Args:
        X: `ndarray` of shape (N, D) representing the dataset. 
        N is the size of the dataset (the number of data points) 
        and D is the dimensionality of each data point.
    Returns:
        ndarray: ndarray with shape (D, D), the sample covariance of the dataset `X`.
    """
    # YOUR CODE HERE
    ### Uncomment and edit the code below
    #N, D = X.shape
#     ### Edit the code below to compute the covariance matrix by iterating over the dataset.
    covariance = np.cov(X, rowvar=False, bias=True)
#     ### Update covariance
    
#     ###
    return covariance

X = np.array([[0., 1.], 
              [0., 1.],
              [0., 1.]])


print(cov_naive(X))