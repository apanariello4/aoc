try:
    from tqdm import tqdm
except ImportError:
    def tqdm(x, *args, **kwargs):
        return x

from utils import advent
from utils.advent_debug import assert_debug

advent.setup(2023, 14)

DEBUG = """O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#...."""


def transpose(x: list[list[str]]) -> list[list[str]]:
    return list(map(list, zip(*x)))


def roll_north(lines: list[list[str]]) -> list[list[str]]:
    changed = True
    while changed:
        changed = False
        for y, line in enumerate(lines[:-1]):
            for x, space in enumerate(line):
                if space == '.' and lines[y + 1][x] == 'O':
                    line[x] = 'O'
                    lines[y + 1][x] = '.'
                    changed = True
    return lines


def roll_south(lines: list[list[str]]) -> list[list[str]]:
    changed = True
    while changed:
        changed = False
        for y, line in enumerate(lines[1:]):
            for x, space in enumerate(line):
                if space == '.' and lines[y][x] == 'O':
                    line[x] = 'O'
                    lines[y][x] = '.'
                    changed = True
    return lines


def roll_east(lines: list[list[str]]) -> list[list[str]]:
    changed = True
    while changed:
        changed = False
        for line in lines:
            l = ''.join(line)
            if 'O.' in l:
                line[:] = l.replace('O.', '.O')
                changed = True
    return lines


def roll_west(lines: list[list[str]]) -> list[list[str]]:
    changed = True
    while changed:
        changed = False
        for line in lines:
            l = ''.join(line)
            if '.O' in l:
                line[:] = l.replace('.O', 'O.')
                changed = True
    return lines


def p1(data: list[str]) -> int:
    # bring all the O's to the north as much as possible
    lines = [list(row) for row in data]
    lines = roll_north(lines)

    weight = 0
    for y, line in enumerate(lines[::-1]):
        weight += (y + 1) * line.count('O')
    return weight


def p2(data: list[str]) -> int:
    lines = [list(row) for row in data]
    hashes = []
    target = 0
    with tqdm(total=1000000000) as pbar:
        while True:
            h = hash(tuple([''.join(l) for l in lines]))
            if not target and h in hashes:
                start = hashes.index(h)
                length = len(hashes) - start
                target = (1000000000 - start) % length + start + length
                pbar.total = target

            if len(hashes) == target and target:
                break

            hashes.append(h)
            lines = roll_north(lines)
            lines = roll_west(lines)
            lines = roll_south(lines)
            lines = roll_east(lines)
            pbar.update(1)

    weight = 0
    for y, line in enumerate(lines[::-1]):
        weight += (y + 1) * line.count('O')
    return weight


if __name__ == '__main__':
    with advent.get_input() as f:
        data = f.read().strip().splitlines()

    assert_debug(DEBUG.splitlines(), 136, p1)
    advent.print_answer(1, p1(data))
    assert_debug(DEBUG.splitlines(), 64, p2)
    advent.print_answer(2, p2(data))
