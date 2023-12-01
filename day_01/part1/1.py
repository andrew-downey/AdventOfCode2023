#!/usr/bin/env python3
import os
import re
from time import time


def main():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, "../input.txt")
    with open(filename, "r") as myfile:
        rows = myfile.read().splitlines()

    total = 0
    for row in rows:
        digits = re.findall(r"\d", row)
        firstDigit = digits.pop(0)
        newNumber = firstDigit + (digits.pop() if len(digits) > 0 else firstDigit)
        print(f"Adding new number: {newNumber}")
        total += int(newNumber)

    return total


if __name__ == "__main__":
    challenge_start_time = time()
    result = main()
    challenge_end_time = time()
    print(f"Result: {result}")
    print(
        f"Finished in {round((challenge_end_time  - challenge_start_time) * 1000, 5)} milliseconds"
    )
