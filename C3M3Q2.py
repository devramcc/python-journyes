import numpy as np

x = np.array([[2,1,1]])
b1 = np.array([[1,2,0]])
b2 = np.array([[1,1,0]])
x = x.reshape(3,-1)
b1 = b1.reshape(3,-1)
b2 = b2.reshape(3,-1)
print(x.shape, b1.shape, b2.shape)

B = np.concatenate((b1,b2), axis=1)
print(B)

BTX = B.T @ x
BTB = B.T @ B

lamda = np.linalg.solve(BTB, BTX)

print("BTX: ")
print(BTX)
print("BTB: ")
print(BTB)
print("Lamda: ")
print(lamda)
print("XUN :")
print(lamda[0]*b1 + lamda[1]*b2)