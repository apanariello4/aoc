from utils import advent

advent.setup(2021, 2)


def get_position(moves: list[str], part: int) -> int:
    horizontal, vertical = 0, 0
    aim = 0

    for move in moves:
        direction, value = move.split()
        value = int(value)

        if direction == 'forward':
            horizontal += value
            vertical += value * aim
        else:
            aim += value if direction == 'down' else -value

    return horizontal * aim if part == 1 else horizontal * vertical


if __name__ == '__main__':
    with advent.get_input() as f:
        moves = f.read().splitlines()

    advent.print_answer(1, get_position(moves, 1))
    advent.print_answer(2, get_position(moves, 2))
