# Simple fuzzy test

import unittest
import graph7 as g7
import copy
import random

MIN_INT_VAL = 0
MAX_INT_VAL = 2**128
MIN_ORDER = 3
MAX_ORDER = 50
NITERS = 1

class TestGraph7(unittest.TestCase):
    def _testing(self, min_order, max_order, wtype, niters, min_int_val = 0, max_int_val = 1):
        def to_undirected(_mat):
            mat = copy.deepcopy(_mat)
            order = len(mat)
            for i in range(order - 1):
                for j in range(i + 1, order):
                    mat[j][i] = mat[i][j]

            return mat

        def to_unloops(_mat):
            mat = copy.deepcopy(_mat)
            for i in range(len(mat)):
                mat[i][i] = 0

            return mat

        def random_mat(order, wtype, min_int_val, max_int_val):
            mat = None
            if wtype == "int":
                mat = [[random.randint(min_int_val, max_int_val) for _ in range(order)] for _ in range(order)]
            else:
                mat = [[random.random() for _ in range(order)] for _ in range(order)]

            return mat

        for _ in range(niters):
            for order in range(min_order, max_order):
                # Directed with loops
                mat1 = random_mat(order, wtype, min_int_val, max_int_val)
                # Directed without loops
                mat2 = to_unloops(mat1)
                # Undirected with loops
                mat3 = to_undirected(mat1)
                # Undirected without loops
                mat4 = to_undirected(mat2)

                self.assertEqual(g7.decode(g7.encode(mat1, wtype), wtype), mat1)
                self.assertEqual(g7.decode(g7.encode(mat2, wtype), wtype), mat2)
                self.assertEqual(g7.decode(g7.encode(mat3, wtype), wtype), mat3)
                self.assertEqual(g7.decode(g7.encode(mat4, wtype), wtype), mat4)

    def test_compact(self):
        self._testing(MIN_ORDER, MAX_ORDER, "int", NITERS)

    def test_int(self):
        self._testing(MIN_ORDER, MAX_ORDER, "int", NITERS, MIN_INT_VAL, MAX_INT_VAL)

    def test_float(self):
        self._testing(MIN_ORDER, MAX_ORDER, "double", NITERS)

unittest.main()
