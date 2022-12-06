from itertools import groupby
from typing import List, Tuple


def compact_list(input: List[str], *, sep: str) -> List[Tuple[int]]:
    return [sum(map(int, g)) for k, g in groupby(input, lambda s: s == sep) if not k]


def answer_1(input: List[str]) -> int:
    normalized_list = compact_list(input, sep="")
    result = max(normalized_list)

    return result


def answer_2(input: List[str]) -> int:
    normalized_list = sorted(compact_list(input, sep=""), reverse=True)
    result = sum(normalized_list[:3])

    return result
