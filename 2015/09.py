import itertools
from utils import advent

advent.setup(2015, 9)


def get_unique_locations(lines: list[str]) -> set[str]:
    locations = set()
    for line in lines:
        locations.add(line.split(' ')[0])
        locations.add(line.split(' ')[2])
    return locations


def get_distances(lines: list[str]) -> dict[tuple[str, str], int]:
    distances = {}
    for line in lines:
        a, _, b, _, dist = line.split(' ')
        distances[(a, b)] = int(dist)
        distances[(b, a)] = int(dist)
    return distances


def get_min_and_max_route_distance(locations: set[str], distances: dict[tuple[str, str], int]) -> tuple[int, int]:
    routes = list(itertools.permutations(locations))
    distances = [sum(distances[(a, b)] for a, b in zip(route, route[1:])) for route in routes]

    return min(distances), max(distances)


if __name__ == '__main__':
    with advent.get_input() as f:
        lines = f.read().splitlines()

    locations = get_unique_locations(lines)
    distances = get_distances(lines)

    p1, p2 = get_min_and_max_route_distance(locations, distances)

    advent.submit_answer(1, p1)
    advent.submit_answer(2, p2)
