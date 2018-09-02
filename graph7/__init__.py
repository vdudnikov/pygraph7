"""
graph7

A simple example of usage:

>>> import graph7 as g7
>>> mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
>>> encoded = g7.encode(mat)
>>> print(encoded)
b'HAAQIDBAUGBwgJ'
>>> decoded = g7.decode(encoded)
>>> print(mat == decoded)
True
"""

try: from .graph7 import *
except ImportError: pass

__all__ = graph7.__all__

__author__     = "Vladik Dudnikov"
__version__     = "0.0"
__revision__    = "0.0.2a1"
