with open("input.txt") as f:
    data = f.read().splitlines()

def get_adjacent(x, y, len_x, len_y):
    valid = []
    if x > 0:
        valid.append((x-1, y))
    if x < len_x-1:
        valid.append((x+1, y))
    if y > 0:
        valid.append((x, y-1))
    if y < len_y-1:
        valid.append((x, y+1))

    yield from valid

def is_lowest(x, y, data):
    len_x = len(data[0])
    len_y = len(data)
    for adj in get_adjacent(x, y, len_x, len_y):
        if int(data[adj[1]][adj[0]]) <= int(data[y][x]):
            return False
    return True

total = 0
for y, row in enumerate(data):
    for x, col in enumerate(row):
        if is_lowest(x, y, data):
            total += 1 + int(col)

print(total)
