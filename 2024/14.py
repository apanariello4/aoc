from functools import partial
from utils import advent
from utils.advent_debug import print_debug

advent.setup(2024, 14)

DEBUG = """p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3"""


def parse(data):
    robots = []
    for line in data.splitlines():
        p, v = line.split(' v=')
        p = tuple(map(int, p[2:].split(',')))
        v = tuple(map(int, v.split(',')))
        robots.append((p, v))
    return robots


def p1(data, H=103, W=101):

    occupied = (((x + vx * 100) % W, (y + vy * 100) % H) for (x, y), (vx, vy) in data)

    return get_score(occupied, H, W)


def get_score(occupied, H, W):
    VM = (H - 1) // 2
    HM = (W - 1) // 2
    quadrants = [0, 0, 0, 0]

    for r, c in occupied:
        if r == HM or c == VM:
            continue

        if r < VM:
            if c < HM:
                quadrants[0] += 1
            else:
                quadrants[1] += 1
        else:
            if c < HM:
                quadrants[2] += 1
            else:
                quadrants[3] += 1

    return quadrants[0] * quadrants[1] * quadrants[2] * quadrants[3]


def p2(data, H=103, W=101):
    min_score = float('inf')
    best_iteration = None
    for second in range(W * H):
        occupied = (((x + vx * second) % W, (y + vy * second) % H) for (x, y), (vx, vy) in data)

        score = get_score(occupied, H, W)

        if score < min_score:
            min_score = score
            best_iteration = second
    return best_iteration


if __name__ == '__main__':
    with advent.get_input() as f:
        data = f.read().strip()
    data = parse(data)

    print_debug(parse(DEBUG), 12, partial(p1, H=7, W=11))
    # print_debug(parse(DEBUG), 0, p2) N/A

    advent.print_answer(1, p1(data))
    advent.print_answer(2, p2(data))
