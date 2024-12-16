from collections import deque
from utils import advent
from utils.advent_debug import print_debug
from utils.utils import neighbors4, neighbors4_coords, in_bounds

advent.setup(2024, 12)

DEBUG = """RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE
"""


def parse(data):
    return [list(line) for line in data.splitlines()]

def connected_components(data):
    regions = []
    seen = set()
    H, W = len(data), len(data[0])
    for r, row in enumerate(data):
        for c, cell in enumerate(row):
            if (r, c) in seen:
                continue
            seen.add((r, c))
            region = {(r, c)}

            q = deque([(r, c)])

            while q:
                rr, cc = q.popleft()
                for dr, dc in neighbors4():
                    new_coord = nr, nc = rr + dr, cc + dc
                    if in_bounds(nr, nc, H, W) and new_coord not in seen and data[nr][nc] == cell:
                        seen.add(new_coord)
                        region.add(new_coord)
                        q.append(new_coord)
            seen.update(region)
            regions.append(region)
    return regions

def perimeter(region):
    output = 0
    for (r, c) in region:
        for nr, nc in neighbors4_coords(r, c):
            if (nr, nc) not in region:
                output += 1
    return output

def p1(data):
    regions = connected_components(data)

    return sum(perimeter(region) * len(region) for region in regions)


def sides(region):
    corner_candidates = set()
    for r, c in region:
        for cr, cc in ((r - 0.5, c - 0.5), (r + 0.5, c - 0.5), (r + 0.5, c + 0.5), (r - 0.5, c + 0.5)):
            corner_candidates.add((cr, cc))
    corners = 0
    for cr, cc in corner_candidates:
        config = ((sr, sc) in region for sr, sc in ((cr - 0.5, cc - 0.5), (cr + 0.5, cc - 0.5), (cr + 0.5, cc + 0.5), (cr - 0.5, cc + 0.5)))
        number = sum(config)
        if number in (1, 3):
            corners += 1
        elif number == 2 and config in ([True, False, True, False], [False, True, False, True]):
            corners += 2
    return corners

def p2(data):
    regions = connected_components(data)

    return sum(sides(region) * len(region) for region in regions)



if __name__ == '__main__':
    with advent.get_input() as f:
        data = f.read().strip()
    data = parse(data)

    print_debug(parse(DEBUG), 1930, p1)
    print_debug(parse(DEBUG), 1206, p2)

    advent.print_answer(1, p1(data))
    advent.print_answer(2, p2(data))
