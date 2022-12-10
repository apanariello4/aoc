from utils import advent
import hashlib

advent.setup(2015, 4)


def get_md5(data: str) -> str:
    return hashlib.md5(data.encode()).hexdigest()


def get_lowest_with_trailing_zeros(data: str, n_zeros: int) -> int:
    i = 0
    while True:
        if get_md5(data + str(i)).startswith('0' * n_zeros):
            return i
        i += 1


if __name__ == '__main__':
    with advent.get_input() as f:
        data = f.read().strip()

    advent.submit_answer(1, get_lowest_with_trailing_zeros(data, 5))
    advent.submit_answer(2, get_lowest_with_trailing_zeros(data, 6))
