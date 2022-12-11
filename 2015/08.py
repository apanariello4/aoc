from utils import advent

advent.setup(2015, 8)


def count_chars(lines: list[str]) -> tuple[int, int]:
    n_chars = 0
    n_chars_in_memory = 0
    n_icreased_chars = 0
    for line in lines:
        n_chars += len(line)
        n_chars_in_memory += len(eval(line))
        encoded = '"' + line.replace('\\', '\\\\').replace('"', '\\"') + '"'
        n_icreased_chars += len(encoded)

    return n_chars - n_chars_in_memory, n_icreased_chars - n_chars


if __name__ == '__main__':
    with advent.get_input() as f:
        lines = f.read().splitlines()

    p1, p2 = count_chars(lines)
    advent.submit_answer(1, p1)

    advent.submit_answer(2, p2)
