from utils import advent
from utils.advent_debug import print_debug

advent.setup(2024, 3)

# DEBUG = """xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"""
DEBUG = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"


def parse(data):
    return data


import re
pattern = re.compile(r'mul\((\d+),(\d+)\)')
def p1(data):
    return sum(int(a) * int(b) for a, b in pattern.findall(data))


def p2(data):
    sum = 0
    dos = re.compile(r"do\(\)")
    donts = re.compile(r"don't\(\)")

    dos_idxs = [m.start() for m in dos.finditer(data)]
    donts_idxs = [m.start() for m in donts.finditer(data)]

    do = True
    for i in range(len(data)):
        if i in dos_idxs:
            do = True
        elif i in donts_idxs:
            do = False

        if do:
            if m := pattern.match(data, i):
                a, b = m.groups()
                sum += int(a) * int(b)

    return sum

if __name__ == '__main__':
    with advent.get_input() as f:
        data = f.read().strip()
    data = parse(data)

    print_debug(DEBUG, 161, p1)
    print_debug(DEBUG, 48, p2)

    advent.print_answer(1, p1(data))
    advent.print_answer(2, p2(data))
