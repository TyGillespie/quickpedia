"""Quickpedia
Simple CLI tool to look up something on Wikipedia.

Copyright (C) 2020, Ty Gillespie. All rights reserved.
MIT License.
"""

import wikipedia

import sys


if __name__ == "__main__":
    # Todo: Make this except a commandline parem, not an input.
    print("Enter what to search.")
    to_search = input()
    if to_search == "":
        print("Nothing was typed.")
        sys.exit()
    else:
        res = wikipedia.summary(to_search)
        print(res)
        sys.exit()
