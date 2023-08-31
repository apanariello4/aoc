import re
from collections import defaultdict
from functools import partial
from itertools import combinations, product
from math import inf as INFINITY

from utils import advent

advent.setup(2022, 16)


def parse(data):
    pattern = re.compile(r'Valve (\w+) has flow rate=(\d+); tunnels? leads? to valves? (.*)')
    flow = {}
    tunnels = {}
    for line in data:
        valve, f, t = pattern.match(line).groups()
        f = int(f)
        t = t.split(', ')
        flow[valve] = f
        tunnels[valve] = t
    return flow, tunnels


def make_graph(data):
    flow, tunnels = data
    n_valves = len(flow)
    graph = [[0] * n_valves for _ in range(n_valves)]
    for i, valve in enumerate(flow):
        for j, other in enumerate(flow):
            if other in tunnels[valve]:
                graph[i][j] = 1
    return graph


def floyd_warshall(graph):
    dist = defaultdict(lambda: defaultdict(lambda: INFINITY))
    for a, bs in graph.items():
        dist[a][a] = 0
        for b in bs:
            dist[a][b] = 1
            dist[b][b] = 0
    for a, b, c in product(graph, graph, graph):
        bc, ba, ac = dist[b][c], dist[b][a], dist[a][c]

        if ba + ac < bc:
            dist[b][c] = ba + ac
    return dist


def score(rates, valves):
    s = 0
    for v, t in valves.items():
        s += rates[v] * t
    return s


def solutions(distance, rates, valves, time=30, cur='AA', chosen={}):
    for nxt in valves:
        new_time = time - distance[cur][nxt] - 1
        if new_time < 2:
            continue

        new_chosen = chosen | {nxt: new_time}
        yield from solutions(distance, rates, valves - {nxt}, new_time, nxt, new_chosen)

    yield chosen


if __name__ == '__main__':
    with advent.get_input() as f:
        data = f.read().splitlines()

    flows, paths = parse(data)
    dists = floyd_warshall(paths)
    good = frozenset(filter(flows.get, paths))
    score = partial(score, flows)
    best = max(map(score, solutions(dists, flows, good)))
    print(best)

    maxscore = defaultdict(int)

    for solution in solutions(dists, flows, good, 26):
        k = frozenset(solution)
        s = score(solution)

        if s > maxscore[k]:
            maxscore[k] = s

    best = max(sa + sb for (a, sa), (b, sb) in combinations(maxscore.items(), 2) if not a & b)

    print(best)

    # 1751
    # 2207
