from collections import deque
from typing import Iterable

from utils import advent

advent.setup(2022, 12)


ADJ = ((0, 1), (0, -1), (1, 0), (-1, 0))

MAZE = list[list[int]]
COORD = tuple[int, int]


def parse(data: list[str]) -> tuple[MAZE, COORD, COORD]:
    maze = [[c for c in line] for line in data]

    for r, row in enumerate(maze):
        for c, col in enumerate(row):
            if col == 'S':
                start = (r, c)
                maze[r][c] = 'a'
            elif col == 'E':
                end = (r, c)
                maze[r][c] = 'z'
            maze[r][c] = ord(maze[r][c]) - ord('a')

    return maze, start, end


def BFS(maze: MAZE, start: COORD, end: COORD) -> int:
    H, W = len(maze), len(maze[0])
    queue: Iterable[tuple[COORD, int]] = deque([(start, 0)])
    visited = set()

    while queue:
        cur_node, steps = queue.popleft()

        if cur_node == end:
            return steps

        if cur_node not in visited:
            visited.add(cur_node)

            r, c = cur_node
            for dr, dc in ADJ:
                next_row, next_col = (r + dr, c + dc)
                if (next_row, next_col) in visited:
                    continue

                if not (0 <= next_col < W and 0 <= next_row < H):
                    continue

                if maze[next_row][next_col] > maze[r][c] + 1:
                    continue

                queue.append(((next_row, next_col), steps + 1))

    return 1000  # unreachable


def shortest_trail(maze: MAZE, end: COORD) -> int:
    all_starts = [(r, c) for r, row in enumerate(maze) for c, col in enumerate(row) if col == 0]
    return min(BFS(maze, start, end) for start in all_starts)


if __name__ == '__main__':
    with advent.get_input() as f:
        data = f.read().splitlines()

    maze, start, end = parse(data)

    advent.print_answer(1, BFS(maze, start, end))
    advent.print_answer(2, shortest_trail(maze, end))
