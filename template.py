from utils import advent
from utils.advent_debug import print_debug

advent.setup(2024, 0)

DEBUG = """"""


def parse(data):
    return data.splitlines()


def p1(data):
    return 0


def p2(data):
    return 0


if __name__ == '__main__':
    with advent.get_input() as f:
        data = f.read().strip()
    data = parse(data)

    print_debug(parse(DEBUG), 13, p1)
    print_debug(parse(DEBUG), 31, p2)

    advent.print_answer(1, p1(data))
    advent.print_answer(2, p2(data))
