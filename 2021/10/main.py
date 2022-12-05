import re
with open("input.txt") as f:
    data = f.read().splitlines()

for line in data:

    while True:
        new_line = re.sub(r"\(.*\)|\[.*\]|\<.*\>|\{.*\}", "", line)
        if new_line == line:
            break
    print(new_line)
