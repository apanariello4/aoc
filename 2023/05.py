from utils import advent

advent.setup(2023, 5)

DEBUG = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""


def get_ranges(mapping: str) -> list[tuple[int, int, int]]:
    return [tuple(map(int, x.split())) for x in mapping.splitlines()[1:]]


def p1(data: list[str]) -> int:
    seeds = [int(x) for x in data.split('\n')[0].split(': ')[1].split()]
    mappings = data.split('\n\n')[1:]
    for m in mappings:
        ranges = get_ranges(m)
        temp = []
        for x in seeds:
            for dest, source, rng in ranges:
                if source <= x < source + rng:
                    temp.append(x - source + dest)
                    break
            else:
                temp.append(x)
        seeds = temp
    return min(seeds)


def p2(data: list[str]) -> int:
    inputs = data.split("\n\n")[0]

    inputs = list(map(int, inputs.split(":")[1].split()))

    seeds = [(inputs[i], inputs[i] + inputs[i + 1]) for i in range(0, len(inputs), 2)]
    mappings = data.split('\n\n')[1:]
    for m in mappings:
        ranges = get_ranges(m)
        temp = []
        while seeds:
            start, end = seeds.pop()
            for dest, source, rng in ranges:
                overlap_start = max(start, source)
                overlap_end = min(end, source + rng)
                if overlap_start < overlap_end:
                    temp.append((overlap_start - source + dest, overlap_end - source + dest))
                    if overlap_start > start:
                        seeds.append((start, overlap_start))
                    if end > overlap_end:
                        seeds.append((overlap_end, end))
                    break
            else:
                temp.append((start, end))
        seeds = temp

    return min(seeds)[0]


if __name__ == '__main__':
    with advent.get_input() as f:
        data = f.read()

    print(p1(DEBUG), f"Correct answer: 35")
    advent.print_answer(1, p1(data))
    print(p2(DEBUG), f"Correct answer: 46")
    advent.print_answer(2, p2(data))
