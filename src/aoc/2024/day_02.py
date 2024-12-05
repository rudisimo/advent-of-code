from __future__ import annotations
from functools import reduce
from itertools import pairwise
from operator import sub
from typing import Iterable, Iterator, List, Tuple


def answer_1(input: List[str]) -> int:
    all_reports = extract_reports(input)
    safe_reports = calculate_safety(all_reports, failure_threshold=0)
    return sum(safe_reports)


def answer_2(input: List[str]) -> int:
    all_reports = extract_reports(input)
    safe_reports = calculate_safety(all_reports, failure_threshold=1)
    return sum(safe_reports)


def extract_reports(input: Iterable[str], /) -> Iterator[List[int]]:
    levels = [list(map(int, line.split())) for line in input]
    yield from levels


def calculate_safety(input: Iterator[List[int]], /, failure_threshold: int = 0) -> Iterator[bool]:
    for _, deltas, directions in filter_reports(input, failure_threshold):
        delta_anomalies = [d for d in deltas if d == 0 or not -4 < d < 4]
        safety_checks = [len(delta_anomalies) == 0, len(set(directions)) == 1]
        yield all(safety_checks)


def filter_reports(
    input: Iterator[List[int]], failure_threshold: int, /
) -> Iterator[Tuple[List[int], List[int], List[int]]]:
    failure_count = 0
    report = next(input)
    while report:
        try:
            deltas = [reduce(sub, reversed(p)) for p in pairwise(report)]
            directions = [-1 if d < 0 else +1 if d > 0 else 0 for d in deltas]
            metadata = zip(deltas, directions)

            # Tolerate bad levels up to a certain threshold
            if failure_count < failure_threshold:
                prevdir = None
                for idx, (delta, curdir) in enumerate(metadata):
                    # Criteria: is neither an increase or a decrease
                    if delta == 0:
                        raise ValueError(idx)
                    # Criteria: is neither an increase or a decrease of at least 1 and at most 3
                    elif not -4 < delta < 4:
                        raise ValueError(idx)
                    # Criteria: is neither all increasing or all decreasing
                    elif prevdir is not None and prevdir != curdir:
                        raise ValueError(idx)
                    prevdir = curdir

            # Return values
            yield report, deltas, directions

            # Pull next report or STOP
            failure_count = 0
            report = next(input)
        except ValueError as err:
            # Remove failure and try again
            failure_count += 1
            del report[err.args[0]]
            continue
        except StopIteration:
            break
