from utils import advent
from utils.advent_debug import print_debug

advent.setup(2023, 7)

ORDER = "23456789TJQKA"
ORDER_P2 = "J23456789TQKA"

DEBUG = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""


def sort(card: str) -> tuple[int]:
    return is_five_of_a_kind(card), is_four_of_a_kind(card), is_full_house(card), is_three_of_a_kind(card), is_two_pairs(card), is_one_pair(
        card), ORDER.index(card[0]), ORDER.index(card[1]), ORDER.index(card[2]), ORDER.index(card[3]), ORDER.index(card[4])


def sort_p2(card: str) -> tuple[int]:
    a = is_five_of_a_kind(card, joker=True), is_four_of_a_kind(card, joker=True), is_full_house(card, joker=True), is_three_of_a_kind(
        card, joker=True), is_two_pairs(card, joker=True), is_one_pair(card, joker=True)
    b = ORDER_P2.index(card[0]), ORDER_P2.index(card[1]), ORDER_P2.index(card[2]), ORDER_P2.index(card[3]), ORDER_P2.index(card[4])

    return 6 - a.index(True) if True in a else 0, b


def is_five_of_a_kind(cards: str, joker: bool = False) -> bool:
    if not joker or 'J' not in cards:
        return len(set(cards)) == 1
    else:
        return len(set(cards)) in (1, 2)


def is_four_of_a_kind(cards: str, joker: bool = False) -> bool:
    if not joker or 'J' not in cards:
        return len(set(cards)) == 2 and any(cards.count(x) == 4 for x in cards)
    else:
        if cards.count('J') == 1:
            return any(cards.count(x) == 3 for x in cards)
        elif cards.count('J') == 2:
            return any(cards.count(x) == 2 for x in cards.replace('J', ''))
        else:
            return True


def is_full_house(cards: str, joker: bool = False) -> bool:
    if not joker or 'J' not in cards:
        return len(set(cards)) == 2 and any(cards.count(x) == 3 for x in cards) and any(cards.count(x) == 2 for x in cards)
    else:
        c = cards.replace('J', '')
        if cards.count('J') == 1:
            return any(cards.count(x) == 3 for x in c) or all(cards.count(x) == 2 for x in c)
        elif cards.count('J') == 2:
            return len(set(c)) == 1 or (len(set(c)) == 2 and any(cards.count(x) == 2 for x in c))
        elif cards.count('J') == 3:
            return len(set(cards)) == 2
        else:
            return True


def is_three_of_a_kind(cards: str, joker: bool = False) -> bool:
    if not joker or 'J' not in cards:
        return len(set(cards)) == 3 and any(cards.count(x) == 3 for x in cards) and not is_full_house(cards)
    else:
        if any(cards.count(x) >= 3 for x in cards):
            return True
        if cards.count('J') == 1:
            return is_one_pair(cards)
        else:
            return True


def is_two_pairs(cards: str, joker: bool = False) -> bool:
    if not joker or 'J' not in cards:
        return len(set(cards)) == 3 and any(cards.count(x) == 2 for x in cards) and not is_full_house(cards)
    else:
        if cards.count('J') == 1:
            return any(cards.count(x) >= 2 for x in cards.replace('J', '')) and len(set(cards)) >= 3
        elif cards.count('J') == 2:
            return any(cards.count(x) >= 2 for x in cards.replace('J', ''))
        else:
            return True


def is_one_pair(cards: str, joker: bool = False) -> bool:
    if not joker or 'J' not in cards:
        return any(cards.count(x) >= 2 for x in cards)
    else:
        return True


def p1(data: list[str]) -> int:
    data.sort(key=lambda x: sort(x.split()[0]))
    tot = 0
    for i, line in enumerate(data, 1):
        _, bid = line.split()
        tot += int(bid) * i

    return tot


def p2(data: list[str]) -> int:
    data.sort(key=lambda x: sort_p2(x.split()[0]))
    tot = 0
    for i, line in enumerate(data, 1):
        _, bid = line.split()
        tot += int(bid) * i

    return tot


def optimized_solve(data: list[str]) -> int:
    # TODO
    pass


if __name__ == '__main__':
    with advent.get_input() as f:
        data = f.read().strip().splitlines()

    print_debug(DEBUG.splitlines(), 6440, p1)
    advent.print_answer(1, p1(data))
    print_debug(DEBUG.splitlines(), 5905, p2)
    advent.print_answer(2, p2(data))
