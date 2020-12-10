"""Quickpedia
Simple CLI tool to look up something on Wikipedia.

Copyright (C) 2020, Ty Gillespie. All rights reserved.
MIT License.
"""

import wikipedia

import sys
import argparse
from typing import List


if __name__ == "__main__":
    parser: argparse.ArgumentParser = argparse.ArgumentParser(
        description="Tool to look up things on Wikipedia."
    )
    parser.add_argument("search", help="What to search.")
    parser.add_argument(
        "-f",
        "--file",
        action="store_true",
        help="Write the output to a file, not the terminal.",
    )
    args: List[str] = parser.parse_args()
    to_search: str = args.search
    if to_search == "":
        print("A queery wasn't provided.")
        sys.exit()
    else:
        try:
            res: str = wikipedia.summary(to_search)
            if args.file:
                f = open(to_search + ".txt", "w")
                f.write(res)
                f.close()
            else:
                print(res)
        except wikipedia.exceptions.DisambiguationError:
            print("Too many possible results. Try being more spacific.")
        finally:
            sys.exit()
