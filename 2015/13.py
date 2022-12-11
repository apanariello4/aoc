import re
from itertools import permutations

from utils import advent

advent.setup(2015, 13)


def get_unique_people(lines: list[str]) -> set[str]:
    return set(line.split(' ')[0] for line in lines)


def get_happiness_mapping(lines: list[str]) -> dict[tuple[str, str], int]:
    happiness = {}
    pattern = re.compile(r'(\w+) would (gain|lose) (\d+) happiness units by sitting next to (\w+).')
    for line in lines:
        a, gain_lose, value, b = pattern.match(line).groups()
        happiness[(a, b)] = int(value) * (1 if gain_lose == 'gain' else -1)
    return happiness


def get_happiness_of_table(table: tuple[str], happiness: dict[tuple[str, str], int]) -> int:
    h = 0
    for a, b in zip(table, table[1:]):
        h += happiness[(a, b)]
        h += happiness[(b, a)]
    h += happiness[(table[0], table[-1])]
    h += happiness[(table[-1], table[0])]
    return h


def get_max_happiness(tables: permutations, happiness: dict[tuple[str, str], int]) -> int:
    return max(get_happiness_of_table(table, happiness) for table in tables)


if __name__ == '__main__':
    with advent.get_input() as f:
        lines = f.read().splitlines()

    people = get_unique_people(lines)
    happiness = get_happiness_mapping(lines)
    tables = permutations(people)

    advent.print_answer(1, get_max_happiness(tables, happiness))

    people.add('me')
    happiness.update({(person, 'me'): 0 for person in people})
    happiness.update({('me', person): 0 for person in people})
    tables = permutations(people)

    advent.print_answer(2, get_max_happiness(tables, happiness))
