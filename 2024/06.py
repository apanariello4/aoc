

from utils import advent
from utils.advent_debug import print_debug

advent.setup(2024, 6)

DEBUG = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""


def parse(data):
    return [list(x) for x in data.splitlines()]


def next_dir(x, y):
    return y, -x


def p1(data):
    for r, row in enumerate(data):
        if '^' in row:
            startpos = (r, row.index('^'))
            break

    seen = set()
    dr, dc = -1, 0
    r, c = startpos

    while True:
        seen.add((r, c))
        if not (0 <= c + dc < len(data[0]) and 0 <= r + dr < len(data)):
            break

        if data[r + dr][c + dc] == '#':
            dr, dc = next_dir(dr, dc)
        else:
            c, r = c + dc, r + dr

    return len(seen)


def check_loop(grid, startpos):
    r, c = startpos
    dr, dc = -1, 0
    seen = set()

    while True:
        seen.add((r, c, dr, dc))
        if not (0 <= r + dr < len(grid) and 0 <= c + dc < len(grid[0])):
            break

        if grid[r + dr][c + dc] == '#':
            dr, dc = next_dir(dr, dc)
        else:
            c, r = c + dc, r + dr

        if (r, c, dr, dc) in seen:
            return True

    return False


def p2(data):

    for r, row in enumerate(data):
        if '^' in row:
            startpos = (r, row.index('^'))
            break

    ans = 0
    seen = set()
    r, c = startpos
    dr, dc = -1, 0
    while True:
        seen.add((r, c))
        if not (0 <= c + dc < len(data[0]) and 0 <= r + dr < len(data)):
            break

        if data[r + dr][c + dc] == '#':
            dr, dc = next_dir(dr, dc)
        else:
            c, r = c + dc, r + dr

    for r, row in enumerate(data):
        for c, char in enumerate(row):
            if char != '.' or (r, c) not in seen:
                continue
            data[r][c] = '#'
            ans += check_loop(data, startpos)
            data[r][c] = '.'

    return ans


if __name__ == '__main__':
    with advent.get_input() as f:
        data = f.read().strip()
    data = parse(data)

    print_debug(parse(DEBUG), 41, p1)
    print_debug(parse(DEBUG), 6, p2)

    advent.print_answer(1, p1(data))
    advent.print_answer(2, p2(data))
