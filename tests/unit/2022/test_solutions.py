from itertools import product
from typing import List

import pytest


@pytest.mark.parametrize(
    "year,day,part,fixtures",
    [
        pytest.param(2022, day, part, ["example", "input"], id=f"{day}-{part}")
        for day, part in product(range(1, 26), range(1, 3))
    ],
)
def test_should_solve_puzzle(year: int, day: int, part: int, fixtures: List[str], load_fixtures, solve_puzzle) -> None:
    try:
        loaded_fixtures = load_fixtures(year=year, day=day, part=part, fixtures=fixtures)
        for (input_data, expected_output) in loaded_fixtures:
            assert solve_puzzle(year=year, day=day, part=part, data=input_data) == expected_output
    except (FileNotFoundError, NotImplementedError) as e:
        pytest.skip(f"Reason: [{type(e).__name__}] {e}")
