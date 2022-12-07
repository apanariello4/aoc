from collections import defaultdict
from pathlib import Path


def make_index(data: str) -> dict[str, int]:
    index = {}
    cwd = ""
    for l in data:
        if l.startswith("$ cd"):
            arg = l.split(" ")[2]
            if arg == "..":
                cwd = cwd.rsplit("/", 1)[0]
            elif arg == '/':
                cwd = arg
            else:
                cwd += "/" + arg if cwd != "/" else arg
        else:
            if not l.startswith("dir") and not l.startswith("$"):
                size, name = l.split(" ")

                file_path = cwd + "/" + name if cwd != "/" else "/" + name
                index[file_path] = int(size)
    return index


def find_dirs_memory(index: dict) -> dict[str, int]:
    d = defaultdict(int)
    for k, v in index.items():
        all_parents_dirs = [str(x) for x in Path(k).parents]
        for p in all_parents_dirs:
            d[p] += v
    return d


if __name__ == "__main__":

    with open("input.txt") as f:
        data = f.read().splitlines()

    index = make_index(data)
    dirs = find_dirs_memory(index)

    print("Part 1:", sum([v for v in dirs.values() if v <= 100000]))

    used_space = dirs["/"]
    free_space = 70000000 - used_space
    needed_space = 30000000 - free_space

    print("Part 2:", min([v for v in dirs.values() if v >= needed_space]))
