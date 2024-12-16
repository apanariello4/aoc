from functools import cache

from utils import advent
from utils.advent_debug import print_debug

advent.setup(2024, 11)

DEBUG = """125 17"""


def parse(data):
    return list(map(int, data.split()))


@cache
def blink(num, steps):
    if steps == 0:
        return 1
    if num == 0:
        return blink(1, steps - 1)
    strnum = str(num)
    length = len(strnum)
    if length % 2 == 0:
        mid = length // 2
        l, r = int(strnum[:mid]), int(strnum[mid:])
        return blink(l, steps - 1) + blink(r, steps - 1)
    return blink(num * 2024, steps - 1)


def p1(data):
    return sum(blink(num, 25) for num in data)


def p2(data):
    return sum(blink(num, 75) for num in data)


if __name__ == '__main__':
    with advent.get_input() as f:
        data = f.read().strip()
    data = parse(data)

    print_debug(parse(DEBUG), 55312, p1)

    advent.print_answer(1, p1(data))
    advent.print_answer(2, p2(data))
