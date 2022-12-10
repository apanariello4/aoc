import operator
from utils import advent

advent.setup(2015, 7)

OPERATORS = {
    'AND': operator.and_,
    'OR': operator.or_,
    'LSHIFT': operator.lshift,
    'RSHIFT': operator.rshift,
}


def get_signals(wires: list[str], signals: dict[str, int]) -> dict[str, int]:
    complete = True
    for line in wires:
        left, target = line.split(' -> ')
        if target in signals:
            continue
        elif len(left.split()) == 1:  # direct assignment
            if left.isdigit():
                signals[target] = int(left)
            elif left not in signals:
                complete = False
                continue

            signals[target] = signals[left]

        elif left.startswith('NOT '):

            if left[4:] not in signals:
                complete = False
                continue

            signals[target] = ~signals[left[4:]]

        else:  # gate
            signal1, op, signal2 = left.split()
            if (signal1 not in signals and signal1.isalpha()) or (signal2 not in signals and signal2.isalpha()):
                complete = False
                continue

            s1 = int(signal1) if signal1.isdigit() else signals[signal1]
            s2 = int(signal2) if signal2.isdigit() else signals[signal2]

            signals[target] = OPERATORS[op](s1, s2)

    return signals, complete


if __name__ == '__main__':
    with advent.get_input() as f:
        lines = f.read().splitlines()
    complete = False
    signals = {}
    while not complete:
        signals, complete = get_signals(lines, signals)

    advent.print_answer(1, signals['a'])

    new_signals = {'b': signals['a']}
    complete = False
    while not complete:
        new_signals, complete = get_signals(lines, new_signals)

    advent.print_answer(2, new_signals['a'])
