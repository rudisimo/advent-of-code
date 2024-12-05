from __future__ import annotations
from string import digits
from typing import List


W2N_MAP = {
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


def compact_values(input: str) -> int:
    first, last = None, None
    for first in input[::1]:
        if first in digits:
            break
    for last in input[::-1]:
        if last in digits:
            break
    return int(f"{first}{last}")


def compact_digits(input: str) -> str:
    output = ""
    index = 0
    while index < len(input):
        append = input[index]
        for word in W2N_MAP.keys():
            pos = input.find(word, index, index + len(word))
            if pos != -1:
                append = W2N_MAP[word]
                break
        output += append
        index += 1
    return output


def answer_1(input: List[str]) -> int:
    calibration_values = [compact_values(v) for v in input]
    return sum(calibration_values)


def answer_2(input: List[str]) -> int:
    calibration_values = [compact_values(compact_digits(v)) for v in input]
    return sum(calibration_values)
