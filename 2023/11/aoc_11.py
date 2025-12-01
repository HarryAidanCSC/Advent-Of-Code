with open("input.txt", "r") as file:
    lines = [line.strip().split() for line in file]

import re

# Get lists to be expanded
row_index = []
for i, line in enumerate(lines):
    if len(re.findall(r"#", str(line))) == 0:
        row_index.append(i)

# Get col index to be expanded
col_index = []
for i in range(0, len(lines[0][0])):
    col = []
    for line in lines:
        col.append(line[0][i])
    if "#" not in col:
        col_index.append(i)

# Apply row expansion
xcount = 0
for x in row_index:
    lines.insert(x + xcount, ["." * 140])
    xcount += 1

# Flatten list of lists into a list of strings
from itertools import chain

lines = list(chain.from_iterable(lines))

# Expand cols
ycount = 0
for y in col_index:
    for i, row in enumerate(lines):
        lines[i] = row[: y + ycount] + "." + row[y + ycount :]
    ycount += 1


# Coords of all galaxies
coords = []
for iy, y in enumerate(lines):
    indices = [index for index, char in enumerate(y) if char == "#"]
    for indicy in indices:
        coords.append([indicy, iy])

from itertools import combinations

pairs = list(combinations(coords, 2))

counter = 0
for item in pairs:
    coord1 = item[0]
    coord2 = item[1]
    score = abs(coord1[0] - coord2[0]) + abs(coord1[1] - coord2[1])
    counter += score

print(counter)

with open("input.txt", "r") as file:
    lines = [line.strip().split() for line in file]
lines = list(chain.from_iterable(lines))

# Coords of all galaxies
coords = []
for iy, y in enumerate(lines):
    indices = [index for index, char in enumerate(y) if char == "#"]
    for indicy in indices:
        coords.append([indicy, iy])

from itertools import combinations

pairs = list(combinations(coords, 2))

counter = 0
for item in pairs:
    coord1 = item[0]
    coord2 = item[1]

    xc = tuple(sorted([coord1[0], coord2[0]]))
    yc = tuple(sorted([coord1[1], coord2[1]]))

    countx = 0
    county = 0

    countx = sum(1000000 - 1 for num in col_index if xc[0] <= num <= xc[1])
    county = sum(1000000 - 1 for num in row_index if yc[0] <= num <= yc[1])

    score = abs(coord1[0] - coord2[0]) + abs(coord1[1] - coord2[1]) + countx + county
    counter += score

print(counter)
