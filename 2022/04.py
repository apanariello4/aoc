from utils import advent

advent.setup(2022, 4)
with advent.get_input() as f:
    lines = f.read().splitlines()

tot = 0
for line in lines:
    a, b = line.split(',')
    a_min, a_max = int(a.split('-')[0]), int(a.split('-')[1])
    b_min, b_max = int(b.split('-')[0]), int(b.split('-')[1])

    if (a_min <= b_min and a_max >= b_max) or (b_min <= a_min and b_max >= a_max):
        tot += 1

print("part 1 : ", tot)

tot = 0
for line in lines:
    a, b = line.split(',')
    a_min, a_max = int(a.split('-')[0]), int(a.split('-')[1])
    b_min, b_max = int(b.split('-')[0]), int(b.split('-')[1])

    range_a = set(range(a_min, a_max + 1))
    range_b = set(range(b_min, b_max + 1))

    if range_a & range_b:
        tot += 1

print("part 2 : ", tot)
