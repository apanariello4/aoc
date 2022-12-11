from utils import advent

advent.setup(2015, 10)


def look_and_say_turn(string: str) -> str:
    result = []
    for char in string:
        if result and result[-1][0] == char:
            result[-1][1] += 1
        else:
            result.append([char, 1])
    return ''.join(f'{count}{char}' for char, count in result)


def look_and_say(string: str, turns: int) -> int:
    for _ in range(turns):
        string = look_and_say_turn(string)
    return len(string)


if __name__ == '__main__':
    with advent.get_input() as f:
        data = f.read().strip()

    advent.print_answer(1, look_and_say(data, 40))
    advent.print_answer(2, look_and_say(data, 50))
