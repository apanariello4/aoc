from utils import advent
from utils.advent_debug import print_debug

advent.setup(2024, 5)

DEBUG = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""


def parse(data):
    orders, updates = data.split('\n\n')
    orders = [tuple(map(int, x.split('|'))) for x in orders.splitlines()]
    updates = [list(map(int, x.split(','))) for x in updates.splitlines()]
    return orders, updates


def update_is_valid(order, update):
    if all(x in update for x in order):
        if update.index(order[0]) > update.index(order[1]):
            return False
    return True


def p1(data):
    orders, updates = data
    sum = 0
    for update in updates:
        if all(update_is_valid(order, update) for order in orders):
            sum += update[len(update) // 2]
    return sum


def reorder_update(orders, update):
    while not all(update_is_valid(order, update) for order in orders):
        for order in orders:
            if not update_is_valid(order, update):
                i, j = order
                i_idx = update.index(i)
                j_idx = update.index(j)
                update[i_idx], update[j_idx] = update[j_idx], update[i_idx]
    return update


def p2(data):
    orders, updates = data
    sum = 0

    for update in updates:
        if any(not update_is_valid(order, update) for order in orders):
            sum += reorder_update(orders, update)[len(update) // 2]

    return sum


def p2_optimized(data):
    from functools import cmp_to_key
    orders, updates = data
    sum = 0
    cache = {}
    for x, y in orders:
        cache[(x, y)] = -1
        cache[(y, x)] = 1

    def cmp(a, b):
        return cache.get((a, b), 0)

    for update in updates:
        if any(not update_is_valid(order, update) for order in orders):
            update.sort(key=cmp_to_key(cmp))
            sum += update[len(update) // 2]

    return sum


if __name__ == '__main__':
    with advent.get_input() as f:
        data = f.read().strip()
    data = parse(data)

    print_debug(parse(DEBUG), 143, p1)
    print_debug(parse(DEBUG), 123, p2)

    advent.print_answer(1, p1(data))
    advent.print_answer(2, p2(data))
