from collections import defaultdict
import queue
import re


def get_piles_and_moves(f):
    start_conf = []
    data = f.readline()
    while not data.startswith(" 1"):
        x = data
        x = re.sub(r"\s{4}", "*", x)
        x = x.replace("[", "").replace("]", "").replace(" ", "").strip()

        start_conf.append(x)
        data = f.readline()
    n_bins = int(data.strip()[-1])
    _ = f.readline()
    moves = f.read().splitlines()

    x = defaultdict(list)
    for l in start_conf:
        for i in range(n_bins):
            x[i + 1].append(l[i])

    return x, moves


class Pile:
    def __init__(self, pile):
        self.pile = queue.LifoQueue()

        for p in pile[::-1]:
            if p != "*":
                self.pile.put(p)

    def __repr__(self):
        return str(self.pile.queue)

    def pop(self):
        return self.pile.get()

    def push(self, x):
        self.pile.put(x)

    def get_top(self):
        return self.pile.queue[-1]

    def pop_stack(self, n):
        return [self.pile.get() for _ in range(n)][::-1]

    def push_stack(self, stack):
        for s in stack:
            self.pile.put(s)


def move(piles, move):
    n, _from, to = map(int, re.findall(r"\d+", move))

    for _ in range(n):
        piles[to].push(piles[_from].pop())


def move2(piles, move):
    n, _from, to = map(int, re.findall(r"\d+", move))

    piles[to].push_stack(piles[_from].pop_stack(n))


if __name__ == "__main__":
    with open("input.txt") as f:
        x, moves = get_piles_and_moves(f)

    piles = {k: Pile(v) for k, v in x.items()}

    for m in moves:
        move(piles, m)

    print("part 1:", ''.join([p.get_top() for p in piles.values()]))

    piles = {k: Pile(v) for k, v in x.items()}
    for m in moves:
        move2(piles, m)
    print("part 2:", ''.join([p.get_top() for p in piles.values()]))
