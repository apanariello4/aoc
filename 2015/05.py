from utils import advent

advent.setup(2015, 5)


def get_nice_strings(data: list[str]) -> int:
    nice = 0
    for line in data:
        if len([c for c in line if c in 'aeiou']) >= 3:
            if any(c1 == c2 for c1, c2 in zip(line, line[1:])):
                if not any(c in line for c in 'ab cd pq xy'.split()):
                    nice += 1

    return nice


def get_nicer_strings(data: list[str]) -> int:
    nice = 0
    for line in data:
        if any(line[i:i + 2] in line[i + 2:] for i in range(len(line) - 2)):
            if any(line[i] == line[i + 2] for i in range(len(line) - 2)):
                nice += 1

    return nice


if __name__ == '__main__':
    with advent.get_input() as f:
        data = f.read().splitlines()

    advent.submit_answer(1, get_nice_strings(data))
    advent.submit_answer(2, get_nicer_strings(data))
