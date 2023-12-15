import functools
from itertools import product

try:
    from tqdm import tqdm
except ImportError:
    def tqdm(x, *args, **kwargs):
        return x

from utils import advent
from utils.advent_debug import assert_debug

advent.setup(2023, 12)

DEBUG = """???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1"""


def p1(data: list[str]) -> int:
    tot = 0
    for line in tqdm(data):
        springs, groups = line.split()
        springs = [*springs]
        groups = list(map(int, groups.split(',')))
        n_missing = springs.count('?')

        for combination in product(['#', '.'], repeat=n_missing):
            springs_copy = springs.copy()
            combination = list(combination)
            for i, c in enumerate(springs_copy):
                if c == '?':
                    springs_copy[i] = combination.pop()

            cur_groups = []
            cur_group = 0
            for c in springs_copy:
                if c == '#':
                    cur_group += 1
                else:
                    if cur_group != 0:
                        cur_groups.append(cur_group)
                        cur_group = 0
            if cur_group != 0:
                cur_groups.append(cur_group)
            if cur_groups == groups:
                tot += 1
                continue
        else:
            continue
    return tot


def unfold(line: str) -> str:
    part1, part2 = line.split()
    part1 = ''.join([part1 + '?'] * 4 + [part1])
    part2 = ','.join([part2] * 5)
    return part1 + ' ' + part2


@functools.lru_cache(maxsize=None)
def count(springs, nums):
    if springs == "":
        return 1 if nums == () else 0

    if nums == ():
        return 0 if "#" in springs else 1

    result = 0

    if springs[0] in ".?":
        result += count(springs[1:], nums)

    if springs[0] in "#?":
        if nums[0] <= len(springs) and "." not in springs[:nums[0]] and (nums[0] == len(springs) or springs[nums[0]] != "#"):
            result += count(springs[nums[0] + 1:], nums[1:])

    return result


def p2(data: list[str]) -> int:
    tot = 0

    for line in tqdm(data):
        line = unfold(line)
        springs, groups = line.split()
        springs = [*springs]
        groups = list(map(int, groups.split(',')))
        tot += count(''.join(springs), tuple(groups))
    return tot


def p1_optimized(data: list[str]) -> int:
    tot = 0

    for line in tqdm(data):
        springs, groups = line.split()
        springs = [*springs]
        groups = list(map(int, groups.split(',')))
        tot += count(''.join(springs), tuple(groups))
    return tot


if __name__ == '__main__':
    with advent.get_input() as f:
        data = f.read().strip().splitlines()

    assert_debug(DEBUG.splitlines(), 21, p1)
    # advent.print_answer(1, p1(data))
    advent.print_answer(1, p1_optimized(data))

    assert_debug(DEBUG.splitlines(), 525152, p2)
    advent.print_answer(2, p2(DEBUG.splitlines()))
    advent.print_answer(2, p2(data))
