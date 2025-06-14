from pathlib import Path
with open(Path(__file__).parent / 'input.txt', 'r') as file:
    lines = [line.strip() for line in file]

grid, x_store, a_store = {}, [], []
for i, line in enumerate(lines):
    for j, char in enumerate(line):
        grid[(i, j)] = char
        if char == 'X': x_store.append((i, j))
        elif char == 'A': a_store.append((i, j))

# Part One
directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
sequences = [[[x * dx, x * dy] for x in range(1, 4)] for dx, dy in directions]

p1 = sum(1 for i in x_store for seq in sequences if 'MAS' == ''.join(grid.get((i[0] + s1, i[1] + s2)) or '' for s1, s2 in seq))
print(p1)

# Part Two
sequences = [[[-1, -1], [1, 1]], [[-1, 1], [1, -1]]]
p2 = 0
for i in a_store:
    y, x = i
    flag = True
    for seq in sequences:
        string = ''
        for s1, s2 in seq:
            char = grid.get((y + s1, x + s2))
            if char:
                string += char
        # Check if the string is either 'MS' or 'SM'
        if string not in ('MS', 'SM'):
            flag = False
    if flag:
        p2 += 1
print(p2)


