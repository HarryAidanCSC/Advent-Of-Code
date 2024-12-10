from pathlib import Path
from collections import deque

with open(Path(__file__).parent / 'input.txt', 'r') as file:
    lines = [line.strip() for line in file]

grid = {}
start = []

for i, line in enumerate(lines):
    for j, val in enumerate(line):
        grid[(i,j)] = int(val)
        if val == '0': start.append((i,j))

queue = deque()
p1 =  0

for s in start:
    queue.append(s)
    part = set()
    while queue:
        i,j = queue.pop()
        val = grid[(i,j)]
        
        if val == 9:
            part.add((i,j))
        
        for x, y in [(-1,0), (0,1), (1,0), (0, -1)]:
            if grid.get((i + x, j + y)) == val + 1:
                queue.append((i + x, j + y))
    p1 += len(part)

print(p1)

# Part Two
p2 = 0
for s in start:
    queue = deque()
    i, j = s
    queue.append((i,j))
    while queue:
        i,j = queue.pop()
        value = grid[(i,j)]
        for x,y in [(1,0), (0,1), (-1,0), (0,-1)]:
            if grid.get((i + x,j + y)) == value + 1:
                
                if grid[(i + x,j + y)] == 9:
                    p2 += 1
                else:         
                    queue.append((i + x,j + y))
    

print(p2)