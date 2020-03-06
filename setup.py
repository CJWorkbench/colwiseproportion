#!/usr/bin/env python

from setuptools import setup

setup(
    name="colwiseproportion",
    version="0.0.1",
    description="Convert numeric columns into proportions of their totals",
    author="Adam Hooper",
    author_email="adam@adamhooper.com",
    url="https://github.com/CJWorkbench/colwiseproportion",
    packages=[""],
    py_modules=["colwiseproportion"],
    install_requires=["pandas==0.25.0", "cjwmodule==*"],
)
