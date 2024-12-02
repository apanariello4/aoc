from utils import advent
from utils.advent_debug import print_debug
from collections import Counter

advent.setup(2024, 1)

DEBUG = """3   4
4   3
2   5
1   3
3   9
3   3"""


def parse(data):
    left = []
    right = []
    for line in data.splitlines():
        l, r = map(int, line.split())
        left.append(l)
        right.append(r)

    left.sort()
    right.sort()

    return left, right


def p1(data):
    left, right = data
    return sum (abs(l - r) for l, r in zip(left, right))


def p2(data):
    c = Counter(data[1])
    return sum(num * c[num] for num in data[0])


if __name__ == '__main__':
    with advent.get_input() as f:
        data = f.read().strip()
    data = parse(data)

    print_debug(parse(DEBUG), 11, p1)
    print_debug(parse(DEBUG), 31, p2)

    advent.print_answer(1, p1(data))
    advent.print_answer(2, p2(data))
