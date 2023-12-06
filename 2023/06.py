import math
import re

from utils import advent

advent.setup(2023)

try:
    from tqdm import trange
except ImportError:
    trange = range

DEBUG = """Time:      7  15   30
Distance:  9  40  200"""


def p1(data: list[str]) -> int:
    tot = []
    times = data[0].split(': ')[1].split()
    distances = data[1].split(': ')[1].split()
    for t, d in zip(times, distances):
        t = int(t)
        d = int(d)
        n_ways = 0
        for stop_time in range(1, t):
            speed = stop_time
            remaining = t - stop_time
            if speed * remaining > d:
                n_ways += 1
        tot.append(n_ways)
    return math.prod(tot)


def p2(data: list[str]) -> int:
    tot = []
    times = data[0].split(': ')[1].split()
    distances = data[1].split(': ')[1].split()
    times = int(''.join(times))
    distances = int(''.join(distances))

    n_ways = 0
    for stop_time in trange(1, times):
        speed = stop_time
        remaining = times - stop_time
        if speed * remaining > distances:
            n_ways += 1
    tot.append(n_ways)
    return math.prod(tot)


def optimized_solve(data: list[str], part2: bool) -> int:
    n_ways = []
    times = re.findall(r'\d+', data[0])
    distances = re.findall(r'\d+', data[1])
    if part2:
        times = re.findall(r'\d+', data[0].replace(' ', ''))
        distances = re.findall(r'\d+', data[1].replace(' ', ''))

    times = map(int, times)
    distances = map(int, distances)

    for t, d in zip(times, distances):
        delta = math.sqrt(t**2 - 4 * d)
        a, b = (t + delta) / 2, (t - delta) / 2
        n_ways.append(math.ceil(a) - math.floor(b) - 1)
    return math.prod(n_ways)


if __name__ == '__main__':
    with advent.get_input() as f:
        data = f.read().splitlines()

    advent.print_answer(1, optimized_solve(data, False))
    advent.print_answer(2, optimized_solve(data, True))
