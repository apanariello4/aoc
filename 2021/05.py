import re
from collections import defaultdict

from utils import advent

advent.setup(2021, 5)


def overlaps(moves: list[list[int, int, int, int]], diagonal: bool = False) -> int:
    matrix = defaultdict(int)
    for x1, y1, x2, y2 in moves:
        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                matrix[(x1, y)] += 1
        elif y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                matrix[(x, y1)] += 1
        elif diagonal:
            step_x = 1 if x1 < x2 else -1
            step_y = 1 if y1 < y2 else -1
            for x, y in zip(range(x1, x2 + step_x, step_x), range(y1, y2 + step_y, step_y)):
                matrix[(x, y)] += 1

    return sum(1 for v in matrix.values() if v > 1)


if __name__ == '__main__':

    with advent.get_input() as f:
        moves = f.read().splitlines()
    moves = [list(map(int, re.findall(r"\d+", line))) for line in moves]

    advent.print_answer(1, overlaps(moves))
    advent.print_answer(2, overlaps(moves, True))
