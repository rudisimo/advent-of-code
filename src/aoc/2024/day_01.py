from __future__ import annotations
from functools import reduce
from operator import countOf, mul, sub
from typing import Iterable, Iterator, List


def answer_1(input: List[str]) -> int:
    locations = extract_locations(input)
    distance = calculate_distance(locations)
    return distance


def answer_2(input: List[str]) -> int:
    locations = extract_locations(input)
    distance = calculate_similarity(locations)
    return distance


def extract_locations(input: List[str]) -> Iterator[Iterable[int]]:
    locations = [map(int, line.split()) for line in input]
    yield from locations


def calculate_distance(input: Iterator[Iterable[int]]) -> int:
    locations = zip(*map(sorted, zip(*input)))
    distances = [reduce(sub, sorted(v, reverse=True)) for v in locations]
    return sum(distances)


def calculate_similarity(input: Iterator[Iterable[int]]) -> int:
    left, right = zip(*input)
    similarity = [reduce(mul, (v,), countOf(right, v)) for v in left]
    return sum(similarity)
