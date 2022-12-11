from utils import advent

advent.setup(2015, 11)


def is_valid(string: str) -> str:
    if any(c in string for c in ('i', 'l', 'o')):
        return False

    pairs = [i for i, (c1, c2) in enumerate(zip(string, string[1:])) if c1 == c2]
    if len(pairs) < 2:
        return False
    for i, j in zip(pairs, pairs[1:]):
        if j - i == 1:
            return False

    if any((ord(a) == ord(b) - 1 == ord(c) - 2) for a, b, c in zip(string, string[1:], string[2:])):
        return True
    return False


def increment_psw(psw: str):
    if psw[-1] == 'z':
        return increment_psw(psw[:-1]) + 'a'
    return psw[:-1] + chr(ord(psw[-1]) + 1)


def find_new_password(psw: str):
    while True:
        psw = increment_psw(psw,)
        if is_valid(psw):
            return psw


if __name__ == '__main__':
    with advent.get_input() as f:
        data = f.read().strip()

    psw = find_new_password(data)
    advent.print_answer(1, psw)
    advent.print_answer(2, find_new_password(psw))
