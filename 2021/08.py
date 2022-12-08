from utils import advent

advent.setup(2021, 8)

KNWON_LEN = (2, 4, 3, 7)
KNOWN_LEN_MAPPING = {2: 1, 4: 4, 3: 7, 7: 8}


def get_1_4_7_8(data):
    count = 0
    for row in data:
        count += sum(l in KNWON_LEN for l in map(len, row[1].split(" ")))

    return count


def get_combination(row):

    patterns, digits = row
    p2d = {}

    patterns = tuple(frozenset(p) for p in patterns.split())
    digits = tuple(frozenset(d) for d in digits.split())

    for p in patterns:
        if len(p) in KNWON_LEN:
            p2d[p] = KNOWN_LEN_MAPPING[len(p)]

    d2p = {v: k for k, v in p2d.items()}
    # 0 -> len 6,
    # 2 -> len 5,
    # 3 -> len 5,
    # 5 -> len 5,
    # 6 -> len 6,
    # 9 -> len 6

    for p in patterns:
        if len(p) not in KNWON_LEN:

            if len(p) == 5:
                # 2, 3, 5
                if len(set(p) & set(d2p[1])) == 2:
                    p2d[p] = 3
                elif len(set(p) & set(d2p[4])) == 3:
                    p2d[p] = 5
                else:
                    p2d[p] = 2
            elif len(p) == 6:
                # 0, 6, 9
                if len(set(p) & set(d2p[1])) == 1:
                    p2d[p] = 6
                elif len(set(p) & set(d2p[4])) == 4:
                    p2d[p] = 9
                else:
                    p2d[p] = 0
    total = 0

    for i, d in enumerate(digits):
        total += int(p2d[d]) * 1000 // (10 ** i)

    return total


def tot(data):
    count = 0
    for row in data:
        count += get_combination(row)
    return count


if __name__ == "__main__":
    with advent.get_input() as f:
        data = f.read().splitlines()

    data = [x.split(" | ") for x in data]

    advent.print_answer(1, get_1_4_7_8(data))
    advent.print_answer(2, tot(data))
