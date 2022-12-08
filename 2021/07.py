from collections import defaultdict

from utils import advent

advent.setup(2021, 7)


def sum_first_n_nums(n: int):
    return n * (n + 1) // 2


def get_fuel_constant(data: list[int]) -> int:
    max_h = max(data)
    fuels = defaultdict(int)

    for position in range(max_h + 1):
        for crab in data:
            fuels[position] += abs(crab - position)
    return min(fuels.values())


def get_fuel_linear(data: list[int]) -> int:
    max_h = max(data)
    fuels = defaultdict(int)

    for position in range(max_h + 1):
        for crab in data:
            fuels[position] += sum_first_n_nums(abs(crab - position))
    return min(fuels.values())


if __name__ == '__main__':
    with advent.get_input() as f:
        data = f.read()

    data = list(map(int, data.split(",")))

    advent.print_answer(1, get_fuel_constant(data))
    advent.print_answer(2, get_fuel_linear(data))
