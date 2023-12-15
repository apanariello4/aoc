import re
from math import lcm
from typing import Iterator

from utils import advent

advent.setup(2023, 8)

DEBUG = """RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)""".splitlines()

DEBUG = """LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)
""".splitlines()

DEBUG = """LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)""".splitlines()


def infinite_iterator(data: str) -> Iterator:
    i = 0
    while True:
        yield data[i % len(data)]
        i += 1


def p1(data: list[str]) -> int:
    moves = data[0]

    all_nodes = {}
    for line in data[2:]:
        node = line.split(' = ')[0]
        all_nodes[node] = re.findall(r'\((.+), (.+)\)', line)[0]

    cur_pos = 'AAA'
    iterator = infinite_iterator(moves)
    steps = 0
    while cur_pos != 'ZZZ':
        next_move = next(iterator)
        cur_pos = all_nodes[cur_pos][0 if next_move == "L" else 1]
        steps += 1
    return steps


def p2(data: list[str]) -> int:
    moves = data[0]

    all_nodes = {}
    for line in data[2:]:
        node = line.split(' = ')[0]
        all_nodes[node] = re.findall(r'\((.+), (.+)\)', line)[0]

    positions = [n for n in all_nodes if n.endswith('A')]
    cycles = []
    iterator = infinite_iterator(moves)
    for cur_pos in positions:
        cycle = []
        steps = 0
        first_z = None
        while True:
            while not cur_pos.endswith("Z"):
                next_move = next(iterator)
                steps += 1
                cur_pos = all_nodes[cur_pos][0 if next_move == "L" else 1]

            cycle.append(steps)

            if first_z is None:
                first_z = cur_pos
                steps = 0
            elif cur_pos == first_z:
                break

        cycles.append(cycle)

    return lcm(*[cycle[0] for cycle in cycles])


if __name__ == '__main__':
    with advent.get_input() as f:
        data = f.read().strip().splitlines()

    advent.print_answer(1, p1(data))
    advent.print_answer(2, p2(data))
