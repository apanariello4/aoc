from utils import advent

advent.setup(2021, 4)


class BingoBoard:
    def __init__(self, lines: str):
        self.lines = {}
        for r, line in enumerate(lines.splitlines()):
            for c, num in enumerate(line.split()):
                self.lines[(r, c)] = int(num)

    def mark_number(self, num: int) -> bool:
        for i in range(5):
            for j in range(5):
                if self.lines[(i, j)] == num:
                    self.lines[(i, j)] = 'X'

        return self.check_win()

    def check_win(self) -> bool:
        for i in range(5):
            if all(self.lines[(i, j)] == 'X' for j in range(5)):
                return True
            if all(self.lines[(j, i)] == 'X' for j in range(5)):
                return True
        return False

    def get_score(self, num: int) -> int:
        return sum(v for v in self.lines.values() if v != 'X') * num

    def __repr__(self) -> str:
        return '\n'.join(' '.join(f'{self.lines[(i, j)]:>2}' for j in range(5)) for i in range(5))


def find_winners(boards: list[BingoBoard], numbers_drawn: list[int]) -> tuple[int, int]:
    scores = []
    for num in numbers_drawn:
        for i, board in enumerate(boards):
            if board and board.mark_number(num):
                scores.append(board.get_score(num))
                boards[i] = None
    return scores[0], scores[-1]


if __name__ == '__main__':
    with advent.get_input() as f:
        numbers_drawn = list(map(int, f.readline().split(',')))
        _ = f.readline()
        boards = f.read().split('\n\n')

    boards = [BingoBoard(board) for board in boards]
    first, last = find_winners(boards, numbers_drawn)
    advent.print_answer(1, first)
    advent.print_answer(2, last)
