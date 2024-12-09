from utils import advent
from utils.advent_debug import print_debug

advent.setup(2024, 9)

DEBUG = """2333133121414131402"""


def parse(data):
    s = []
    num = 0
    for i, c in enumerate(data):
        amount = int(c)
        if i % 2 == 0:
            s += [num] * amount
            num += 1
        else:
            s += [-1] * amount
    return s


def parse2(data):
    files = {}
    empty = []

    pos = 0
    num = 0

    for i, c in enumerate(data):
        amount = int(c)
        if i % 2 == 0:
            files[num] = (pos, amount)
            num += 1
        else:
            if amount:
                empty.append((pos, amount))
        pos += amount

    return files, empty


def p1(data):
    empty_spaces = (i for i, x in enumerate(data) if x == -1)

    for i in empty_spaces:
        while data[-1] == -1:
            data.pop()
        if len(data) <= i:
            break
        data[i] = data.pop()

    return sum(i * x for i, x in enumerate(data))


def p2(data):
    files, empty = data
    m = max(files.keys())
    while m > 0:
        pos, size = files[m]
        for i, (start, length) in enumerate(empty):
            if start >= pos:
                empty = empty[:i]
                break
            if size <= length:
                files[m] = (start, size)
                if size < length:
                    empty[i] = (start + size, length - size)
                elif size == length:
                    empty.pop(i)
                break
        m -= 1

    checksum = 0
    for m, (pos, size) in files.items():
        for x in range(pos, pos + size):
            checksum += m * x
    return checksum


if __name__ == '__main__':
    with advent.get_input() as f:
        data = f.read().strip()
    data1 = parse(data)
    data2 = parse2(data)

    print_debug(parse(DEBUG), 1928, p1)
    print_debug(parse2(DEBUG), 2858, p2)

    advent.print_answer(1, p1(data1))
    advent.print_answer(2, p2(data2))
