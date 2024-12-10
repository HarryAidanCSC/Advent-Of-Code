from pathlib import Path

grid = {}
start = []

for i, line in enumerate(lines):
    for j, val in enumerate(line):
        grid[(i,j)] = int(val)
        if val == '0': start.append((i,j))

from collections import deque

queue = deque()

p1 =  0

for s in start:
    queue.append(s)
    part = set()
    visited = set()
    while queue:
        i,j = queue.pop()
        val = grid[(i,j)]
        visited.add((i,j))
        
        if val == 9:
            part.add((i,j))
        
        for x, y in [(-1,0), (0,1), (1,0), (0, -1)]:
            if grid.get((i + x, j + y)) == val + 1 and (i + x, j + y) not in visited:
                queue.append((i + x, j + y))
    p1 += len(part)
              
print(p1,'\n/n' )