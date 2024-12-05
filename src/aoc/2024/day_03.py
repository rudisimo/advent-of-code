from __future__ import annotations
import re

from functools import reduce
from operator import mul
from typing import Iterable, Iterator, List


RE_INSTRUCTION_P1 = re.compile(r"(?P<value>mul\(\d+,\d+\))+?", re.I)
RE_INSTRUCTION_P2 = re.compile(r"(?P<value>(mul\(\d+,\d+\)|do(n't)?\(\)))+?", re.I)


def answer_1(input: List[str]) -> int:
    instructions = extract_instructions(input, RE_INSTRUCTION_P1)
    multiplications = extract_multiplications(instructions)
    return sum(multiplications)


def answer_2(input: List[str]) -> int:
    instructions = extract_instructions(input, RE_INSTRUCTION_P2)
    multiplications = extract_multiplications(instructions)
    return sum(multiplications)


def extract_instructions(input: List[str], search_pattern: re.Pattern, /) -> Iterator[re.Match[str]]:
    instructions = search_pattern.finditer("".join(input))
    yield from instructions


def extract_multiplications(input: Iterator[re.Match[str]], /) -> Iterator[int]:
    instruction_enabled = True
    for instruction in input:
        instruction_value = instruction.group("value")
        if instruction_value.startswith("don't("):
            instruction_enabled = False
        elif instruction_value.startswith("do("):
            instruction_enabled = True
        elif instruction_value.startswith("mul("):
            instruction_result = reduce(mul, extract_operands(instruction_value)) if instruction_enabled else 0
            yield instruction_result


def extract_operands(input: str) -> Iterable[int]:
    operands = map(lambda s: int(re.sub(r"\D+", "", s)), input.split(","))
    return operands
