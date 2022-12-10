from utils import advent

advent.setup(2015, 1)


def get_floor(data: str) -> int:
    return len(data.replace(')', '')) - len(data.replace('(', ''))


def get_first_negative(data: str) -> int:
    floor = 0
    for i, c in enumerate(data):
        floor += 1 if c == '(' else -1
        if floor < 0:
            return i + 1


if __name__ == '__main__':
    with advent.get_input() as f:
        data = f.read().strip()

    advent.print_answer(1, get_floor(data))
    advent.print_answer(2, get_first_negative(data))
