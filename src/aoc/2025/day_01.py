from __future__ import annotations
from typing import Iterable, Iterator, List

MAX_INT = 99


def answer_1(input: List[str]) -> int:
    rotations = list(extract_rotations(input))
    print(rotations)
    return 0


def answer_2(input: List[str]) -> int:
    return 0


def extract_rotations(input: List[str]) -> Iterator[Iterable[int]]:
    rotations = [map(convert, line.split()) for line in input]
    yield from rotations


def convert(val: str) -> int:
    return 0


def overflow(val: int):
    if not -MAX_INT-1 <= val <= MAX_INT:
        val = (val + (MAX_INT + 1)) % (2 * (MAX_INT + 1)) - MAX_INT - 1
    return val
