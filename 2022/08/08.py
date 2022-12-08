def visibles_trees(data: list[list[int]]) -> int:
    H, W = len(data), len(data[0])
    n_visibles = (H - 1) * 2 + (W - 1) * 2  # perimeter

    for i, row in enumerate(data):
        if i in (0, H - 1):
            continue
        for j, tree in enumerate(row):
            if j in (0, W - 1):
                continue

            east = all(tree > t for t in row[j + 1:])
            west = all(tree > t for t in row[:j])
            north = all(tree > data[x][j] for x in range(i))
            south = all(tree > data[x][j] for x in range(i + 1, H))

            n_visibles += 1 if any((east, west, north, south)) else 0

    return n_visibles


def scenic_score(data: list[list[int]]) -> int:
    score = 1  # account for the perimeter
    H, W = len(data), len(data[0])

    for i, row in enumerate(data):
        if i in (0, H - 1):
            continue
        for j, tree in enumerate(row):
            if j in (0, W - 1):
                continue

            for east in range(j + 1, W):
                if row[east] >= tree:
                    break
            for west in range(j - 1, -1, -1):
                if row[west] >= tree:
                    break
            for north in range(i - 1, -1, -1):
                if data[north][j] >= tree:
                    break
            for south in range(i + 1, H):
                if data[south][j] >= tree:
                    break

            score = max((east - j) * (j - west) * (north - i) * (i - south), score)

    return score


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().splitlines()
    data = [[int(x) for x in line] for line in data]

    print("Part 1:", visibles_trees(data))
    print("Part 2:", scenic_score(data))
