from __future__ import annotations
from string import ascii_letters
from typing import List, Set, Tuple


PRIORITY_TABLE = {c: i for i, c in enumerate(ascii_letters, 1)}


class RuckSack:
    def __init__(self, string: str) -> None:
        self.string = string
        self.length = len(string)
        self.midpoint = self.length >> 1

    @property
    def left(self) -> Set[str]:
        return set(self.string[slice(None, self.midpoint, None)])

    @property
    def right(self) -> Set[str]:
        return set(self.string[slice(self.midpoint, None, None)])

    @property
    def full(self) -> Set[str]:
        return set(self.string)


class RuckSackGroup:
    def __init__(self, rucksacks: List[RuckSack]) -> None:
        self.rucksacks = rucksacks
        print(self.rucksacks)

    def __iter__(self) -> RuckSackGroup:
        self.iterator = iter([g for g in zip(*[iter(self.rucksacks)] * 3)])
        return self

    def __next__(self) -> Tuple[RuckSack]:
        group = next(self.iterator)
        return group


def compact_list(input: List[str]) -> List[RuckSack]:
    return [RuckSack(i) for i in input]


def find_common(item: Set[str], *peers: Set[str]) -> Set[str]:
    intersection = item.intersection(*peers)
    return intersection


def answer_1(input: List[str]) -> int:
    normalized_list = compact_list(input)
    scored_list = [PRIORITY_TABLE[i] for r in normalized_list for i in find_common(r.left, r.right)]
    return sum(scored_list)


def answer_2(input: List[str]) -> int:
    normalized_list = RuckSackGroup(compact_list(input))
    scored_list = [PRIORITY_TABLE[i] for g in normalized_list for i in find_common(*[r.full for r in g])]
    return sum(scored_list)
