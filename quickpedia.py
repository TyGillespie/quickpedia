"""Quickpedia
Simple CLI tool to look up something on Wikipedia.

Copyright (C) 2020, Ty Gillespie. All rights reserved.
MIT License.
"""

import wikipedia

import sys
import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Tool to look up things on Wikipedia.")
    parser.add_argument("search", help="What to search.")
    args = parser.parse_args()
    to_search = args.search
    if to_search == "":
        print("A queery wasn't provided.")
        sys.exit()
    else:
        res = wikipedia.summary(to_search)
        print(res)
        sys.exit()
