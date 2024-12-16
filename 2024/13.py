import re

from utils import advent
from utils.advent_debug import print_debug

advent.setup(2024, 13)

DEBUG = """Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279
"""


def parse(data):
    return [tuple(map(int, re.findall(r'\d+', comb))) for comb in data.split('\n\n')]


def p1(data):
    res = 0
    for comb in data:
        a_x, a_y, b_x, b_y, p_x, p_y = comb

        x = (p_x * b_y - p_y * b_x) / (a_x * b_y - a_y * b_x)
        y = (p_y - x * a_y) / b_y

        if x % 1 == y % 1 == 0:
            res += int(3 * x + y)
    return res


def p2(data):

    res = 0
    for comb in data:
        a_x, a_y, b_x, b_y, p_x, p_y = comb
        p_x += 10000000000000
        p_y += 10000000000000

        x = (p_x * b_y - p_y * b_x) / (a_x * b_y - a_y * b_x)
        y = (p_y - x * a_y) / b_y

        if x % 1 == y % 1 == 0:
            res += int(3 * x + y)
    return res


if __name__ == '__main__':
    with advent.get_input() as f:
        data = f.read().strip()
    data = parse(data)

    print_debug(parse(DEBUG), 480, p1)
    print_debug(parse(DEBUG), 875318608908, p2)

    advent.print_answer(1, p1(data))
    advent.print_answer(2, p2(data))
