from utils import advent

advent.setup(2015, 3)


def get_unique_houses(data: str) -> int:
    houses = {(0, 0)}
    x, y = 0, 0
    for c in data:
        x += 1 if c == '>' else -1 if c == '<' else 0
        y += 1 if c == '^' else -1 if c == 'v' else 0
        houses.add((x, y))
    return len(houses)


def get_unique_houses_with_robo(data: str) -> int:
    houses = {(0, 0)}
    x, y = 0, 0
    rx, ry = 0, 0
    for i, c in enumerate(data):
        if i % 2 == 0:
            x += 1 if c == '>' else -1 if c == '<' else 0
            y += 1 if c == '^' else -1 if c == 'v' else 0
            houses.add((x, y))
        else:
            rx += 1 if c == '>' else -1 if c == '<' else 0
            ry += 1 if c == '^' else -1 if c == 'v' else 0
            houses.add((rx, ry))
    return len(houses)


if __name__ == '__main__':
    with advent.get_input() as f:
        data = f.read().strip()

    advent.print_answer(1, get_unique_houses(data))
    advent.print_answer(2, get_unique_houses_with_robo(data))
