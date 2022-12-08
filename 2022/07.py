from collections import defaultdict
from pathlib import Path

from utils import advent


def make_index(data: list[str]) -> dict[str, int]:
    index = {}
    cwd = Path()
    for l in data:
        if l.startswith("$ cd"):
            arg = l.split(" ")[2]
            cwd = cwd.parent if arg == ".." else cwd / arg
        elif l[0].isdigit():
            size, name = l.split(" ")
            file_path = cwd / name
            index[str(file_path)] = int(size)
    return index


def find_dirs_memory(index: dict) -> dict[str, int]:
    d = defaultdict(int)
    for k, v in index.items():
        all_parents_dirs = [str(x) for x in Path(k).parents]
        for p in all_parents_dirs:
            d[p] += v
    return d


if __name__ == "__main__":
    advent.setup(2022, 7)

    with advent.get_input() as f:
        data = f.read().splitlines()

    index = make_index(data)
    dirs = find_dirs_memory(index)

    print("Part 1:", sum([v for v in dirs.values() if v <= 100000]))

    used_space = dirs["/"]
    free_space = 70000000 - used_space
    needed_space = 30000000 - free_space

    print("Part 2:", min([v for v in dirs.values() if v >= needed_space]))
