from itertools import product
from typing import Iterable, List, Set, Tuple

from utils import advent

advent.setup(2022, 18)

NODE = Tuple[int, int, int]

DEBUG_INPUT = """2,2,2
1,2,2
3,2,2
2,1,2
2,3,2
2,2,1
2,2,3
2,2,4
2,2,6
1,2,5
3,2,5
2,1,5
2,3,5"""


def parse(data: List[str]) -> Set[NODE]:

    return set(tuple(map(int, line.split(','))) for line in data)


def adjacent_3d(x: int, y: int, z: int) -> Iterable[NODE]:
    yield from ((x + 1, y, z), (x - 1, y, z), (x, y + 1, z), (x, y - 1, z), (x, y, z + 1), (x, y, z - 1))


def naive_free_faces(graph: Set[NODE]) -> int:
    free_faces = 0
    for node in graph:
        free_faces += sum((adj not in graph for adj in adjacent_3d(*node)))
    return free_faces


def get_boundary(graph: Set[NODE]) -> Tuple[range, range, range]:
    minx = miny = minz = 100000
    maxx = maxy = maxz = 0

    for x, y, z in graph:
        minx, maxx = min(x, minx), max(x, maxx)
        miny, maxy = min(y, miny), max(y, maxy)
        minz, maxz = min(z, minz), max(z, maxz)

    rangex = range(minx, maxx + 1)
    rangey = range(miny, maxy + 1)
    rangez = range(minz, maxz + 1)

    return rangex, rangey, rangez


def find_pocket_dfs(graph: Set[NODE], start_node: NODE,
                    ranges: Tuple[range]) -> Tuple[int, set]:
    stack = [start_node]
    visited = set()
    blocked_faces = 0
    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        if any(n not in r for n, r in zip(node, ranges)):
            return 0, visited

        for adj in adjacent_3d(*node):
            if adj in graph:
                blocked_faces += 1
            else:
                if adj not in visited:
                    stack.append(adj)

    return blocked_faces, visited


def free_faces(graph: Set[NODE], naive_sol: int) -> int:
    tot_blocked_faces = 0
    tot_visited = set()
    ranges = range_x, range_y, range_z = get_boundary(graph)
    for node in product(range_x, range_y, range_z):
        if node not in graph and node not in tot_visited:  # possibly a pocket
            blocked_faces, visited = find_pocket_dfs(graph, node, ranges)
            tot_visited.update(visited)
            tot_blocked_faces += blocked_faces

    return naive_sol - tot_blocked_faces


if __name__ == '__main__':
    with advent.get_input() as f:
        data = f.read().splitlines()

    graph = parse(data)
    advent.print_answer(1, n := naive_free_faces(graph))

    advent.print_answer(2, free_faces(graph, n))
