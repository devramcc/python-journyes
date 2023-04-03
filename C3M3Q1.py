import numpy as np

#NO 1
b = np.array([[1,2,2]])

print(b.shape)

print("this is multipication: ")
print( b * b.T)
print("this is dot_product:", b @ b.T)

#NO 2
b = np.array([[3,0,4]])
P = np.array([[9,0,12],
              [0,0,0],
              [12,0,16]])
P = 1/25 * P
x = np.array([[1,1,1]])
print(b.shape)
lamda = (b.T * x) / (b @ b.T)
nu = lamda * b
print(lamda)
# print(nu)
# print(P * x)
left = (x @ b.T) / (b @ b.T) * b
print("b:",b.shape,"x",x.shape)
print(left)

x = np.array([[1,1,1]])
x_prime = np.array([[5,10,10]])
x_prime = 1/9 * x_prime
temp = x - x_prime
result = temp @ temp.T
print(result)