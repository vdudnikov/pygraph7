# Example 3
# This example show how to decoding matrix from graph7 format

import graph7 as g7
import os

base_path = os.path.dirname(os.path.realpath(__file__))

mat = None

# Reading file with matrix in graph7 format
# and decoding it.
with open(base_path + "/dataset/mat.g7", "r") as file:
    line = file.readline().rstrip()
    mat = g7.decode(line, "float")

# Print type of graph
print(g7.gtype(mat))

try:
    import numpy as np
    # Standart NumPy matrix
    np_mat = np.matrix(mat)
    # Do anything...
except ImportError:
    print("Needed NumPy")
