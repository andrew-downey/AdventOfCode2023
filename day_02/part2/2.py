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
        parts = row.split(":")
        gameNumber = int(parts[0].split(" ")[1])
        subsets = parts[1]
        minCubeCounts = {"red": 0, "green": 0, "blue": 0}
        for subset in subsets.split(";"):
            for draw in subset.split(","):
                draw = draw.strip()
                count, colour = draw.split(" ")
                minCubeCounts[colour] = max(minCubeCounts[colour], int(count))
        power = 1
        for val in minCubeCounts.values():
            power *= val
        total += power

    return total


if __name__ == "__main__":
    challenge_start_time = time()
    result = main()
    challenge_end_time = time()
    print(f"Result: {result}")
    print(
        f"Finished in {round((challenge_end_time  - challenge_start_time) * 1000, 5)} milliseconds"
    )
