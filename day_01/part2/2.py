#!/usr/bin/env python3
import os
import re
from time import time

wordDict = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def main():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, "../input.txt")
    with open(filename, "r") as myfile:
        rows = myfile.read().splitlines()

    regex = "(?=(\d|" + "|".join(wordDict) + "))"

    total = 0
    for row in rows:
        digits = re.findall(regex, row)
        firstDigit = digits.pop(0)
        secondDigit = digits.pop() if len(digits) > 0 else firstDigit

        firstDigit = firstDigit if firstDigit.isdigit() else wordDict[firstDigit]
        secondDigit = secondDigit if secondDigit.isdigit() else wordDict[secondDigit]

        newNumber = firstDigit + secondDigit
        print(f"{newNumber} for {row}")
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
