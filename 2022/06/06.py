from pathlib import Path


def find_start(string: str, header_len: int) -> int:
    buffer = []
    for i, char in enumerate(string):
        if len(buffer) == len(set(buffer)) == header_len:
            return i
        buffer.append(char)
        if len(buffer) > header_len:
            buffer.pop(0)


if __name__ == '__main__':
    string = Path('input.txt').read_text()
    print("part 1:", find_start(string, header_len=4))
    print("part 2:", find_start(string, header_len=14))
