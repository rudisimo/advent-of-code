# Advent of Code

[![Python Package](https://github.com/rudisimo/advent-of-code/actions/workflows/build.yaml/badge.svg?branch=main)](https://github.com/rudisimo/advent-of-code/actions/workflows/build.yaml)

[Advent of Code](https://adventofcode.com/) is an Advent calendar of small programming puzzles for a variety of skill sets and skill levels that can be solved in any programming language you like.

This project contains all of my attempts at finishing the Advent of Code calendar each year.

## Quickstart

Create a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -U pip setuptools
python3 -m pip install -e '.[test]'
```

Check all answers for 2024:

```bash
python3 -m pytest --cov=. -k 2024
```

## License

Licensed under the [MIT](LICENSE.txt) license.
