# Example 2
# This example show how to encoding matrix in graph7 format

import graph7 as g7
import random

order = 4

rand_mat = [[random.randint(0, 255) for _ in range(order)] for _ in range(order)]

# Matrix contains numbers between 0 and 255,
# so for encoding a matrix on one element needed 1 byte
mat1 = g7.encode(rand_mat)

# Matrix contains numbers between 0 and 65535,
# so for encoding a matrix on one element needed 2 bytes
rand_mat = [[random.randint(0, 65535) for _ in range(order)] for _ in range(order)]
mat2 = g7.encode(rand_mat)

# Matrix contains float numbers
# You can choose with what accuracy you need to store
rand_mat = [[random.random() for _ in range(order)] for _ in range(order)]
mat3 = g7.encode(rand_mat, "float")
mat4 = g7.encode(rand_mat, "double")

# Compare
print(mat1)
print(mat2)
print(mat3)
print(mat4)
