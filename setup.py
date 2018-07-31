from setuptools import setup, Extension
import graph7

description = """
"""

ext_modules = [
    Extension(
        "_graph7",
        ["graph7/graph7/src/graph7.c", "graph7/wrapper.c"]
    )
]

setup(
    name="pygraph7",
    version=graph7.__revision__,
    description="A simple format for storing different types of graphs in the ASCII-string",
    long_description=description,
    author=graph7.__author__,
    author_email="dudnikov.vladislav@gmail.com",
    url="https://github.com/va-dudnikov/pygraph7",
    packages=["graph7"],
    platforms=['any'],
    keywords=["graphs", "storage method"],
    license="MIT",
    ext_modules=ext_modules,
)
