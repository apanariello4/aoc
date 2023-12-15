from utils import advent

advent.setup(2023, 10)

DEBUG = """-L|F7
7S-7|
L|7||
-L-J|
L|-JF"""

DEBUG = """...........
.S-------7.
.|F-----7|.
.||.....||.
.||.....||.
.|L-7.F-J|.
.|..|.|..|.
.L--J.L--J.
..........."""

# | is a vertical pipe connecting north and south.
# - is a horizontal pipe connecting east and west.
# L is a 90-degree bend connecting north and east.
# J is a 90-degree bend connecting north and west.
# 7 is a 90-degree bend connecting south and west.
# F is a 90-degree bend connecting south and east.
# . is ground; there is no pipe in this tile.
# S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.


def p1(data: list[str]) -> tuple[set, int]:
    # find loop
    grid = [[x for x in line] for line in data]
    starting = None
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == 'S':
                starting = (x, y)
                break
        if starting:
            break

    # find loop
    visited = set()
    x, y = starting
    direction = None
    possible_neighbors = [(0, -1), (0, 1), (1, 0), (-1, 0)]
    possible_neighbors = [(dx, dy) for dx, dy in possible_neighbors if 0 <= x + dx < len(grid[0]) and 0 <= y + dy < len(grid) and grid[y + dy][x + dx] != '.']

    for dx, dy in possible_neighbors:
        x, y = starting
        if dx == 0 and dy == -1:
            direction = 'N'
        elif dx == 0 and dy == 1:
            direction = 'S'
        elif dx == 1 and dy == 0:
            direction = 'E'
        elif dx == -1 and dy == 0:
            direction = 'W'
        visited.add((x + dx, y + dy))
        x += dx
        y += dy

        while True:
            if grid[y][x] == '|':
                if direction == 'S':
                    direction = 'S'
                    x += 0
                    y += 1
                    visited.add((x, y))
                elif direction == 'N':
                    direction = 'N'
                    x += 0
                    y -= 1
                    visited.add((x, y))
                else:
                    visited = set()
                    break
            elif grid[y][x] == '-':
                if direction == 'E':
                    direction = 'E'
                    x += 1
                    y += 0
                    visited.add((x, y))
                elif direction == 'W':
                    direction = 'W'
                    x -= 1
                    y += 0
                    visited.add((x, y))
                else:
                    visited = set()
                    break
            elif grid[y][x] == 'L':
                if direction == 'S':
                    direction = 'E'
                    x += 1
                    y += 0
                    visited.add((x, y))
                elif direction == 'W':
                    direction = 'N'
                    x += 0
                    y -= 1
                    visited.add((x, y))
                else:
                    visited = set()
                    break
            elif grid[y][x] == 'J':
                if direction == 'S':
                    direction = 'W'
                    x -= 1
                    y += 0
                    visited.add((x, y))
                elif direction == 'E':
                    direction = 'N'
                    x += 0
                    y -= 1
                    visited.add((x, y))
                else:
                    visited = set()
                    break
            elif grid[y][x] == '7':
                if direction == 'N':
                    direction = 'W'
                    x -= 1
                    y += 0
                    visited.add((x, y))
                elif direction == 'E':
                    direction = 'S'
                    x += 0
                    y += 1
                    visited.add((x, y))
                else:
                    visited = set()
                    break
            elif grid[y][x] == 'F':
                if direction == 'N':
                    direction = 'E'
                    x += 1
                    y += 0
                    visited.add((x, y))
                elif direction == 'W':
                    direction = 'S'
                    x += 0
                    y += 1
                    visited.add((x, y))
                else:
                    visited = set()
                    break

            elif grid[y][x] == 'S':
                visited.add((x, y))
                return visited, len(visited) // 2


def p2(data: str, visited: set) -> int:
    H, W = len(data), len(data[0])
    grid = [[0] * W for _ in range(H)]
    for i in visited:
        grid[i[1]][i[0]] = 1
    count = 0
    for i in range(H):
        inside = False
        for j in range(W):
            if grid[i][j]:
                if data[i][j] in "|7F":
                    inside = not inside
            elif inside:
                count += 1
    return count


def p1_optimized(data: list[str]) -> tuple[set, int]:
    W = len(data[0])
    grid = [[x for x in line] for line in data]
    starting = ''.join(data).index('S') % W, ''.join(data).index('S') // W

    mapping = {'|': {'S': (0, 1, 'S'), 'N': (0, -1, 'N')},
               '-': {'E': (1, 0, 'E'), 'W': (-1, 0, 'W')},
               'L': {'S': (1, 0, 'E'), 'W': (0, -1, 'N')},
               'J': {'S': (-1, 0, 'W'), 'E': (0, -1, 'N')},
               '7': {'N': (-1, 0, 'W'), 'E': (0, 1, 'S')},
               'F': {'N': (1, 0, 'E'), 'W': (0, 1, 'S')}}

    x, y = starting
    possible_neighbors = [(0, -1, 'N'), (0, 1, 'S'), (1, 0, 'E'), (-1, 0, 'W')]

    for dx, dy, direction in possible_neighbors:
        visited = set()
        x, y = starting
        x += dx
        y += dy
        visited.add((x, y))
        while True:
            if grid[y][x] in mapping:
                if direction in mapping[grid[y][x]]:
                    dx, dy, direction = mapping[grid[y][x]][direction]
                    x += dx
                    y += dy
                    visited.add((x, y))
                else:
                    break
            elif grid[y][x] == 'S':
                visited.add((x, y))
                return visited, len(visited) // 2
            else:
                break


if __name__ == '__main__':
    with advent.get_input() as f:
        data = f.read().strip().splitlines()

    visited, sol_p1 = p1(data)
    print(p2(DEBUG.splitlines(), p1_optimized(DEBUG.splitlines())[0]))
    advent.print_answer(1, sol_p1)
    advent.print_answer(2, p2(data, visited))
