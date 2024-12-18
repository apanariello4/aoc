from collections import deque
from functools import partial

from utils import advent
from utils.advent_debug import print_debug
from utils.utils import in_bounds, neighbors4

advent.setup(2024, 18)

DEBUG = """5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0"""


def parse(data):
    return [tuple(map(int, x.split(','))) for x in data.splitlines()]


def p1(data, HW=70, steps=1024):
    H, W = HW, HW

    grid = {(y, x) for x, y in data[:steps]}

    sr, sc = 0, 0
    er, ec = H, W

    q = deque([(0, sr, sc)])
    visited = set((sr, sc))

    while q:
        st, r, c = q.popleft()

        for dr, dc in neighbors4():
            nr, nc = r + dr, c + dc
            if not in_bounds(nr, nc, H+1, W+1) or (nr, nc) in visited:
                continue
            if nr == er and nc == ec:
                return st + 1
            if (nr, nc) not in grid:
                visited.add((nr, nc))
                q.append((st + 1, nr, nc))

    return False


def p2(data, HW=70, start=1024):
    low, high = start, len(data) - 1

    while low < high:
        mid = (low + high) // 2
        if p1(data, HW=HW, steps=mid+1):
            low = mid + 1
        else:
            high = mid

    return ','.join(str(x) for x in data[low])


if __name__ == '__main__':
    with advent.get_input() as f:
        data = f.read().strip()
    data = parse(data)

    print_debug(parse(DEBUG), 22, partial(p1, HW=6, steps=12))
    print_debug(parse(DEBUG), '6,1', partial(p2, HW=6, start=12))

    advent.print_answer(1, p1(data))
    advent.print_answer(2, p2(data))
