from collections import defaultdict

from utils import advent

advent.setup(2021, 6)


def grow(data: list[int], days: int) -> int:
    population = defaultdict(int)
    for fish in data:
        population[fish] += 1
    for _ in range(days):
        new_population = {}
        for days_left in range(0, 8):
            new_population[days_left] = population[days_left + 1]
        new_population[8] = population[0]
        new_population[6] += population[0]
        population = new_population

    return sum(population.values())


if __name__ == '__main__':
    with advent.get_input() as f:
        data = f.read()

    data = list(map(int, data.split(",")))

    advent.print_answer(1, grow(data, 80))
    advent.print_answer(2, grow(data, 256))
