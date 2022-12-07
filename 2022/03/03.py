def get_value(char: str) -> int:
    return ord(char) - 96 if char.islower() else ord(char) - 38


def part1(lines: list[str]) -> int:
    tot = 0
    for line in lines:
        a, b = line[:len(line) // 2], line[len(line) // 2:]
        tot += sum(get_value(c) for c in set(a) & set(b))
    return tot


def part2(lines: list[str]) -> int:
    tot = 0
    for line_group in zip(*[iter(lines)] * 3):
        common = set(line_group[0]) & set(line_group[1]) & set(line_group[2])
        tot += sum(get_value(c) for c in common)
    return tot


if __name__ == '__main__':
    with open('input.txt') as f:
        lines = f.read().splitlines()
    print('part 1:', part1(lines))
    print('part 2:', part2(lines))
