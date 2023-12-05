import re

from utils import advent

advent.setup(2023, 2)

DEBUG = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

max_red = 12
max_blue = 14
max_green = 13


def p1(data: list[str]) -> int:
    all_ids_sum = 0
    for line in data:
        id_ = line.split(':')[0].split()[1]
        games = line.split(':')[1].split(';')
        for i, game in enumerate(games):
            game = game.strip()

            green = int(re.search(r'(\d+) green', game).group(1)) if 'green' in game else 1
            blue = int(re.search(r'(\d+) blue', game).group(1)) if 'blue' in game else 1
            red = int(re.search(r'(\d+) red', game).group(1)) if 'red' in game else 1

            if red > max_red or blue > max_blue or green > max_green:
                # print(f'{id_} is not valid')
                break
            if i == len(games) - 1:
                # print(f'{id_} is valid')
                all_ids_sum += int(id_)
    return all_ids_sum


def p2(data: list[str]) -> int:
    all_ids_sum = 0
    for line in data:
        id_ = line.split(':')[0].split()[1]
        games = line.split(':')[1].split(';')
        min_green, min_blue, min_red = 0, 0, 0
        cur_min_green, cur_min_blue, cur_min_red = 0, 0, 0
        for i, game in enumerate(games):
            game = game.strip()

            green = int(re.search(r'(\d+) green', game).group(1)) if 'green' in game else 0
            blue = int(re.search(r'(\d+) blue', game).group(1)) if 'blue' in game else 0
            red = int(re.search(r'(\d+) red', game).group(1)) if 'red' in game else 0

            cur_min_green = max(cur_min_green, green)
            cur_min_blue = max(cur_min_blue, blue)
            cur_min_red = max(cur_min_red, red)
            if i == len(games) - 1:

                all_ids_sum += cur_min_green * cur_min_blue * cur_min_red
    return all_ids_sum


def solve(data: list[str]) -> tuple[int, int]:
    p1_sol = p2_sol = 0
    for id_, line in enumerate(data, 1):
        games = line.split(':')[1].split('; ')
        cur_min_green, cur_min_blue, cur_min_red = 0, 0, 0
        valid = True

        for game in games:

            green = int(re.search(r'(\d+) green', game).group(1)) if 'green' in game else 0
            blue = int(re.search(r'(\d+) blue', game).group(1)) if 'blue' in game else 0
            red = int(re.search(r'(\d+) red', game).group(1)) if 'red' in game else 0

            cur_min_green = max(cur_min_green, green)
            cur_min_blue = max(cur_min_blue, blue)
            cur_min_red = max(cur_min_red, red)

            valid &= green <= max_green and blue <= max_blue and red <= max_red

        p1_sol += id_ * valid
        p2_sol += cur_min_green * cur_min_blue * cur_min_red

    return p1_sol, p2_sol


if __name__ == '__main__':
    with advent.get_input() as f:
        data = f.read().splitlines()

    p1_sol, p2_sol = solve(data)

    advent.print_answer(1, p1_sol)
    advent.print_answer(2, p2_sol)
