import numpy as np

# # GRADED FUNCTION: DO NOT EDIT THIS LINE
# def project_1d(x, b):
#     """Compute the projection matrix onto the space spanned by `b`
#     Args:
#         x: the vector to be projected
#         b: ndarray of dimension (D,), the basis for the subspace
    
#     Returns:
#         y: ndarray of shape (D,) projection of x in space spanned by b
#     """
#     # YOUR CODE HERE
#     ### Uncomment and modify the code below
# #     p = np.zeros((3,)) # <-- EDIT THIS
#     print("xTb")
#     print(x.T * b)
#     print("bTb")
#     print(b @ b.T)
#     p = ((b * b.T) / (np.linalg.norm(b)**2)) * b
#     return p
# #     return p

x = np.array([1, 2, 2])
b = np.array([[1,  2,  2],
              [2,  4,  4],
              [2,  4,  4]]) / 9

# result = project_1d(b, x)
# print("result: ")
# print(result)

# print(b)
# print("-")
# print(b*b.T)
# print(np.linalg.norm(b)**2)

def projection_matrix_1d(b):
    numerator = (b * b.T)
    print("Numerator")
    print(numerator)
    denominator = np.linalg.norm(b)**2
    print("Denominator")
    print(denominator)
    P = numerator / denominator
    print(P)
    return P

projection_matrix_1d(b)