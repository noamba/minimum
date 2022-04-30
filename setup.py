# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open("README.md") as f:
    readme = f.read()

with open("LICENSE") as f:
    license = f.read()

setup(
    name="minimum",
    version="0.1.1",
    description="Find the minimal element in a specific type of array",
    long_description=readme,
    author="Noam Bamberger",
    author_email="noamba@gmail.com",
    url="https://github.com/noamba/minimum",
    license=license,
    py_modules=["minimum"],
    install_requires=[
        "pytest",
    ],
)
