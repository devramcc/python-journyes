import numpy as np

def mean_naive(X):
    return np.mean(X, axis = 1, keepdims=True)

X = np.array([[0., 1., 1.], 
              [1., 2., 1.]])

print(mean_naive(X))