import numpy as np

a = np.array([[2, 2, 1]])
b = np.array([[2, 3, 4]])
c = np.array([[5, 3, 4]])

distance = []


dist = np.linalg.norm(a - b)**2
distance.append(dist)

dist = np.linalg.norm(c - b)**2
distance.append(dist)

print(distance)