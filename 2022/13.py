import ast
import functools
import math
from typing import Optional, Tuple

from utils import advent

advent.setup(2022, 13)


def recursion(p0: list, p1: list) -> Optional[bool]:
    for left, right in zip(p0, p1):
        if isinstance(left, list) and isinstance(right, list):
            result = recursion(left, right)
            if result is not None:
                return result
        elif isinstance(left, int) and isinstance(right, int):
            if left < right:
                return True
            if left > right:
                return False
        elif isinstance(left, int) and isinstance(right, list):
            result = recursion([left], right)
            if result is not None:
                return result
        elif isinstance(left, list) and isinstance(right, int):
            result = recursion(left, [right])
            if result is not None:
                return result

    if len(p0) < len(p1):
        return True
    if len(p0) > len(p1):
        return False
    return None


def find_correct(pairs: Tuple[Tuple[list, list], ...]) -> int:
    correct_indexes = [idx for idx, (p0, p1) in enumerate(pairs, 1) if recursion(p0, p1)]
    return sum(correct_indexes)


def reorder_sequences(pairs: Tuple[Tuple[list, list], ...]) -> int:
    cmp = functools.cmp_to_key(lambda a, b: -1 if recursion(a, b) else 1)

    sorted_pairs = [[[2]], [[6]]] + [list(pair) for pair in pairs]

    sorted_pairs.sort(key=cmp)

    indexes = [idx for idx, pair in enumerate(sorted_pairs, 1) if pair in ([[2]], [[6]])]
    return math.prod(indexes)


if __name__ == '__main__':
    with advent.get_input() as f:
        data = f.read().split('\n\n')

    pairs = tuple(tuple(map(ast.literal_eval, pair.splitlines())) for pair in data)

    advent.print_answer(1, find_correct(pairs))

    advent.print_answer(2, reorder_sequences(pairs))
