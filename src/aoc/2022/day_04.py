from typing import List, Set, Tuple


class Section:
    def __init__(self, assignment: str) -> None:
        self.assignment = sorted(set(map(int, assignment.split("-"))))

    def __repr__(self) -> str:
        return f"{self.range}"

    @property
    def range(self) -> Set[int]:
        if len(self.assignment) < 2:
            return set(self.assignment)
        else:
            start, end = self.assignment
            return set(range(start, end + 1))


def compact_list(input: List[str]) -> List[Tuple[Section, Section]]:
    return [(Section(a), Section(b)) for a, b in [p.split(",") for p in input]]


def filter_subset(left: Set[int], right: Set[int]) -> bool:
    return left.issubset(right) or right.issubset(left)


def filter_overlap(left: Set[int], right: Set[int]) -> bool:
    return len(left.intersection(right)) > 0


def answer_1(input: List[str]) -> int:
    normalized_list = compact_list(input)
    overlap_list = [
        1
        for a, b in normalized_list
        if filter_subset(
            a.range,
            b.range,
        )
    ]
    return len(overlap_list)


def answer_2(input: List[str]) -> int:
    normalized_list = compact_list(input)
    overlap_list = [
        1
        for a, b in normalized_list
        if filter_overlap(
            a.range,
            b.range,
        )
    ]
    return len(overlap_list)
