from collections import defaultdict

from utils import advent
from utils.advent_debug import print_debug

advent.setup(2023, 15)

DEBUG = """rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"""


def hash(c: str) -> int:
    h = 0
    for x in c:
        h = (h + ord(x)) * 17 % 256
    return h


def p1(data: str) -> int:
    return sum(map(hash, data.split(',')))


def p2(data: str) -> int:
    boxes = defaultdict(dict)
    for step in data.split(','):
        if '=' in step:
            label, value = step.split('=')
            box = hash(label)
            value = int(value)
            boxes[box][label] = value

        elif '-' in step:
            label = step[:-1]
            box = hash(label)
            if box in boxes:
                if label in boxes[box]:
                    del boxes[box][label]
    tot = 0
    for box, lenses in boxes.items():
        tot += sum((1 + box) * i * value for i, value in enumerate(lenses.values(), 1))

    return tot


if __name__ == '__main__':
    with advent.get_input() as f:
        data = f.read().strip()

    print_debug(DEBUG, 1320, p1)
    advent.print_answer(1, p1(data))
    print_debug(DEBUG, 145, p2)
    advent.print_answer(2, p2(data))
