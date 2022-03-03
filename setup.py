import os

import setuptools
from setuptools import setup


def get_long_description():
    with open(
        os.path.join(os.path.dirname(__file__), "README.md"), encoding="utf8"
    ) as fp:
        return fp.read()


setup(
    name="data_science_common",
    version="0.1.4",
    description="UNDER CONSTRUCTION: A simple python library for facilitating analysis",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Ryan Kelley",
    url="https://github.com/kelleyrw/data_science_common",
    license="Apache License, Version 2.0",
    py_modules=["dsc"],
    extras_require={"test": ["pytest"]},
    package_dir={"": "."},
    packages=setuptools.find_packages(where="."),
    install_requires=[
        # "boto3==1.11.13",
        # "paramiko==2.7.1",
        # "sqlparse==0.3.0",
        # "tabulate==0.8.7",
        # "grpcio==1.33.2",
        # "google-cloud-bigquery-storage==2.0.1",
        # "pandas-gbq==0.14.0",
        # "pyarrow==1.0.1",
        # "gcsfs==0.7.1",
        # "boto3",
        # "paramiko",
        # "sqlparse",
        # "tabulate",
        # "grpcio",
        # "google-cloud-bigquery-storage",
        # "pandas-gbq",
        # "pyarrow",
        # "gcsfs",
    ],
    python_requires=">=3.7",
)
