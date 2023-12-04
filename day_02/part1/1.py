#!/usr/bin/env python3
import os
import re
from time import time

cubeCounts = {"red": 12, "green": 13, "blue": 14}


def main():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, "../input.txt")
    with open(filename, "r") as myfile:
        rows = myfile.read().splitlines()

    total = 0
    for row in rows:
        possible = True
        parts = row.split(":")
        gameNumber = int(parts[0].split(" ")[1])
        subsets = parts[1]
        for subset in subsets.split(";"):
            for draw in subset.split(","):
                draw = draw.strip()
                count, colour = draw.split(" ")
                if int(count) > cubeCounts.get(colour):
                    print(f"{gameNumber} is not possible, continuing")
                    possible = False
                    break
        if possible:
            print(f"{gameNumber} is possible, summing...")
            total += gameNumber

    return total


if __name__ == "__main__":
    challenge_start_time = time()
    result = main()
    challenge_end_time = time()
    print(f"Result: {result}")
    print(
        f"Finished in {round((challenge_end_time  - challenge_start_time) * 1000, 5)} milliseconds"
    )
