# Task 5: NumPy array operations on a sample matrix
import numpy as np

matrix = np.array([
    [2, 4, 6],
    [1, 3, 5],
    [7, 8, 9]
])

print("Original matrix:\n", matrix)
print("\nShape:", matrix.shape)
print("Element at row 0, column 2:", matrix[0, 2])
print("First row:", matrix[0])
print("Last column:", matrix[:, -1])

# Mathematical operations
print("\nMatrix multiplied by 2:\n", matrix * 2)
print("\nMatrix plus 10:\n", matrix + 10)
print("\nTranspose:\n", matrix.T)
print("\nMatrix multiplication with itself:\n", np.dot(matrix, matrix))

# Statistics
print("\nSum of all elements:", matrix.sum())
print("Column sums:", matrix.sum(axis=0))
print("Row averages:", matrix.mean(axis=1))
print("Max value:", matrix.max())
print("Min value:", matrix.min())

# Boolean filtering
print("\nValues greater than 5:", matrix[matrix > 5])