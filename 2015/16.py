import operator
import re

from utils import advent

advent.setup(2015, 16)

A = {"children": 3,
     "cats": 7,
     "samoyeds": 2,
     "pomeranians": 3,
     "akitas": 0,
     "vizslas": 0,
     "goldfish": 5,
     "trees": 3,
     "cars": 2,
     "perfumes": 1}

OP = {"cats": operator.gt,
      "trees": operator.gt,
      "pomeranians": operator.lt,
      "goldfish": operator.lt}


def is_sue_part1(p_v) -> bool:
    return all(A[prop] == int(value) for prop, value in p_v)


def is_sue_part2(p_v) -> bool:
    return all(OP.get(prop, operator.eq)(A[prop], int(value)) for prop, value in p_v)


def find_sue(data: str) -> int:
    pattern = re.compile(r'Sue (\d+): (\w+): (\d+), (\w+): (\d+), (\w+): (\d+)')
    sue_part1 = None
    sue_part2 = None
    for line in data:
        sue_number, p1, v1, p2, v2, p3, v3 = pattern.match(line).groups()
        p_v = list(zip((p1, p2, p3), (v1, v2, v3)))
        if not sue_part1 and is_sue_part1(p_v):
            sue_part1 = sue_number
        if not sue_part2 and is_sue_part2(p_v):
            sue_part2 = sue_number

        if sue_part1 and sue_part2:
            return sue_part1, sue_part2


if __name__ == '__main__':
    with advent.get_input() as f:
        data = f.read().splitlines()
    p1, p2 = find_sue(data)
    advent.print_answer(1, p1)
    advent.submit_answer(2, p2)
