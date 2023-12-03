import itertools
import re
from collections import defaultdict
from typing import Iterator

from utils import advent

advent.setup(2023, 3)

DEBUG = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""


def get_num(line) -> tuple[int, int]:
    n = re.search(r'(\d+)', line).group(1)
    return int(n), len(n)


def get_boundary(x, y, H, W, len_num) -> Iterator[tuple[int, int]]:
    for item in itertools.product(range(max(0, x - 1), min(H, x + 2)), range(max(0, y - 1), min(W, y + len_num + 1))):
        yield item


def p1(data: list[str]) -> int:
    nums = []
    H = len(data)
    W = len(data[0])
    for i, line in enumerate(data):
        for j, char in enumerate(line):
            if not char.isdigit() or (j > 0 and line[j - 1].isdigit()):
                continue
            else:
                cur_num, num_len = get_num(line[j:])
                valid = False
                for x in range(max(0, i - 1), min(H, i + 2)):
                    for y in range(max(0, j - 1), min(W, j + num_len + 1)):
                        if data[x][y].isdigit() or data[x][y] == '.':
                            continue
                        else:
                            valid = True

                nums.append(cur_num) if valid else None
    return sum(nums)


def p2(data: list[str]) -> int:
    nums = defaultdict(list)
    H = len(data)
    W = len(data[0])
    for i, line in enumerate(data):
        for j, char in enumerate(line):
            if not char.isdigit() or (j > 0 and line[j - 1].isdigit()):
                continue
            else:
                cur_num, num_len = get_num(line[j:])
                valid = False
                for x in range(max(0, i - 1), min(H, i + 2)):
                    for y in range(max(0, j - 1), min(W, j + num_len + 1)):
                        if data[x][y].isdigit() or data[x][y] == '.':
                            continue
                        elif data[x][y] == '*':
                            coord = (x, y)
                            valid = True

                nums[coord].append(cur_num) if valid else None

    return sum([nums[key][0] * nums[key][1] for key in nums.keys() if len(nums[key]) == 2])


def solve_optimized(data: list[str]) -> tuple[int, int]:
    nums_p1 = []
    nums_p2 = defaultdict(list)
    H, W = len(data), len(data[0])
    symbols = set(x for line in data for x in line if not x.isdigit() and x != '.')

    for i, line in enumerate(data):
        for j, char in enumerate(line):
            if char.isdigit() and (j == 0 or not line[j - 1].isdigit()):
                cur_num, num_len = get_num(line[j:])
                valid_p1 = valid_p2 = False
                for x, y in get_boundary(i, j, H, W, num_len):
                    if data[x][y] in symbols:
                        valid_p1 = True
                        if data[x][y] == '*':
                            coord = (x, y)
                            valid_p2 = True
                            break

                nums_p1.append(cur_num) if valid_p1 else None
                nums_p2[coord].append(cur_num) if valid_p2 else None

    p1 = sum(nums_p1)
    p2 = sum(nums_p2[k][0] * nums_p2[k][1] for k in nums_p2 if len(nums_p2[k]) == 2)
    return p1, p2


if __name__ == '__main__':
    with advent.get_input() as f:
        data = f.read().splitlines()

    print(solve_optimized(data))

    advent.print_answer(1, p1(data))
    advent.print_answer(2, p2(data))
