"""
graph7 module
"""
import _graph7
from enum import Enum
import struct

class Gtype(Enum):
    """All types of graphs, which the graph7 are supported.
    Formulas for calculate of count of cells of adjacency matrix:
    Undirected:             n * (n - 1) / 2
    Undirected with loops:  n * (n + 1) / 2
    Directed:               n * (n - 1)
    Directed with loops:    n^2
    Where n: order of graph
    """
    Undirected      = 0
    Directed        = 1
    UndirectedLoops = 2
    DirectedLoops   = 3

def gtype(mat):
    """Determine the type of the graph from the adjacency matrix
    """
    is_directed = False
    is_have_loops = False

    order = len(mat)

    for i in range(order - 1):
        for j in range(i + 1, order):
            if mat[i][j] != mat[j][i]:
                is_directed = True
                break
        if is_directed:
            break

    for i in range(order):
        if mat[i][i] != 0:
            is_have_loops = True
            break

    t = 0
    if is_directed:   t |= 1
    if is_have_loops: t |= 2

    return Gtype(t)

def encode(_mat, *args):
    """Encode from adjacency matrix to graph7 format
    """

    wtype = "int"

    if args != ():
        wtype, *_ = args

    mat = []
    for row in _mat: mat.extend(row)

    max_val = max(mat)
    min_val = min(mat)
    width = None
    src = b""

    if wtype == "int":
        max_val = int(max_val)
        min_val = int(min_val)
        mx = max(max_val.bit_length(), min_val.bit_length())
        width = (mx + 8) // 8

        for x in mat:
            x = int(x)
            src += x.to_bytes((x.bit_length() + 8) // 8, "little", signed=True).ljust(width, b"\0")
    else:
        t, width = ("=f", 4) if wtype == "float" else ("=d", 8)
        src = src.join(map(lambda x: struct.pack(t, x), mat))

    if wtype == "int" and max_val <= 1 and min_val >= 0:
        width = 0

    retval = _graph7.encode(src, len(_mat), gtype(_mat).value, width)

    return retval

def decode(src, *args):
    """Decode to adjacency matrix from graph7 format
    """

    wtype = "int"

    if args != ():
        wtype, *_ = args

    if type(src) == str: src = src.encode("utf-8")

    raw, width = _graph7.decode(src)
    mat = []
    if wtype == "int":
        mat = [int.from_bytes(raw[i * width:i * width + width], "little", signed=True) for i in range(int(len(raw) / width))]
    else:
        t = "=f" if wtype == "float" else "=d"
        mat = [struct.unpack(t, raw[i * width:i * width + width])[0] for i in range(int(len(raw) / width))]

    order = int(len(mat)**0.5)
    return [[mat[i * order + j] for j in range(order)] for i in range(order)]

__all__ = [
    "Gtype",
    "gtype",
    "encode",
    "decode",
]
