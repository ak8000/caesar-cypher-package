![GitHub Release](https://img.shields.io/github/v/release/software-students-spring2024/3-python-package-exercise-ja-ia)

# Project Description
Our project is a Caesar cipher package inteded to help encrypt messages for users.

# Documentation

## Functions

caesar_encrypt(text, shift)

    Given given text of alphanumerical characters, return a Caesar cipher with a specified shift amount. Shift must be positive number

    :param text: The input string to encrypt.
    :param shift: The number of positions to shift each character.
    :return: The encrypted string.

caesar_decrypt(text, shift)

    Given given Caeser cipher of alphanumerical characters, return unencrypted message if you have the original shift amount. Shift must be a positive number.
       
    :param text: The input string to decrypt.
    :param shift: The number of positions the characters were shifted to encrypt.
    :return: The decrypted string.

brute_force_decrypt(encrypted_text)

    Possibly decrypts alphanumeric Caesar cipher by going through all of the possible shift amounts. Return every possible shift amount

    :param encrypted_text: The encrypted message to decrypt.
    :return: A dictionary of all possible shifts and their corresponding decrypted messages.

verify_encryption_decryption(original_text, decrypted_text):

    Verifies that the original plaintext matches the decrypted text,
indicating the encryption and decryption processes are inverses of each other.

    :param original_text: The original plaintext before encryption.
    :param decrypted_text: The text after being encrypted and then decrypted.
    :return: True if the original and decrypted texts match, False otherwise.

export PYTHONPATH="/your-path/src:$PYTHONPATH"


# Installation

To install, just use pip to install from PyPI:

`` pip install ccrypt ``
or
`` pip3 install ccrypt ``

For your 

# Usage

Upon installation, just call *ccrypt* the program from the command line:
`` python -m ccrypt `` or ``python 3 ccrypt ``

Once the program is called, first type and enter whether you would like to (e)ncrypt, (d)ecrypt, or (b)rute-force (note that only an encryption up to 26 is allowed).

If encrypt, then simply enter the text you would like to encrypt as the first parameter and the amount you'd like each character shifted as the second parameter. The program will then output the Caesar cipher.

If decrypt, then simply enter the text you would like to know as the first parameter and the amount you know each character shifted as the second parameter. The program will then output the original text. Make sure you remember the shift for any encrypted message you create.

If brute-force, then the program will iterate through all of the possible shifts and output all of the results.

# Contributors

- [Alex Kondratiuk](https://github.com/ak8000)
- [Janet Pan](https://github.com/jp6024)
- [Isaac Kwon](https://github.com/iok206)
- [Adam Schwartz](https://github.com/aschwartz01)

# PyPI page
