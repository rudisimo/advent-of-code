import importlib

from glob import glob
from pathlib import Path
from typing import List, Optional, Tuple

import pytest


@pytest.fixture
def solve_puzzle():
    def wrapper(year: int, day: int, part: int, data: List[str]) -> Optional[str]:
        try:
            solver_fn = getattr(importlib.import_module(f"aoc.{year}.day_{day:0{2}}"), f"answer_{part}")
        except (AttributeError, ModuleNotFoundError) as e:
            raise NotImplementedError(e)
        else:
            return str(solver_fn(data))

    return wrapper


@pytest.fixture
def load_fixtures():
    def wrapper(year: int, day: int, part: int, fixtures: List[str]) -> Tuple[List[str], Optional[str]]:
        for fixture_name in fixtures:
            fixture_glob = f"{Path().absolute()}/tests/fixtures/{year}/{day:0{2}}-{fixture_name}.txt"
            fixture_files = glob(fixture_glob)
            for fixture in fixture_files:
                try:
                    with open(fixture) as fp:
                        samples = fp.read().split("--EXPECT--\n")
                        yield (samples[0].splitlines(), samples[part].strip())
                except (IndexError):
                    yield ([], None)
            if not fixture_files:
                raise FileNotFoundError(f"fixture(s) not found: {fixture_glob}")

    return wrapper
