from itertools import combinations

from utils import advent
from utils.advent_debug import assert_debug

advent.setup(2023, 11)

DEBUG = """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#....."""

exp = """....#........
.........#...
#............
.............
.............
........#....
.#...........
............#
.............
.............
.........#...
#....#......."""


def p1(data: list[str]) -> int:
    line_without_galaxies = []
    column_without_galaxies = []

    for i, line in enumerate(data):
        if '#' not in line:
            line_without_galaxies.append(i)
    for c, col in enumerate(zip(*data)):
        if '#' not in col:
            column_without_galaxies.append(c)

    galaxies = []
    for r, line in enumerate(data):
        for c, char in enumerate(line):
            if char == '#':
                galaxies.append((r, c))

    distances = []
    for a, b in combinations(galaxies, 2):
        cur_distance = 0
        for num in line_without_galaxies:
            if a[0] < num < b[0] or b[0] < num < a[0]:
                cur_distance += 1
        for num in column_without_galaxies:
            if a[1] < num < b[1] or b[1] < num < a[1]:
                cur_distance += 1
        distances.append(abs(a[0] - b[0]) + abs(a[1] - b[1]) + cur_distance)

    return sum(distances)


def p2(data: list[str]) -> int:
    line_without_galaxies = []
    column_without_galaxies = []

    for i, line in enumerate(data):
        if '#' not in line:
            line_without_galaxies.append(i)
    for c, col in enumerate(zip(*data)):
        if '#' not in col:
            column_without_galaxies.append(c)

    galaxies = []
    for r, line in enumerate(data):
        for c, char in enumerate(line):
            if char == '#':
                galaxies.append((r, c))

    distances = []
    for a, b in combinations(galaxies, 2):
        cur_distance = 0
        for num in line_without_galaxies:
            if a[0] < num < b[0] or b[0] < num < a[0]:
                cur_distance += 999999
        for num in column_without_galaxies:
            if a[1] < num < b[1] or b[1] < num < a[1]:
                cur_distance += 999999
        distances.append(abs(a[0] - b[0]) + abs(a[1] - b[1]) + cur_distance)

    return sum(distances)


if __name__ == '__main__':
    with advent.get_input() as f:
        data = f.read().strip().splitlines()

    assert_debug(DEBUG.splitlines(), 374, p1)

    advent.print_answer(1, p1(data))
    # assert_debug(DEBUG.splitlines(), 8410, p2)
    advent.print_answer(2, p2(data))
