from collections import defaultdict
from typing import Dict, List, Optional, Tuple

from utils import advent

advent.setup(2022, 14)

GRID_TYPE = Dict[Tuple[int, int], int]
START = (500, 0)


def get_grid(data: List[str]) -> Tuple[GRID_TYPE, int]:
    grid = defaultdict(int)
    max_y = 0
    for line in data:
        coords = line.split(' -> ')
        for a, b in zip(coords, coords[1:]):
            x1, y1 = map(int, a.split(','))
            x2, y2 = map(int, b.split(','))
            max_y = max(max_y, max(y1, y2))
            if x1 == x2:
                step = 1 if y2 > y1 else -1
                for y in range(y1, y2 + step, step):
                    grid[(x1, y)] = 1

            elif y1 == y2:
                step = 1 if x2 > x1 else -1
                for x in range(x1, x2 + step, step):
                    grid[(x, y1)] = 1

    return grid, max_y


def plot_grid(grid: GRID_TYPE, max_y: int,
              max_x: int = 520, min_x: int = 300,
              falling_sand: Optional[Tuple[int, int]] = None) -> None:

    mapping = {0: '.', 1: '#', 2: 'o'}
    for y in range(0, max_y + 1):
        print(f'{y:>3} -> ', end=' ')
        for x in range(min_x - 5, max_x + 1):
            if falling_sand is not None and x == falling_sand[0] and y == falling_sand[1]:
                print('V', end='')
            else:
                print(mapping[grid[(x, y)]], end='')
        print()


def n_sands(data: List[str]) -> int:
    grid, max_y = get_grid(data)
    n_sand = 0
    while True:
        x, y = START
        for i in range(y, max_y + 1):
            if grid[(x, i + 1)] != 0:
                if grid[(x - 1, i + 1)] == 0:
                    x -= 1
                elif grid[(x + 1, i + 1)] == 0:
                    x += 1
                else:
                    grid[(x, i)] = 2
                    n_sand += 1
                    break
            if i == max_y:
                return n_sand


def part_2(data: List[str]) -> int:
    grid, max_y = get_grid(data)
    n_sand = 0
    while True:
        x, y = START
        for i in range(y, max_y + 2):
            if grid[(x, i)] != 0 and i == 0:
                return n_sand
            if grid[(x, i + 1)] != 0:
                if grid[(x - 1, i + 1)] == 0:
                    x -= 1
                elif grid[(x + 1, i + 1)] == 0:
                    x += 1
                else:
                    grid[(x, i)] = 2
                    n_sand += 1
                    break

            if i == max_y + 1:
                grid[(x, i)] = 2
                n_sand += 1
                break


if __name__ == '__main__':
    with advent.get_input() as f:
        data = f.read().splitlines()

    advent.print_answer(1, n_sands(data))
    advent.print_answer(2, part_2(data))
