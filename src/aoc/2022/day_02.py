from enum import IntEnum
from typing import List, Tuple


class Shape(IntEnum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


class ShapeLookupTable(IntEnum):
    A = Shape.ROCK
    B = Shape.PAPER
    C = Shape.SCISSORS
    X = Shape.ROCK
    Y = Shape.PAPER
    Z = Shape.SCISSORS


TOURNAMENT_RULES = {
    Shape.ROCK: (Shape.SCISSORS, Shape.PAPER),
    Shape.PAPER: (Shape.ROCK, Shape.SCISSORS),
    Shape.SCISSORS: (Shape.PAPER, Shape.ROCK),
}


def compact_list(input: List[str]) -> List[Tuple[Shape, Shape]]:
    return [(ShapeLookupTable[a], ShapeLookupTable[b]) for a, b in [p.split() for p in input]]


def compute_score(opponent: Shape, player: Shape, manipulate: bool = False) -> int:
    if manipulate:
        if player == Shape.ROCK:
            player = TOURNAMENT_RULES[opponent][0]
        elif player == Shape.SCISSORS:
            player = TOURNAMENT_RULES[opponent][1]
        else:
            player = opponent

    if player == TOURNAMENT_RULES[opponent][0]:
        return player.value
    elif player == opponent:
        return player.value + 3
    else:
        return player.value + 6


def answer_1(input: List[str]) -> int:
    normalized_list = compact_list(input)
    scored_list = [compute_score(o, p, manipulate=False) for o, p in normalized_list]
    return sum(scored_list)


def answer_2(input: List[str]) -> int:
    normalized_list = compact_list(input)
    scored_list = [compute_score(o, p, manipulate=True) for o, p in normalized_list]
    return sum(scored_list)
