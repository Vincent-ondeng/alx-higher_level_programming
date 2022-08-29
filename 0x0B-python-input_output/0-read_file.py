#!/usr/bin/python3
"""
0-read_file: read file()
"""


def read_file(filename=""):
    """
    read_file reads text file and prints to standard output
    """
    with open(filename, "r", encoding='utf-8') as a_file:
        print("{}".format(a_file.read()), end="")