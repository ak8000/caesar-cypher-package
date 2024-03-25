![GitHub Release](https://img.shields.io/github/v/release/software-students-spring2024/3-python-package-exercise-ja-ia)


# Python Package Exercise

An exercise to create a Python package, build it, test it, distribute it, and use it. See [instructions](./instructions.md) for details.

# Project Description
Our project is a Caesar cipher package inteded to help encrypt messages for users.

# Documentation

export PYTHONPATH="/your-path/src:$PYTHONPATH"

# Installation

To install, just use pip to install from PyPI:

`` pip install ccrypt ``
or
`` pip3 install ccrypt ``

# Usage

Upon installation, just call *ccrypt* the program from the command line.

Once the program is called, first type and enter whether you would like to (e)ncrypt, (d)ecrypt, or (b)rute-force (note that only an encryption up to 26 is allowed).

If encrypt, then simply enter the text you would like to encrypt as the first parameter and the amount you'd like each character shifted as the second parameter. The program will then output the Caesar cipher.

If decrypt, then simply enter the text you would like to know as the first parameter and the amount you know each character shifted as the second parameter. The program will then output the original text.

If brute-force, then the program will iterate through all of the possible shifts and output all of the results.

# Contributors

- [Alex Kondratiuk](https://github.com/ak8000)
- [Janet Pan](https://github.com/jp6024)
- [Isaac Kwon](https://github.com/iok206)
- [Adam Schwartz](https://github.com/aschwartz01)

# PyPI page
