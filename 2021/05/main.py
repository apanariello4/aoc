import re
with open("input.txt") as f:
    data = f.read().splitlines()

data = [map(int,re.findall(r"\d+", line)) for line in data]

matrix = {}
for x1,y1,x2,y2 in data:
    if x1 == x2:
        for y in range(min(y1, y2), max(y1, y2)+1):
          matrix[(x1,y)] = matrix.get((x1,y), 0) + 1
    elif y1 == y2:
            for x in range(min(x1, x2), max(x1, x2)+1):
                matrix[(x,y1)] = matrix.get((x,y1), 0) + 1
    else:
        step_x = 1 if x1 < x2 else -1
        step_y = 1 if y1 < y2 else -1
        for x,y in zip(range(x1, x2+step_x, step_x), range(y1, y2+step_y, step_y)):
                matrix[(x,y)] = matrix.get((x,y), 0) + 1

print(sum(1 for v in matrix.values() if v > 1))
