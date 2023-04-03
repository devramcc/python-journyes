import numpy as np

x = np.array([2, 3])
y = np.array([4, 1])
A = np.array([[1, -0.5],
             [-0.5, 1]])
distance = x - y
result = distance.T * A * distance
print(result)