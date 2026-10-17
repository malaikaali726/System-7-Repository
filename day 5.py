# Day 5: NumPy arrays, indexing, mathematical operations
import numpy as np

# Creating arrays
arr = np.array([10, 20, 30, 40, 50])
print("Array:", arr)
print("Shape:", arr.shape)
print("Data type:", arr.dtype)

# Indexing and slicing
print("First element:", arr[0])
print("Last element:", arr[-1])
print("Slice (index 1 to 3):", arr[1:4])

# Mathematical operations
print("Add 5:", arr + 5)
print("Multiply by 2:", arr * 2)
print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Max:", np.max(arr))

# 2D array (matrix)
matrix = np.array([[1, 2, 3], [4, 5, 6]])
print("Matrix:\n", matrix)
print("Shape:", matrix.shape)
print("Element at row 1, column 2:", matrix[1, 2])
print("Column sums:", matrix.sum(axis=0))
print("Row sums:", matrix.sum(axis=1))

# Creating special arrays
print("Zeros:", np.zeros(3))
print("Ones:", np.ones((2, 2)))
print("Range array:", np.arange(0, 10, 2))