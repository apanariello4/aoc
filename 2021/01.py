from utils import advent

advent.setup(2021, 1)


def count_increase(nums: list[int], window: int = 1) -> int:
    return sum(b > a for a, b in zip(nums, nums[window:]))


if __name__ == '__main__':
    with advent.get_input() as f:
        nums = [int(x) for x in f.readlines()]

    advent.print_answer(1, count_increase(nums))
    advent.print_answer(2, count_increase(nums, 3))
