from utils import advent

advent.setup(2023, 4)

DEBUG = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""


def p1(data: list[str]) -> int:
    tot = 0
    for i, line in enumerate(data):
        w = 0
        line = line.split(': ')[1]
        winning, mine = line.split(' | ')
        winning = [int(n) for n in winning.split()]
        mine = [int(n) for n in mine.split()]

        for num in mine:
            if num in winning:
                w += 1
        tot += 0 if w == 0 else 2 ** (w - 1)
    return tot


def p2(data: list[str]) -> int:
    instances = [1] * len(data)
    for i, line in enumerate(data):
        w = 0
        line = line.split(': ')[1]
        winning, mine = line.split(' | ')
        winning = [int(n) for n in winning.split()]
        mine = [int(n) for n in mine.split()]

        for num in mine:
            if num in winning:
                w += 1
        for k in range(i + 1, min(i + w + 1, len(data))):
            instances[k] += instances[i]
    return sum(instances)


def optimized_solve(data: list[str]) -> tuple[int, int]:
    p1 = 0
    instances = [1] * len(data)
    for i, line in enumerate(data):
        winning, mine = line[line.find(':') + 1:].split(' | ')
        matching = len(set(winning.split()) & set(mine.split()))

        p1 += int(2 ** (matching - 1))
        for k in range(i + 1, min(i + matching + 1, len(data))):
            instances[k] += instances[i]
    return p1, sum(instances)


if __name__ == '__main__':
    with advent.get_input() as f:
        data = f.read().splitlines()

    print(optimized_solve(data))
    advent.print_answer(1, p1(data))
    advent.print_answer(2, p2(data))
