from itertools import product
from operator import add, mul

from utils import advent
from utils.advent_debug import print_debug

advent.setup(2024, 7)

DEBUG = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""


def parse(data):
    return data.splitlines()


ops_ = {'+': add, '*': mul, '||': lambda x, y: int(str(x) + str(y))}


def p1(data):
    s = 0

    for line in data:
        val = int(line.split(': ')[0])
        nums = list(map(int, line.split(': ')[1].split()))

        for op in product(['+', '*'], repeat=len(nums) - 1):
            value = nums[0]
            for i in range(1, len(nums)):
                value = ops_[op[i - 1]](value, nums[i])
                if value > val:
                    break
            if value == val:
                s += val
                break
    return s


def p2(data):
    s = 0

    for line in data:
        val = int(line.split(': ')[0])
        nums = list(map(int, line.split(': ')[1].split()))

        for op in product(['+', '*', '||'], repeat=len(nums) - 1):
            value = nums[0]
            for i in range(1, len(nums)):
                value = ops_[op[i - 1]](value, nums[i])
                if value > val:
                    break
            if value == val:
                s += val
                break
    return s


def optimized(data, p1):
    s = 0

    def can_obtain(val, nums, p1=True):
        if len(nums) == 1:
            return val == nums[0]
        if val % nums[-1] == 0 and can_obtain(val // nums[-1], nums[:-1], p1):
            return True
        if val > nums[-1] and can_obtain(val - nums[-1], nums[:-1], p1):
            return True
        if not p1:
            if len(str(val)) > len(str(nums[-1])) and str(val).endswith(str(nums[-1])) and can_obtain(int(str(val)[:-len(str(nums[-1]))]), nums[:-1], p1):
                return True
        return False

    for line in data:
        val = int(line.split(': ')[0])
        nums = list(map(int, line.split(': ')[1].split()))

        if can_obtain(val, nums, p1):
            s += val
    return s


if __name__ == '__main__':
    with advent.get_input() as f:
        data = f.read().strip()
    data = parse(data)

    print_debug(parse(DEBUG), 3749, p1)
    print_debug(parse(DEBUG), 11387, p2)

    advent.print_answer(1, optimized(data, p1=True))
    advent.print_answer(2, optimized(data, p1=False))
