from utils import advent
from utils.advent_debug import assert_debug

advent.setup(2023, 13)

DEBUG = """#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#"""


def parse(data: str) -> list[str]:
    data = data.split('\n\n')
    return data


def transpose(x: list[list[str]]) -> list[list[str]]:
    return list(map(list, zip(*x)))


def solvep1(pattern: list[str]) -> int:
    for i in range(1, len(pattern)):
        above = pattern[:i][::-1]
        below = pattern[i:]
        min_len = min(len(above), len(below))
        if above[:min_len] == below[:min_len]:
            return i

    return 0


def solvep2(pattern: list[str]) -> int:
    for i in range(1, len(pattern)):
        above = pattern[:i][::-1]
        below = pattern[i:]
        min_len = min(len(above), len(below))
        non_matches = 0
        for j in range(min_len):
            non_matches += len([k for k in range(len(above[j])) if above[j][k] != below[j][k]])
            if non_matches > 1:
                break
        if non_matches == 1:
            return i
    return 0


def p1(data: list[str]) -> int:
    tot = 0
    for pattern in data:
        pattern = pattern.splitlines()
        tot += 100 * solvep1(pattern)
        tot += solvep1(transpose(pattern))
    return tot


def p2(data: list[str]) -> int:
    tot = 0
    for pattern in data:
        pattern = pattern.splitlines()
        tot += 100 * solvep2(pattern)
        tot += solvep2(transpose(pattern))
    return tot


if __name__ == '__main__':
    with advent.get_input() as f:
        data = f.read().strip()
    data = parse(data)

    assert_debug(parse(DEBUG), 405, p1)
    advent.print_answer(1, p1(data))
    assert_debug(parse(DEBUG), 400, p2)

    advent.print_answer(2, p2(data))
