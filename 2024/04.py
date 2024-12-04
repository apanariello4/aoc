from utils import advent
from utils.advent_debug import print_debug

advent.setup(2024, 4)

DEBUG = """\
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""


def parse(data):
    return data.splitlines()

def get_all_neighbors_word(r, c, grid):
    H, W = len(grid), len(grid[0])
    neighbors = []
    if c < W - 3:
        neighbors.append(''.join((grid[r][c + i] for i in range(4))))
    if c >= 3:
        neighbors.append(''.join((grid[r][c - i] for i in range(4))))
    if r < H - 3:
        neighbors.append(''.join((grid[r + i][c] for i in range(4))))
    if r >=3:
        neighbors.append(''.join((grid[r - i][c] for i in range(4))))
    if c < W - 3 and r < H - 3:
        neighbors.append(''.join((grid[r + i][c + i] for i in range(4))))
    if c >=3 and r >=3:
        neighbors.append(''.join((grid[r - i][c - i] for i in range(4))))
    if c < W - 3 and r >=3:
        neighbors.append(''.join((grid[r - i][c + i] for i in range(4))))
    if c >=3 and r < H - 3:
        neighbors.append(''.join((grid[r + i][c - i] for i in range(4))))

    return neighbors


def get_all_neighbors_word2(r, c, grid):
    H, W = len(grid), len(grid[0])
    neighbors = []
    if c < W-1  and r < H-1 and c >= 1 and r >= 1:
        neighbors.append(''.join((grid[x][y] for x, y in ((r-1, c-1), (r, c), (r+1, c+1)))))
        neighbors.append(''.join((grid[x][y] for x, y in ((r-1, c+1), (r, c), (r+1, c-1)))))


    return neighbors

def p1(data):
    grid = data
    num_xmas = 0
    for r, row in enumerate(grid):
        for c, cell in enumerate(row):
            if cell == 'X':
                neighbors = get_all_neighbors_word(r, c, grid)
                num_xmas += neighbors.count('XMAS')
    return num_xmas


def p2(data):
    grid = data
    num_xmas = 0
    for r, row in enumerate(grid):
        for c, cell in enumerate(row):
            if cell == 'A':
                neighbors = get_all_neighbors_word2(r, c, grid)
                if sum(neighbors.count(word) for word in ('MAS', 'SAM')) == 2:
                    num_xmas += 1

    return num_xmas


if __name__ == '__main__':
    with advent.get_input() as f:
        data = f.read().strip()
    data = parse(data)

    print_debug(DEBUG.splitlines(), 18, p1)
    print_debug(DEBUG.splitlines(), 9, p2)

    advent.print_answer(1, p1(data))
    advent.print_answer(2, p2(data))
