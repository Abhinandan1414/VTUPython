import numpy as np
from scipy.sparse import csr_matrix

# Create a sparse matrix
data = np.array([1, 2, 3, 4])  # Non-zero values
row_indices = np.array([0, 0, 1, 2])  # Row indices
col_indices = np.array([1, 3, 2, 0])  # Column indices

sparse_matrix = csr_matrix((data, (row_indices, col_indices)))

# Accessing values
print(sparse_matrix[0, 1])  # Accessing a specific element

# Converting back to a dense matrix
dense_matrix = sparse_matrix.toarray()
print(dense_matrix)

# Performing operations on sparse matrices
sparse_matrix_squared = sparse_matrix.multiply(sparse_matrix)
print(sparse_matrix_squared.toarray())
