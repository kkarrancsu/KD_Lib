#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

import codecs
import os

from setuptools import find_packages, setup

# Basic information
with open("README.rst", "r") as f:
    LONG_DESCRIPTION = f.read()

# Define the keywords
KEYWORDS = [
    "Knowledge Distillation",
    "Pruning",
    "Quantization",
    "pytorch",
    "machine learning",
    "deep learning",
]
REQUIRE_PATH = "requirements.txt"
PROJECT = os.path.abspath(os.path.dirname(__file__))
setup_requirements = ["pytest-runner"]

test_requirements = ["pytest", "pytest-cov"]

requirements = [
    "pip",
    "transformers",
    "sacremoses",
    "tokenizers",
    "huggingface-hub",
    "torchtext",
    "bumpversion",
    "wheel",
    "watchdog",
    "flake8",
    "tox",
    "coverage",
    "Sphinx",
    "twine",
    "pytest",
    "pytest-runner",
    "pytest-cov",
    "matplotlib",
    "torch",
    "torchvision",
    "tensorboard",
    "contextlib2",
    "pandas",
    "tqdm",
    "numpy",
    "sphinx-rtd-theme",
]


if __name__ == "__main__":
    setup(
        author="Het Shah",
        author_email="divhet163@gmail.com",
        classifiers=[
            "Development Status :: 2 - Pre-Alpha",
            "Intended Audience :: Developers",
            "License :: OSI Approved :: MIT License",
            "Natural Language :: English",
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.7",
        ],
        description="A Pytorch Library to help extend all Knowledge Distillation works",
        install_requires=requirements,
        license="MIT license",
        long_description=LONG_DESCRIPTION,
        include_package_data=True,
        keywords=KEYWORDS,
        name="KD_Lib",
        packages=find_packages(where=PROJECT),
        setup_requires=setup_requirements,
        test_suite="tests",
        tests_require=test_requirements,
        url="https://github.com/SforAiDL/KD_Lib",
        version="0.0.29",
        zip_safe=False,
    )
