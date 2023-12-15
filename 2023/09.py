from utils import advent

advent.setup(2023, 9)

DEBUG = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45"""


def p1(data: list[str]) -> int:
    tot = 0
    for line in data:
        history = [list(map(int, line.split()))]
        while len(set(history[-1])) > 1:
            next_line = [history[-1][i + 1] - history[-1][i] for i in range(len(history[-1]) - 1)]
            history.append(next_line)
        k = history[-1][0]
        for i in range(len(history) - 2, -1, -1):
            k += history[i][-1]
        tot += k
    return tot


def p2(data: list[str]) -> int:
    tot = 0
    for line in data:
        history = [list(map(int, line.split()))]
        while len(set(history[-1])) > 1:
            next_line = [history[-1][i + 1] - history[-1][i] for i in range(len(history[-1]) - 1)]
            history.append(next_line)
        k = history[-1][0]
        for i in range(len(history) - 2, -1, -1):
            k = history[i][0] - k
        tot += k
    return tot


if __name__ == '__main__':
    with advent.get_input() as f:
        data = f.read().strip().splitlines()

    advent.print_answer(1, p1(data))
    advent.print_answer(2, p2(data))
