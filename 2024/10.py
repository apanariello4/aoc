from utils import advent
from utils.advent_debug import print_debug

advent.setup(2024, 10)

DEBUG = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""


def parse(data):
    return [list(map(int, line)) for line in data.splitlines()]


def dfs(grid, r, c):
    H, W = len(grid), len(grid[0])
    q = [(r, c)]
    visited = set()
    while q:
        r, c = q.pop()
        if (r, c) in visited:
            continue
        visited.add((r, c))
        for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nr, nc = r + dr, c + dc
            if 0 <= nc < W and 0 <= nr < H and grid[nr][nc] == grid[r][c] + 1:
                q.append((nr, nc))

    return sum(1 for y, x in visited if grid[y][x] == 9)


def p1(data):
    grid = data
    H, W = len(grid), len(grid[0])

    trailheads = [(r, c) for r in range(H) for c in range(W) if grid[r][c] == 0]

    return sum(dfs(grid, *head) for head in trailheads)


def dfs2(grid, r, c):
    H, W = len(grid), len(grid[0])
    q = [((r, c), ((r, c),))]
    visited = set()
    paths = set()
    while q:
        node = q.pop()
        if node in visited:
            continue
        visited.add(node)
        (r, c), path = node
        if grid[r][c] == 9:
            paths.add(path)

        val = grid[r][c]

        for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < H and 0 <= nc < W and grid[nr][nc] == val + 1:
                q.append(((nr, nc), path + ((nr, nc))))

    return len(paths)


def p2(data):
    grid = data
    H, W = len(grid), len(grid[0])

    trailheads = [(r, c) for r in range(H) for c in range(W) if grid[r][c] == 0]

    return sum(dfs2(grid, *head) for head in trailheads)


if __name__ == '__main__':
    with advent.get_input() as f:
        data = f.read().strip()
    data = parse(data)

    print_debug(parse(DEBUG), 36, p1)
    print_debug(parse(DEBUG), 81, p2)

    advent.print_answer(1, p1(data))
    advent.print_answer(2, p2(data))
