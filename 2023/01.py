import re

from utils import advent

advent.setup(2023, 1)

DEBUG = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""

NUMBERS = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
           'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}


def p1(data: list[str]) -> int:
    return sum(10 * int(re.search(r'\d', line)[0]) + int(re.search(r'\d', line[::-1])[0]) for line in data)


def get_value(line: str, reverse: bool = False) -> int:
    for i, char in enumerate(line):
        if char.isdigit():
            return int(char)
        else:
            for word in NUMBERS:
                if line[i:].startswith(word if not reverse else word[::-1]):
                    return NUMBERS[word]


def p2(data: list[str]) -> int:
    return sum(10 * get_value(line) + get_value(line[::-1], True) for line in data)


if __name__ == '__main__':
    with advent.get_input() as f:
        data = f.read().splitlines()

    advent.print_answer(1, p1(data))
    advent.print_answer(2, p2(data))
