import os

import setuptools
from setuptools import setup

import dsc


def get_long_description():
    with open(
        os.path.join(os.path.dirname(__file__), "README.md"), encoding="utf8"
    ) as fp:
        return fp.read()


def get_version():
    version = (dsc.get_version(),)
    return version


setup(
    name="data_science_common",
    version=get_version(),
    description="UNDER CONSTRUCTION: A simple python library for facilitating analysis",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Ryan Kelley",
    url="https://github.com/kelleyrw/data_science_common",
    license="Apache License, Version 2.0",
    project_urls={
        # "Documentation": "https://packaging.python.org/tutorials/distributing-packages/",
        "Funding": "https://donate.pypi.org",
        "Source": f"https://github.com/kelleyrw/data_science_common/{get_version()}",
        "Tracker": "https://github.com/kelleyrw/data_science_common/issues",
    },
    # py_modules=[], # stand-alone modules
    extras_require={"test": ["pytest"]},
    package_dir={"": "."},
    packages=setuptools.find_packages(include=["dsc", "dsc.*"]),
    install_requires=[
        "tabulate>=0.8",
        "sqlparse>=0.4.2",
        # "boto3==1.11.13",
        # "paramiko==2.7.1",
        # "sqlparse==0.3.0",
        # "tabulate==0.8.7",
        # "grpcio==1.33.2",
        # "pandas-gbq==0.14.0",
        # "pyarrow==1.0.1",
        # "gcsfs==0.7.1",
        # "boto3",
        # "paramiko",
        # "sqlparse",
        # "grpcio",
        # "google-cloud-bigquery-storage==2.0.1",
        # "google-cloud-bigquery-storage",
        # "pandas-gbq",
        # "pyarrow",
        # "gcsfs",
    ],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.7",
)
