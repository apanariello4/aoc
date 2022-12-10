from utils import advent

advent.setup(2022, 10)


class Program:
    def __init__(self, instrusctions: tuple[str]):
        self.X = 1
        self.n_cycles = 1
        self.signal_str = 0
        self.crt = []
        self.row = ''
        self.instr = instrusctions

    def run(self):
        for op in self.instr:

            self.update_row_and_cycles()

            if op.startswith('add'):
                self.update_sig_and_crt()
                self.update_row_and_cycles()
                self.X += int(op[5:])

            self.update_sig_and_crt()

        return self.signal_str, self.crt

    def update_signal(self):
        self.signal_str += self.n_cycles * self.X

    def update_crt(self):
        self.crt.append(self.row)
        self.row = ''

    def update_row_and_cycles(self):
        self.row += '#' if self.X <= self.n_cycles % 40 <= self.X + 2 else ' '
        self.n_cycles += 1

    def update_sig_and_crt(self):
        if self.n_cycles % 40 == 20:
            self.update_signal()
        elif self.n_cycles % 40 == 1:
            self.update_crt()


if __name__ == '__main__':
    with advent.get_input() as f:
        instr = tuple(f.read().splitlines())
    p = Program(instr)
    res, row = p.run()
    advent.print_answer(1, res)
    print('Part 2:\n', '\n'.join(row), sep='')
