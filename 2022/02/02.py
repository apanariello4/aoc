COMB = {"A X": 1 + 3,
        "A Y": 2 + 6,
        "A Z": 3 + 0,
        "B X": 1 + 0,
        "B Y": 2 + 3,
        "B Z": 3 + 6,
        "C X": 1 + 6,
        "C Y": 2 + 0,
        "C Z": 3 + 3, }

COMB_PART2 = {"A X": 3 + 0,
              "A Y": 1 + 3,
              "A Z": 2 + 6,
              "B X": 1 + 0,
              "B Y": 2 + 3,
              "B Z": 3 + 6,
              "C X": 2 + 0,
              "C Y": 3 + 3,
              "C Z": 1 + 6, }
# A: ROCK, B: PAPER, C: SCISSORS
# X: LOSE, Y: DRAW, Z: WIN
# WIN = 6, DRAW = 3, LOSE = 0


with open("./input.txt") as f:
    moves = f.read().splitlines()

result = sum([COMB[x] for x in moves])
print("part 1: ", result)

result = sum([COMB_PART2[x] for x in moves])
print("part 2: ", result)
