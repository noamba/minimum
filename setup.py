# -*- coding: utf-8 -*-

from setuptools import find_packages, setup

from minimum._version import __version__

with open("README.md") as f:
    readme = f.read()

with open("LICENSE") as f:
    license = f.read()

setup(
    name="minimum",
    version=__version__,
    description="Find the minimal element in a specific type of array",
    long_description=readme,
    author="Noam Bamberger",
    author_email="noamba@gmail.com",
    url="https://github.com/noamba/minimum",
    license=license,
    packages=find_packages(),
    install_requires=[
        "pytest",
    ],
)
