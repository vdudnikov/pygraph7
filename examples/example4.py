# Example 4
# This example show how to decoding matrix from graph7 format.
# Here we read all pairwise non-isomorphics simple graphs of sixth order
# and calculate number of edges.

import graph7 as g7
import os

base_path = os.path.dirname(os.path.realpath(__file__))

def edges_num(mat):
    score = 0
    order = len(mat)

    for i in range(order - 1):
        for j in range(i + 1, order):
            score += mat[i][j]

    return score

with open(base_path + "/dataset/6.lst", "r") as file:
    lines = [line.rstrip() for line in file.readlines()]

    for line in lines:
        print(edges_num(g7.decode(line)))
