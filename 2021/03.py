from functools import partial

from utils import advent

advent.setup(2021, 3)


def get_most_common_bit(pos: int, nums: tuple[int]) -> int:
    ones = sum(((n >> pos) & 1) for n in nums)
    return 1 if ones >= len(nums) // 2 + 1 else 0


def get_least_common_bit(pos: int, nums: tuple[str]) -> int:
    return 1 - get_most_common_bit(pos, nums)


def get_power_consumption(nums: tuple[int], n_bits: int) -> int:
    gamma = 0

    for pos in range(n_bits - 1, -1, -1):
        gamma <<= 1
        gamma += get_most_common_bit(pos, nums)

    eps = (1 << n_bits) - gamma - 1
    return gamma * eps


def filter_nums(nums: tuple[int], pos: int, bit: int) -> tuple[int]:
    return tuple(n for n in nums if (n >> pos) & 1 == bit)


def get_life_supp_rate(nums: tuple[int], n_bits: int):
    values = 1
    for predicate in (get_most_common_bit, get_least_common_bit):
        n = nums
        for pos in range(n_bits - 1, -1, -1):
            bit = predicate(pos, n)
            n = filter_nums(n, pos, bit)
            if len(n) == 1:
                break
        values *= n[0]

    return values


if __name__ == '__main__':
    with advent.get_input() as f:
        lines = f.read().splitlines()
    n_bits = len(lines[0])
    nums = tuple(map(partial(int, base=2), lines))

    advent.print_answer(1, get_power_consumption(nums, n_bits))
    advent.print_answer(2, get_life_supp_rate(nums, n_bits))
