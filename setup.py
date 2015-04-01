import os
from setuptools import setup, find_packages

# package met info
NAME = "MatrixUtils"
VSESION = "0.0.1"
DESCRIPTION = "Matrix Utils"
AUTHOR = "Yuanye Ge"
URL = "https://github.com/Yuanye/MatrixUtils"
KEYWORDS = ""
CLASSIFIERS = []


commands= {} 

ENTRY_POINTS = """
"""

# dependencies
requires = [
    "redis",
    "msgpack-python",
    "rfc3987",
]

setup(
    name=NAME,
    version=VSESION,
    description=DESCRIPTION,
    author=AUTHOR,
    url = URL,
    packages=find_packages(),
    install_package_data=True,
    commands=commands,
    zip_safe=False,
    install_requires=requires,
    entry_points=ENTRY_POINTS,
)

