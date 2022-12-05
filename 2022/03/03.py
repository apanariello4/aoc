with open("./input.txt") as f:
    lines = f.read().splitlines()
tot = 0

for line in lines:
    a, b = line[:len(line) // 2], line[len(line) // 2:]
    common = set(a).intersection(set(b))
    for item in common:
        if item.islower():
            tot += ord(item) - 96
        elif item.isupper():
            tot += ord(item) - 38

print("part 1 : ", tot)
# print(ord('a') - 96)
# print(ord('A') - 38)

tot = 0
for line_group in zip(*[iter(lines)] * 3):
    common = set(line_group[0]).intersection(set(line_group[1])).intersection(set(line_group[2]))
    for item in common:
        if item.islower():
            tot += ord(item) - 96
        elif item.isupper():
            tot += ord(item) - 38

print("part 2 : ", tot)
