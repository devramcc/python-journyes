import numpy as np
def find_angle(A, x, y):
    """Compute the angle"""
    inner_prod = x.T @ A @ y
    # Fill in the expression for norm_x and norm_y below
    norm_x = np.sqrt(x.T * A * x)
    norm_y = np.sqrt(y.T * A * y)
    alpha = inner_prod/(norm_x*norm_y)
    #alpha = np.clip(alpha, -1, 1)
    angle = np.arccos(alpha)
    return np.round(angle, 2)

A = np.array([1, 1, 1])
x = np.array([2, -1, 0])
y = np.array([[1, 0, 0],
              [0, 2, -1],
              [0, -1, 3]])

#find_angle(A, x, y)
print(x.T @ A @ y)