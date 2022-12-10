from utils import advent

advent.setup(2022, 9)


def get_adj_coords(x: int, y: int) -> list[tuple[int, int]]:
    return [(x + dx, y + dy) for dx in (-1, 0, 1) for dy in (-1, 0, 1)]


def sign(x: int) -> int:
    return (x > 0) - (x < 0)


DIRECTIONS = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}


def get_n_visited(moves: tuple[str]) -> tuple[int, int]:
    rope = [(0, 0)] * 10
    visited0 = {(0, 0)}
    visited9 = {(0, 0)}

    for m in moves:
        direction, distance = m.split()
        for _ in range(int(distance)):
            hx, hy = rope[0]
            dx, dy = DIRECTIONS[direction]
            rope[0] = hx + dx, hy + dy

            for x in range(9):
                hx, hy = rope[x]
                tx, ty = rope[x + 1]

                if (tx, ty) not in get_adj_coords(hx, hy):
                    rope[x + 1] = tx + sign(hx - tx), ty + sign(hy - ty)

            visited0.add(tuple(rope[1]))
            visited9.add(tuple(rope[9]))

    return len(visited0), len(visited9)


if __name__ == '__main__':
    with advent.get_input() as f:
        moves = tuple(f.read().splitlines())

    p1, p2 = get_n_visited(moves)
    advent.print_answer(1, p1)  # 6563
    advent.print_answer(2, p2)  # 2653
