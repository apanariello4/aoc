
from collections import defaultdict


with open("input.txt") as f:
    data = f.read()

data = list(map(int,data.split(",")))


def grow(days:int):
    population = defaultdict(int)
    for fish in data:
        population[fish] += 1
    for _ in range(days):
        new_population = {}
        for days_left in range(0,8):
            new_population[days_left] = population[days_left+1]
        new_population[8] = population[0]
        new_population[6] += population[0]
        population = new_population

    return sum(population.values())


print("Part 1:", grow(80), " Part 2:", grow(256))
