COMB1 = {"A X": 1 + 3,
         "A Y": 2 + 6,
         "A Z": 3 + 0,
         "B X": 1 + 0,
         "B Y": 2 + 3,
         "B Z": 3 + 6,
         "C X": 1 + 6,
         "C Y": 2 + 0,
         "C Z": 3 + 3, }

COMB2 = {"A X": 3 + 0,
         "A Y": 1 + 3,
         "A Z": 2 + 6,
         "B X": 1 + 0,
         "B Y": 2 + 3,
         "B Z": 3 + 6,
         "C X": 2 + 0,
         "C Y": 3 + 3,
         "C Z": 1 + 6, }

if __name__ == "__main__":
    with open("./input.txt") as f:
        moves = f.read().splitlines()

    print("part 1: ", sum([COMB1[x] for x in moves]))

    print("part 2: ", sum([COMB2[x] for x in moves]))
