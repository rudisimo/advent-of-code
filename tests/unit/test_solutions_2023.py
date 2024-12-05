from itertools import product
from typing import Iterator

import pytest

from _pytest.mark import ParameterSet


FIXTURE_YEAR = "2023"
FIXTURE_COMPONENTS = product(range(1, 26), [("example-1", 1, 1), ("example-2", 1, 2), ("input", 1, 1), ("input", 2, 2)])


def parametrize_fixtures(year, components) -> Iterator[ParameterSet]:
    return [
        pytest.param(year, day, part, solver, fixture, id=f"{year}-{day:02}-{solver}-{fixture}")
        for day, (fixture, part, solver) in components
    ]


@pytest.mark.year(FIXTURE_YEAR)
@pytest.mark.parametrize("year,day,part,solver,fixture", parametrize_fixtures(FIXTURE_YEAR, FIXTURE_COMPONENTS))
def test_solve_puzzle_answers(
    year: str, day: int, part: int, solver: int, fixture: str, load_fixtures, solve_puzzle
) -> None:
    for fixture_data, expected_output in load_fixtures(year, day, part, [fixture]):
        output = solve_puzzle(year, day, solver, fixture_data)
        assert output == expected_output
