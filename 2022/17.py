from collections import defaultdict
from itertools import count
import os
import time
from typing import Iterator, Tuple
from utils import advent

advent.setup(2022, 17)

COORD = Tuple[int, int]


class Figure:
    blocks: Tuple[COORD, ...]
    down: Tuple[COORD, ...]
    left: Tuple[COORD, ...]
    right: Tuple[COORD, ...]
    x: int
    y: int

    def __init__(self, start_y: int) -> None:
        self.y = start_y
        self.start_y = start_y
        self.min_x = min(self.blocks, key=lambda x: x[0])[0]
        self.max_x = max(self.blocks, key=lambda x: x[0])[0]
        self._max_y = max(self.blocks, key=lambda x: x[1])[1]

    def move_wind(self, wind_direction: str, grid: dict) -> None:
        if wind_direction == '>' and not self.collision_right(grid):
            self.x += 1

        elif wind_direction == '<' and not self.collision_left(grid):
            self.x -= 1

    def move_down(self, grid: dict) -> bool:
        if not self.collision_down(grid):
            self.y -= 1
            return True
        else:
            self.update_grid(grid)
            return False

    def update_grid(self, grid) -> None:
        for dx, dy in self.blocks:
            grid[(self.x + dx, self.y + dy)] = BLOCK_CHAR

    def collision_down(self, grid: dict) -> bool:
        if self.y == 1:
            return True
        for dx, dy in self.down:
            if grid[(self.x + dx, self.y + dy)] == BLOCK_CHAR:
                return True
        return False

    def collision_left(self, grid: dict) -> bool:

        if self.x + self.min_x == 0:
            return True
        for dx, dy in self.left:
            if grid[(self.x + dx, self.y + dy)] == BLOCK_CHAR:
                return True
        return False

    def collision_right(self, grid: dict) -> bool:
        if self.x + self.max_x == 6:
            return True
        for dx, dy in self.right:
            if grid[(self.x + dx, self.y + dy)] == BLOCK_CHAR:
                return True
        return False

    def plot(self, grid: dict) -> None:
        min_x = 0
        max_x = 6
        min_y = 1

        height_display = 20

        for y in range(self.start_y + 3, max(min_y - 1, self.start_y - height_display), -1):
            print(f"{y:>5} |", end='')
            for x in range(min_x, max_x + 1):
                if (x, y) in [(self.x + dx, self.y + dy) for dx, dy in self.blocks]:
                    print(FALLING_CHAR, end='')
                else:
                    print(grid[(x, y)], end='')
            print('|', end='')
            if y == self.start_y - 3:
                print('  <-- previous max', end='')
            print()
        print(' ' * 5, '+-------+')
        print(' ' * 6, '0123456')

    def __repr__(self) -> str:
        return f"({self.__class__.__name__} {self.x}, {self.y})"

    @property
    def max_y(self) -> int:
        return self.y + self._max_y


class Dash(Figure):
    def __init__(self, y_start: int) -> None:
        self.x = 2
        self.blocks = ((0, 0), (1, 0), (2, 0), (3, 0))
        self.down = ((0, -1), (1, -1), (2, -1), (3, -1))
        self.left = ((-1, 0),)
        self.right = ((4, 0),)
        super().__init__(y_start)


class Plus(Figure):
    def __init__(self, y_start: int) -> None:
        self.x = 3
        self.blocks = ((0, 0), (0, 1), (0, 2), (-1, 1), (1, 1))
        self.down = ((-1, 0), (0, -1), (1, 0))
        self.left = ((-2, 1), (-1, 0), (-1, 2))
        self.right = ((2, 1), (1, 0), (1, 2))
        super().__init__(y_start)


class ReverseL(Figure):
    def __init__(self, y_start: int) -> None:
        self.x = 2
        self.blocks = ((0, 0), (1, 0), (2, 0), (2, 1), (2, 2))
        self.down = ((0, -1), (1, -1), (2, -1))
        self.left = ((-1, 0), (1, 1), (1, 2))
        self.right = ((3, 0), (3, 1), (3, 2))
        super().__init__(y_start)


class Line(Figure):
    def __init__(self, y_start: int) -> None:
        self.x = 2
        self.blocks = ((0, 0), (0, 1), (0, 2), (0, 3))
        self.down = ((0, -1),)
        self.left = ((-1, 0), (-1, 1), (-1, 2), (-1, 3))
        self.right = ((1, 0), (1, 1), (1, 2), (1, 3))
        super().__init__(y_start)


class Cube(Figure):
    def __init__(self, y_start: int) -> None:
        self.x = 2
        self.blocks = ((0, 0), (0, 1), (1, 1), (1, 0))
        self.right = ((2, 0), (2, 1))
        self.left = ((-1, 0), (-1, 1))
        self.down = ((0, -1), (1, -1))
        super().__init__(y_start)


def plot_grid(figure: Figure, grid: dict, i: int,
              m: str, max_y: int, n_figure: int) -> None:
    os.system('clear')
    figure.plot(grid)
    print(f'Move {i} => {m}, max_y {max_y}, figures {n_figure}')
    time.sleep(0.05)


FIGURES = (Dash, Plus, ReverseL, Line, Cube)
BLOCK_CHAR = '#'
FALLING_CHAR = '@'


def loop(moves: str) -> Iterator[Tuple[int, str]]:
    for i in count(0):
        yield i, moves[i % len(moves)]


def check_pattern(grid, it, max_y, previous, n_figures, figure, len_data, stop):
    rocktype = FIGURES.index(figure.__class__)
    if max_y > 200:
        topchunk = []
        for x, y in grid:
            if y >= max_y - 100 and grid[(x, y)] == BLOCK_CHAR:
                topchunk.append((x, max_y - y))

        state = (tuple(sorted(topchunk)), it % len_data, rocktype)

        if state in previous:

            nn, yy = previous[state]
            delta_y = max_y - yy
            f_in_pattern = n_figures - nn
            if stop - n_figures < f_in_pattern:
                # avoid overshooting for part1
                return False

            jumps = (stop - n_figures) // f_in_pattern
            h_jump = delta_y * jumps
            n_figures_jump = f_in_pattern * jumps
            return h_jump, n_figures_jump

        previous[state] = (n_figures, max_y)
    return False


def simulation(moves: str, stop: int) -> int:
    verbose = False
    max_y = 0
    n_figure = 1
    grid = defaultdict(lambda: '.')
    figure = FIGURES[0](4)
    len_data = len(moves)
    previous = {}
    pattern = None
    for i, m in loop(moves):
        plot_grid(figure, grid, i, m, max_y, n_figure) if verbose else None
        figure.move_wind(m, grid)
        plot_grid(figure, grid, i, m, max_y, n_figure) if verbose else None

        if not figure.move_down(grid):
            max_y = max(figure.max_y, max_y)
            if n_figure == stop:
                max_y = max_y + r[0] if pattern else max_y
                print(f'Moves {i}, max_y {max_y}, figures {n_figure}') if verbose else None
                return max_y
            if not pattern and (r := check_pattern(grid, i, max_y, previous, n_figure, figure, len_data, stop)):
                n_figure += r[1]
                pattern = True

            figure = FIGURES[n_figure % len(FIGURES)](max_y + 4)
            n_figure += 1

        if (i % 10000 == 0 or n_figure == stop) and verbose:
            print(f'Moves {i}, max_y {max_y}, figures {n_figure} ({n_figure/stop:.2%})', end='\r')

    raise ValueError('No solution found')


if __name__ == '__main__':
    with advent.get_input() as f:
        moves = f.read().strip()

    advent.print_answer(1, simulation(moves, 2022))
    t1 = time.time()
    advent.print_answer(2, simulation(moves, 1000000000000))
    print(f'Time Part 2: {time.time() - t1:.2f}s')
