import numpy as np
# the matrix A defines the inner product
A = np.array([[1, -1/2],[-1/2,5]])
x = np.array([0,-1])
y = np.array([1,1])

def find_angle(A, x, y):
    """Compute the angle"""
    inner_prod = x.T @ A @ y
    # Fill in the expression for norm_x and norm_y below
    norm_x = np.sqrt(x.T @ A @ x)
    norm_y = np.sqrt(y.T @ A @ y)
    alpha = inner_prod/(norm_x*norm_y)
    #alpha = np.clip(alpha, -1, 1)
    angle = np.arccos(alpha)
    return np.round(angle, 2) 

find_angle(A, x, y)

A = np.array([[2, -1],[-1,4]])
x = np.array([1,1])
y = np.array([-1,1])

def find_angle(A, x, y):
    """Compute the angle"""
    inner_prod = x.T @ A @ y
    # Fill in the expression for norm_x and norm_y below
    norm_x = np.sqrt(x.T @ A @ x)
    norm_y = np.sqrt(y.T @ A @ y)
    alpha = inner_prod/(norm_x*norm_y)
    #alpha = np.clip(alpha, -1, 1)
    angle = np.arccos(alpha)
    return np.round(angle, 2) 

print(find_angle(A, x, y))

A = np.array([[1, 0],[0,5]])
x = np.array([1,1])
y = np.array([1,-1])

def find_angle(A, x, y):
    """Compute the angle"""
    inner_prod = x.T @ A @ y
    # Fill in the expression for norm_x and norm_y below
    norm_x = np.sqrt(x.T @ A @ x)
    norm_y = np.sqrt(y.T @ A @ y)
    alpha = inner_prod/(norm_x*norm_y)
    #alpha = np.clip(alpha, -1, 1)
    angle = np.arccos(alpha)
    return np.round(angle, 2) 

print(find_angle(A, x, y))


