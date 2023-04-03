import numpy as np

# NO 1
# x = np.array([[6,0,0]])
# b1 = np.array([[1,1,1]])
# b2 = np.array([[0,1,2]])
# x = x.reshape(3,-1)
# b1 = b1.reshape(3,-1)
# b2 = b2.reshape(3,-1)
# print(x.shape, b1.shape, b2.shape)

# B = np.concatenate((b1,b2), axis=1)
# print(B)

# BTX = B.T @ x
# BTB = B.T @ B

# lamda = np.linalg.solve(BTB, BTX)

# print("BTX: ")
# print(BTX)
# print("BTB: ")
# print(BTB)
# print("Lamda: ")
# print(lamda)
# print("XUN :")
# print(lamda[0]*b1 + lamda[1]*b2)
# print("projection matrix: ")
# print(B@np.linalg.inv(BTB)@B.T)

# NO 2
# x = np.array([[3,2,2]])
# b1 = np.array([[1,0,0]])
# b2 = np.array([[0,1,1]])
# x = x.reshape(3,-1)
# b1 = b1.reshape(3,-1)
# b2 = b2.reshape(3,-1)
# print(x.shape, b1.shape, b2.shape)

# B = np.concatenate((b1,b2), axis=1)
# print(B)

# BTX = B.T @ x
# BTB = B.T @ B

# lamda = np.linalg.solve(BTB, BTX)

# print("BTX: ")
# print(BTX)
# print("BTB: ")
# print(BTB)
# print("Lamda: ")
# print(lamda)
# print("XUN :")
# print(lamda[0]*b1 + lamda[1]*b2)
# print("projection matrix: ")
# print(B@np.linalg.inv(BTB)@B.T)

# NO 3
# x = np.array([[12,0,0]])
# b1 = np.array([[1,1,1]])
# b2 = np.array([[0,1,2]])
# x = x.reshape(3,-1)
# b1 = b1.reshape(3,-1)
# b2 = b2.reshape(3,-1)
# print(x.shape, b1.shape, b2.shape)

# B = np.concatenate((b1,b2), axis=1)
# print(B)

# BTX = B.T @ x
# BTB = B.T @ B

# lamda = np.linalg.solve(BTB, BTX)

# print("BTX: ")
# print(BTX)
# print("BTB: ")
# print(BTB)
# print("Lamda: ")
# print(lamda)
# print("XUN :")
# print(lamda[0]*b1 + lamda[1]*b2)
# print("projection matrix: ")
# print(B@np.linalg.inv(BTB)@B.T)

# NO 3
# x = np.array([[10,4,-2]])
# b1 = np.array([[-10*np.sqrt(6), -4*np.sqrt(6), 2*np.sqrt(4)]])
# x = x.reshape(3,-1)
# b1 = b1.reshape(3,-1)
# print(x.shape, b1.shape)

# B = b1
# print(B)

# BTX = B.T @ x
# BTB = B.T @ B

# lamda = np.linalg.solve(BTB, BTX)

# print("BTX: ")
# print(BTX)
# print("BTB: ")
# print(BTB)
# print("Lamda: ")
# print(lamda)
# print("XUN :")
# print(lamda[0]*b1)
# print("projection matrix: ")
# print(B@np.linalg.inv(BTB)@B.T)