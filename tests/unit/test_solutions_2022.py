from itertools import product
from typing import Iterator, List

import pytest

from _pytest.mark import ParameterSet


FIXTURE_YEAR = "2022"
FIXTURE_DATES = product(range(1, 26), range(1, 3))
FIXTURE_NAMES = ["example", "input"]


def parametrize_fixtures(year, dates, fixtures) -> Iterator[ParameterSet]:
    return [pytest.param(year, day, part, fixtures, id=f"{year}-{day:02}-{part}") for day, part in dates]


@pytest.mark.year(FIXTURE_YEAR)
@pytest.mark.parametrize("year,day,part,fixtures", parametrize_fixtures(FIXTURE_YEAR, FIXTURE_DATES, FIXTURE_NAMES))
def test_solve_puzzle_answers(year: str, day: int, part: int, fixtures: List[str], load_fixtures, solve_puzzle) -> None:
    for fixture_data, expected_output in load_fixtures(year, day, part, fixtures):
        output = solve_puzzle(year, day, part, fixture_data)
        assert output == expected_output
