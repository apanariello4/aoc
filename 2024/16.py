import heapq

from utils import advent
from utils.advent_debug import print_debug
from utils.utils import find_in_grid

advent.setup(2024, 16)

DEBUG = """###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############
"""


def parse(data):
    return [list(line) for line in data.splitlines()]


def p1(data):
    sr, sc = find_in_grid(data, 'S')

    q = [(0, sr, sc, 0, 1)]
    seen = set((sr, sc, 0, 1))

    while q:
        cost, r, c, dr, dc = heapq.heappop(q)
        seen.add((r, c, dr, dc))

        if data[r][c] == 'E':
            return cost

        for cost, r, c, dr, dc in ((cost + 1, r + dr, c + dc, dr, dc),
                                   (cost + 1000, r, c, -dc, dr),
                                   (cost + 1000, r, c, dc, -dr)):
            if data[r][c] == '#' or (r, c, dr, dc) in seen:
                continue
            heapq.heappush(q, (cost, r, c, dr, dc))


def p2(data):
    min_cost = float('inf')
    sr, sc = find_in_grid(data, 'S')

    q = [(0, sr, sc, 0, 1, set([(sr, sc)]))]
    seen = set((sr, sc, 0, 1))

    while q:
        cost, r, c, dr, dc, path = heapq.heappop(q)
        seen.add((r, c, dr, dc))

        if data[r][c] == 'E':
            if cost < min_cost:
                min_cost = cost
                valid = path
            elif cost == min_cost:
                valid |= path
        if cost > min_cost:
            continue

        for new_cost, r, c, dr, dc in ((cost + 1, r + dr, c + dc, dr, dc),
                                       (cost + 1000, r, c, -dc, dr),
                                       (cost + 1000, r, c, dc, -dr)):
            if data[r][c] == '#' or (r, c, dr, dc) in seen:
                continue
            heapq.heappush(q, (new_cost, r, c, dr, dc, path | {(r, c)}))

    return len(valid)


if __name__ == '__main__':
    with advent.get_input() as f:
        data = f.read().strip()
    data = parse(data)

    print_debug(parse(DEBUG), 7036, p1)
    print_debug(parse(DEBUG), 45, p2)

    advent.print_answer(1, p1(data))
    advent.print_answer(2, p2(data))
