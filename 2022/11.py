import operator
import re
from copy import deepcopy
from math import lcm
from typing import Callable, Optional

from utils import advent

advent.setup(2022, 11)


class Monkey:
    id: int
    items: list[int]
    op: Callable
    value: Optional[int]
    test_val: int
    target_monkey: dict[bool, int]

    def __init__(self, string: str):
        self.parse_input(string)
        self.n_inspected = 0

    def parse_input(self, string: str):
        pattern = re.compile(r'Monkey (\d+):'
                             r'\s+Starting items: (\d+(?:, \d+)*)'
                             r'\s+Operation: new = old (\*|\+) (\d+|\w+)'
                             r'\s+Test: divisible by (\d+)'
                             r'\s+If true: throw to monkey (\d+)'
                             r'\s+If false: throw to monkey (\d+)')

        id, items, op, value, test, if_true, if_false = pattern.match(string).groups()
        self.id = int(id)
        self.items = [int(item) for item in items.split(', ')]
        self.op = operator.add if op == '+' else operator.mul
        self.value = int(value) if value.isnumeric() else None
        self.test_val = int(test)
        self.target_monkey = {True: int(if_true), False: int(if_false)}

    def __repr__(self):
        return f'Monkey {self.id} ({self.n_inspected} inspected)'

    def turn(self, item: int) -> tuple[int, int]:
        item = self.inspect(item)

        item = item % MOD if MOD else item // 3

        return item, self.get_target(item)

    def get_target(self, item: int) -> int:
        return self.target_monkey[item % self.test_val == 0]

    def inspect(self, item: int) -> int:
        if self.value:
            return self.op(item, self.value)
        return self.op(item, item)

    def add(self, item: int):
        self.items.append(item)


def monkey_business(monkeys: list[Monkey], rounds: int, part2: bool = False):
    global MOD
    MOD = lcm(*[m.test_val for m in monkeys]) if part2 else None

    for _ in range(rounds):
        for m in monkeys:
            while m.items:
                i, target = m.turn(m.items.pop(0))
                monkeys[target].add(i)
                m.n_inspected += 1

    a, b = sorted([m.n_inspected for m in monkeys], reverse=True)[:2]
    return a * b


if __name__ == '__main__':
    with advent.get_input() as f:
        data = f.read().split('\n\n')

    monkeys = [Monkey(d) for d in data]
    og = deepcopy(monkeys)
    p1 = monkey_business(monkeys, 20)
    p2 = monkey_business(og, 1000, part2=True)

    advent.print_answer(1, p1)
    advent.print_answer(2, p2)
