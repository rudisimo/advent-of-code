import importlib

from glob import glob
from pathlib import Path
from typing import List, Union

import pytest


def pytest_addoption(parser):
    parser.addoption(
        "-Y",
        action="store",
        metavar="YYYY",
        help="only run tests matching the year YYYY.",
    )


def pytest_configure(config):
    config.addinivalue_line("markers", "year(YYYY): mark test to run only for specific year")


def pytest_runtest_setup(item):
    years = [mark.args[0] for mark in item.iter_markers(name="year")]
    if years:
        year_opt = item.config.getoption("-Y")
        if year_opt and year_opt not in years:
            pytest.skip(f"test requires year to be in [{', '.join(years)}]")


@pytest.fixture
def solve_puzzle():
    def wrapper(year: int, day: int, part: int, fixture_data: List[str]):
        try:
            solver_module = f"aoc.{year}.day_{day:0{2}}"
            solver_attr = f"answer_{part}"
            solver_fn = getattr(importlib.import_module(solver_module), solver_attr)
        except (AttributeError, ModuleNotFoundError):
            pytest.skip(f"solver not found: {solver_module}:{solver_attr}")
        else:
            return str(solver_fn(fixture_data))

    return wrapper


@pytest.fixture(scope="session")
def load_fixtures():
    def wrapper(year: Union[str, int], day: Union[str, int], part: Union[str, int], fixture_names: List[str]):
        for fixture_name in fixture_names:
            fixture_glob = f"{Path().absolute()}/tests/fixtures/{year}/{day:02}-{fixture_name}.txt"
            fixture_files = glob(fixture_glob)
            for fixture in fixture_files:
                try:
                    with open(fixture) as fp:
                        samples = fp.read().split("--EXPECT--\n")
                        yield (samples[0].splitlines(), samples[part].strip())
                except (IndexError):
                    yield ([], None)
            if not fixture_files:
                pytest.skip(f"fixture not found: {fixture_glob}")

    return wrapper
