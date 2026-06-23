import numpy as np
import time

size = 1000
matrix_A = np.random.rand(size, size)
matrix_B = np.random.rand(size, size)

list_A = matrix_A.tolist()
list_B = matrix_B.tolist()

# Testing Python Loops

start_time = time.time()

result_loop = [[0 for _ in range(size)] for _ in range(size)]

for i in range(size):
    for j in range(size):
        for k in range(size):
            result_loop[i][j] += list_A[i][k] * list_B[k][j]

loop_time = time.time() - start_time
print(f"Loop Time: {loop_time:.4f} seconds")


# Testing Numpy np.dot()

start_time = time.time()

result_vectorised = matrix_A @ matrix_B

vectorised_time = time.time() - start_time
print(f"NumPy Time: {vectorised_time:.4f} seconds")


# Einsum Way.

start_time = time.time()

einsum_vectorised = np.einsum("ij, jk->ik", matrix_A, matrix_B)
einsum_time = time.time() - start_time

print(f"Einsum Time: {einsum_time:.4f} seconds")