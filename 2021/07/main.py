from collections import defaultdict


with open("input.txt") as f:
    data = f.read()

data = list(map(int,data.split(",")))

def somma_n_numeri(n):
    return n*(n+1)//2


def get_fuel_constant(data):
    max_h = max(data)
    fuels = defaultdict(int)

    for position in range(max_h+1):
        for crab in data:
            fuels[position] +=abs(crab-position)
    return min(fuels.values())

def get_fuel_linear(data):
    max_h = max(data)
    fuels = defaultdict(int)

    for position in range(max_h+1):
        for crab in data:
            fuels[position] += somma_n_numeri(abs(crab-position))
    return min(fuels.values())

print("Part 1:",get_fuel_constant(data))
print("Part 2:",get_fuel_linear(data))
