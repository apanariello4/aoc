from collections import defaultdict

from utils import advent
from utils.advent_debug import print_debug

advent.setup(2024, 8)

DEBUG = """\
............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............"""



def parse(data):
    H, W = len(data.splitlines()), len(data.splitlines()[0])
    grid = defaultdict(lambda: '.')
    antennas = defaultdict(list)
    for r, row in enumerate(data.splitlines()):
        for c, cell in enumerate(row):
            if cell != '.':
                antennas[cell].append((r, c))
                grid[(r, c)] = cell

    return grid, antennas, (H, W)

def p1(data):
    _, antennas, (H, W) = data
    antinodes = set()

    for array in antennas.values():
        for i in range(len(array)):
            for j in range(i + 1, len(array)):
                r1, c1 = array[i]
                r2, c2 = array[j]
                r0 = 2 * r1 - r2
                c0 = 2 * c1 - c2
                if 0 <= r0 < H and 0 <= c0 < W:
                    antinodes.add((r0, c0))
                r3 = 2 * r2 - r1
                c3 = 2 * c2 - c1
                if 0 <= r3 < H and 0 <= c3 < W:
                    antinodes.add((r3, c3))

    return len(antinodes)




def p2(data):
    _, antennas, (H, W) = data
    antinodes = set()

    for array in antennas.values():
        for i in range(len(array)):
            for j in range(i + 1, len(array)):
                r1, c1 = array[i]
                r2, c2 = array[j]
                dr0 = r1 - r2
                dc0 = c1 - c2
                r0 = r1
                c0 = c1
                while 0 <= r0 < H and 0 <= c0 < W:
                    antinodes.add((r0, c0))
                    r0 += dr0
                    c0 += dc0

                dr3 = r2 - r1
                dc3 = c2 - c1
                r3 = r2
                c3 = c2
                while 0 <= r3 < H and 0 <= c3 < W:
                    antinodes.add((r3, c3))
                    r3 += dr3
                    c3 += dc3

    return len(antinodes)


if __name__ == '__main__':
    with advent.get_input() as f:
        data = f.read().strip()
    data = parse(data)

    print_debug(parse(DEBUG), 14, p1)
    print_debug(parse(DEBUG), 34, p2)

    advent.print_answer(1, p1(data))
    advent.print_answer(2, p2(data))
