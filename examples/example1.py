# Example 1
# This example show how to encoding matrix in graph7 format

import graph7 as g7
import random

order = 10

# Matrix contains only 0 and 1, so for encoding a matrix on one element
# needed only 1 bit
rand_mat = [[random.randint(0, 1) for _ in range(order)] for _ in range(order)]
directed = g7.encode(rand_mat)

# We leave only the upper triangle of the matrix
for i in range(order):
    for j in range(i, order):
        if i == j:
            rand_mat[i][j] = 0
            continue
        rand_mat[j][i] = rand_mat[i][j]

undirected = g7.encode(rand_mat)

# Compare
print(directed)
print(undirected)
