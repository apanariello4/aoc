sums = []

with open("./input.txt") as f:
    data = f.read().split('\n\n')

tot = 0
for chunk in data:
    sums.append(sum([int(x) for x in chunk.split()]))

sums = sorted(sums, reverse=True)
print("part 1 ", sums[0])
print("part 2 ", sum(sums[:3]))

# with open("./input.txt", "r") as f:
#     chunks = f.read().split('\n\n')
# chunks = [tuple(map(int, chunk.split())) for chunk in chunks]
# chunks.sort(key=sum, reverse=True)

# ans1 = sum(chunks[0])
# ans2 = sum(map(sum, chunks[:3]))

# print(ans1)
# print(ans2)
