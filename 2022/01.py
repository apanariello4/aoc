from utils import advent


def main(data: list[str]) -> tuple[int, int]:
    sums = [sum([int(x) for x in chunk.split()]) for chunk in data]
    sums = sorted(sums, reverse=True)
    return sums[0], sum(sums[:3])


if __name__ == "__main__":
    advent.setup(2022, 1)

    with advent.get_input() as f:
        data = f.read().split('\n\n')

    p1, p2 = main(data)
    print("part 1 ", p1)
    print("part 2 ", p2)
