
from collections import deque

try:
    from tqdm import tqdm
except ImportError:
    def tqdm(x):
        return x

from utils import advent
from utils.advent_debug import print_debug

advent.setup(2023, 16)

DEBUG = r""".|...\....
|.-.\.....
.....|-...
........|.
..........
.........\
..../.\\..
.-.-/..|..
.|....-|.\
..//.|...."""


def solve(data: list[str], start: tuple[int, int, int, int]) -> int:
    seen = set()
    q = deque([start])
    while q:
        r, c, dr, dc = q.popleft()
        r += dr
        c += dc
        if not (0 <= r < len(data) and 0 <= c < len(data[r])):
            continue

        if data[r][c] == '.' or (data[r][c] == '-' and dc != 0) or (data[r][c] == '|' and dr != 0):
            if (r, c, dr, dc) not in seen:
                seen.add((r, c, dr, dc))
                q.append((r, c, dr, dc))
        elif data[r][c] == '|':
            if (r, c, -1, 0) not in seen:
                seen.add((r, c, -1, 0))
                q.append((r, c, -1, 0))
            if (r, c, 1, 0) not in seen:
                seen.add((r, c, 1, 0))
                q.append((r, c, 1, 0))
        elif data[r][c] == '-':
            if (r, c, 0, -1) not in seen:
                seen.add((r, c, 0, -1))
                q.append((r, c, 0, -1))
            if (r, c, 0, 1) not in seen:
                seen.add((r, c, 0, 1))
                q.append((r, c, 0, 1))
        elif data[r][c] == '/':
            if (r, c, -dc, -dr) not in seen:
                seen.add((r, c, -dc, -dr))
                q.append((r, c, -dc, -dr))
        elif data[r][c] == '\\':
            if (r, c, dc, dr) not in seen:
                seen.add((r, c, dc, dr))
                q.append((r, c, dc, dr))

    return len({(r, c) for r, c, _, _ in seen})


def print_grid(data: list[str], seen: set[tuple[int, int]]) -> None:
    s = ''
    for r, row in enumerate(data):
        for c, col in enumerate(row):
            if (r, c) in seen:
                s += '#'
            else:
                s += '.'
        s += '\n'
    print(s)


def p1(data: list[str]) -> int:
    # r c dr dc
    start = (0, -1, 0, 1)
    return solve(data, start)


def p2(data: list[str]) -> int:
    possible_starts = [(i, -1, 0, 1) for i in range(len(data[0]))]
    possible_starts += [(-1, i, 1, 0) for i in range(len(data))]
    possible_starts += [(len(data), i, -1, 0) for i in range(len(data))]
    possible_starts += [(i, len(data[0]), 0, -1) for i in range(len(data[0]))]

    return max(solve(data, start) for start in tqdm(possible_starts))


if __name__ == '__main__':
    with advent.get_input() as f:
        data = f.read().strip().splitlines()

    print_debug(DEBUG.splitlines(), 46, p1)
    advent.print_answer(1, p1(data))
    print_debug(DEBUG.splitlines(), 51, p2)
    advent.print_answer(2, p2(data))
