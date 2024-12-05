from pathlib import Path
from functools import cmp_to_key

with open(Path(_file_).parent / 'input.txt', 'r') as file:
    rules, lines = [], []

    for line in file:
        if '|' in line:
            rules.append(line.strip())
        elif ',' in line:
            lines.append(line.strip().split(','))

# Part One
p1 = 0
incorrect_lines = []

for line in lines:
    lhs, flag = set(), True
    for i in line:
        rule = {s[-2:] for s in rules if f"{i}|" in s}
        if any(r in lhs for r in rule):
            flag = False
            break
        else:
            lhs.add(i)
    if flag:
        p1 += int(line[len(line) // 2])
    else:
        incorrect_lines.append(line)

print(p1)

# Part Two
p2 = 0

for line in incorrect_lines:
    sorted_line = sorted(line, key=cmp_to_key(lambda x, y: (x + y in rules)))
    p2 += int(sorted_line[len(sorted_line) // 2])

print(p2)