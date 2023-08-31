import re
import time
from collections import defaultdict

from utils import advent

advent.setup(2022, 15)

DEBUG = """Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3""".splitlines()


def parse(data):
    pattern = re.compile(r'Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)')

    return [tuple(map(int, pattern.match(line).groups())) for line in data]


def l1_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


def get_coords_filled_diamond(x, y, distance, y_line):
    # yield only when y == y_line
    for i in range(distance + 1):
        if y_line in (y + i, y - i):
            yield from ((x + i, y_line) for i in range(0, distance - i + 1))
            yield from ((x - i, y_line) for i in range(0, distance - i + 1))


def get_grid(sensors, y_line=2000000):
    grid = defaultdict(lambda: '.')
    occupied = set()

    for x, y, bx, by in sensors:
        grid[(x, y)] = 'S'
        grid[(bx, by)] = 'B'

    t1 = time.time()
    for x, y, bx, by in sensors:
        dist = l1_distance(x, y, bx, by)
        for cx, cy in get_coords_filled_diamond(x, y, dist, y_line):
            grid[(cx, cy)] = '#' if grid[(cx, cy)] == '.' else grid[(cx, cy)]
            if grid[(cx, cy)] == '#':
                occupied.add((cx, cy))
    print(f"Time: {time.time() - t1}")
    return grid, len(occupied)


def plot_grid(grid):
    min_x = min(x for x, y in grid.keys())
    max_x = max(x for x, y in grid.keys())
    min_y = min(y for x, y in grid.keys())
    max_y = max(y for x, y in grid.keys())

    for y in range(min_y, max_y + 1):
        print(f"{y:>3} ", end='')
        for x in range(min_x, max_x + 1):
            print(grid[(x, y)], end='')
        print()


def get_segment_occupied(x, y, dist, line, p2=False):
    MAX = 4000000
    w = x - dist
    e = x + dist
    s = y + dist
    n = y - dist

    if n <= line <= s:
        d = abs(line - y)
        w = max(0, w + d) if p2 else w + d
        e = min(MAX, e - d) if p2 else e - d
        return [w, e]

    return None


def merge_segments(segments):
    segments.sort()
    it = iter(segments)
    q = [next(it)]
    for lo, hi in it:
        qlo, qhi = q[-1]

        if lo > qhi + 1:
            q.append([lo, hi])
            continue

        q[-1][1] = max(qhi, hi)

    return tuple(q[-1])


def p1_fast(sensors, y_line=2000000):
    segments = []
    for x, y, bx, by in sensors:
        dist = l1_distance(x, y, bx, by)
        seg = get_segment_occupied(x, y, dist, y_line)

        if seg is None:
            continue

        segments.append(seg)

    return merge_segments(segments)


def p2(sensors):
    MAX = 4000000
    for y_line in range(0, MAX + 1):
        print(y_line, end='\r')
        space = set()
        segments = []

        for sx, sy, bx, by in sensors:
            dist = l1_distance(sx, sy, bx, by)
            seg = get_segment_occupied(sx, sy, dist, y_line, p2=True)
            if seg is None:
                continue

            segments.append(seg)

        seg = merge_segments(segments)

        for x in range(seg[0], seg[1] + 1):
            space.add((x, y_line))

        if len(space) == 0:
            continue

        return space.pop()


if __name__ == '__main__':
    with advent.get_input() as f:
        data = f.read().splitlines()

    sensors = parse(data)

    seg = p1_fast(sensors)
    advent.print_answer(1, seg[1] - seg[0] + 1)

    x, y = p2(sensors)
    ans = x * 4000000 + y
    advent.print_answer(2, ans)
