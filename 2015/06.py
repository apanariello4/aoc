from utils import advent

advent.setup(2015, 6)


def count_lights(moves: list[str]) -> int:
    lights = [[False] * 1000 for _ in range(1000)]

    for line in moves:
        action, xy1, xy2 = line.split()
        x1, y1 = xy1.split(',')
        x2, y2 = xy2.split(',')
        x1, y1, x2, y2 = map(int, (x1, y1, x2, y2))
        if action == 'toggle':
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    lights[x][y] = not lights[x][y]
        else:
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    lights[x][y] = action == 'on'
    return sum(sum(lights, []))


def total_brightness(moves: list[str]) -> int:
    lights = [[0] * 1000 for _ in range(1000)]

    for line in moves:
        action, xy1, xy2 = line.split()
        x1, y1 = xy1.split(',')
        x2, y2 = xy2.split(',')
        x1, y1, x2, y2 = map(int, (x1, y1, x2, y2))
        if action == 'toggle':
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    lights[x][y] += 2
        else:
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    lights[x][y] += 1 if action == 'on' else -1
                    lights[x][y] = max(0, lights[x][y])
    return sum(sum(lights, []))


if __name__ == '__main__':
    with advent.get_input() as f:
        lines = f.read().splitlines()
    lines = list(map(lambda x: x.replace(' through ', ' ').replace('turn ', ''), lines))

    advent.submit_answer(1, count_lights(lines))
    advent.submit_answer(2, total_brightness(lines))
