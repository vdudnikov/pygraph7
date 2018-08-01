from setuptools import setup, Extension
import graph7

description = """
Package graph7 is designed to store a large number of graphs (adjacency matrices) with two states with a minimum of memory.
However, for convenience, you can store adjacent matrices with any element values (int, float), just for this you need more memory.
"""

ext_modules = [
    Extension(
        "_graph7",
        ["graph7/graph7/src/graph7.c", "graph7/wrapper.c"]
    )
]

setup(
    name="pygraph7",
    python_requires=">=3",
    version=graph7.__revision__,
    description="A simple format for storing different types of graphs in the ASCII-string",
    long_description=description,
    author=graph7.__author__,
    author_email="dudnikov.vladislav@gmail.com",
    url="https://github.com/va-dudnikov/pygraph7",
    packages=["graph7"],
    platforms=['any'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: C",
        "Programming Language :: Python :: 3 :: Only",
    ],
    keywords=["graphs", "storage method"],
    license="MIT",
    ext_modules=ext_modules,
)
