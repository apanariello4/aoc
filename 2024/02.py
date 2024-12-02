from utils import advent
from utils.advent_debug import print_debug

advent.setup(2024, 2)

DEBUG = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""


def parse(data):
    return data

def is_line_safe(nums):
    is_decreasing = nums[0] > nums[1]
    for num_1, num_2 in zip(nums, nums[1:]):
        if abs(num_2 - num_1) > 3 or abs(num_2 - num_1) == 0:
            return False
        if is_decreasing != (num_1 > num_2):
            return False
    return True

def p1(data):
    safe = 0
    for line in data.splitlines():
        nums = list(map(int, line.split()))
        if is_line_safe(nums):
            safe += 1

    return safe



def p2(data):
    safe = 0
    for line in data.splitlines():
        nums = list(map(int, line.split()))
        if is_line_safe(nums):
            safe += 1
        else:
            for i in range(len(nums)):
                to_check = nums[:i] + nums[i + 1:]
                print(to_check)
                if is_line_safe(to_check):
                    safe += 1
                    break

    return safe


if __name__ == '__main__':
    with advent.get_input() as f:
        data = f.read().strip()
    data = parse(data)

    print_debug(DEBUG, 2, p1)
    print_debug(DEBUG, 4, p2)

    advent.print_answer(1, p1(data))
    advent.print_answer(2, p2(data))
