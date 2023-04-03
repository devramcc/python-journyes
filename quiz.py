import numpy as np

x = np.array([1, -1, 3])
A = np.array([[2, 1, 0],
              [1, 2, -1],
              [0, -1, 2]])

result = x.T @ A @ x
print("no_1", result)

x = np.array([0.5, -1, -0.5])
y = np.array([0, 1, 0])
A = np.array([[2, 1, 0],
              [1, 2, -1],
              [0, -1, 2]])

result = x.T @ A @ y
print("no_2", result)

x = np.array([4, 2, 1])
y = np.array([0, 1, 0])
A = np.array([[2, 1, 0],
              [1, 2, -1],
              [0, -1, 2]])

result = x.T @ A @ y
print("no_4", result)

x = np.array([-1, -1, -1])
A = np.array([[1, 0, 0],
              [0, 1, 0],
              [0, 0, 1]])

result = x.T @ A @ x
print("no_5", result)

x = np.array([-1, 1])
A = np.array([[5, -1],
              [-1, 5]])
A = A * 1/2

result = x.T @ A @ x
print("no_3", result)