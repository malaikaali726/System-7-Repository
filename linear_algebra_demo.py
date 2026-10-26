import numpy as np

vector_a = np.array([2, 3, 4])
vector_b = np.array([5, 6, 7])
matrix = np.array([[1, 2], [3, 4], [5, 6]])

print("Vector A:", vector_a)
print("Vector B:", vector_b)
print("Matrix:\n", matrix)
print("Dot product:", np.dot(vector_a, vector_b))  # 2*5 + 3*6 + 4*7 = 56
print("Matrix shape:", matrix.shape)
