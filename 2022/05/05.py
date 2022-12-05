from collections import defaultdict
import queue
import re

start_conf = []
with open("input.txt") as f:
    data = f.readline()
    while not data.startswith(" 1"):
        x = data
        x = re.sub(r"\s{4}", "*", x)
        x = x.replace("[", "").replace("]", "").replace(" ", "").strip()

        start_conf.append(x)
        data = f.readline()
    _ = f.readline()
    moves = f.read().splitlines()

x = defaultdict(list)
for l in start_conf:
    for i in range(10 - 1):
        try:
            x[i + 1].append(l[i])
        except IndexError:
            x[i + 1].append("*")


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


x_og = x.copy()
piles = {k: Pile(v) for k, v in x_og.items()}


def move(piles, move):
    n, _from, to = map(int, re.findall(r"\d+", move))

    for _ in range(n):
        piles[to].push(piles[_from].pop())


for m in moves:
    move(piles, m)

print("part 1:", ''.join([p.get_top() for p in piles.values()]))


def move2(piles, move):
    n, _from, to = map(int, re.findall(r"\d+", move))

    piles[to].push_stack(piles[_from].pop_stack(n))


piles = {k: Pile(v) for k, v in x_og.items()}
for m in moves:
    move2(piles, m)

print("part 2:", ''.join([p.get_top() for p in piles.values()]))
