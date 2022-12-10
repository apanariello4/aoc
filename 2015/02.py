from utils import advent

advent.setup(2015, 2)


def paper_required(data: list[str]) -> int:
    tot = 0
    for line in data:
        l, w, h = map(int, line.split('x'))
        sides = [l * w, w * h, h * l]
        tot += 2 * sum(sides) + min(sides)
    return tot


def ribbon_required(data: list[str]) -> int:
    tot = 0
    for line in data:
        l, w, h = map(int, line.split('x'))
        sides = [2 * (l + w), 2 * (w + h), 2 * (h + l)]
        tot += min(sides) + l * w * h
    return tot


if __name__ == '__main__':
    with advent.get_input() as f:
        data = f.read().splitlines()

    advent.print_answer(1, paper_required(data))
    advent.print_answer(2, ribbon_required(data))
