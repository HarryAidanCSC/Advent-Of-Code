# Solved in 250ms (including imports)
from pathlib import Path
from itertools import product

with open(Path(__file__).parent / 'input.txt', 'r') as file:
    lines = [line.strip() for line in file]

map ={}
visit = set()

for i, line in enumerate(lines):
    for j, val in enumerate(line):
        map[(i,j)] = val
        visit.add((i,j))
        
dir = [(-1,0),(1,0),(0,1),(0,-1)]
p1 = 0
shapes = []

while visit:
    y, x = visit.pop()
    temp = set()
    round_visit = [(y,x)]
    touching  = 0
    
    while round_visit:
        y, x = round_visit.pop(0)
        temp.add((y,x))
        val = map[(y,x)]
    
        for yv, xv in dir:
            y2, x2 = y + yv, x + xv
            val2  = map.get((y2, x2))
            if val2 == val and (y2,x2)  in visit:
                visit.remove((y2,x2))
                round_visit.append((y2,x2))
            if val2== val:
                touching += 1
    
    a, p = len(temp), len(temp) * 4 - touching
    p1 += a*p
    shapes.append(temp)

dir2 = [(0,0), (-1,0),(-1,-1),(0,-1)]
p2 = 0
for shape in shapes:
    sides = 0
    miny, maxy = min([y for y,x in shape]), max([y for y,x in shape]) + 2
    minx, maxx = min([x for y,x in shape]), max([x for y,x in shape]) + 2
    
    corners = list(product(range(miny, maxy), range(minx, maxx)))
    for c in corners:
        check = [(c[0] + d[0], c[1] + d[1]) for d in dir2 if (c[0] + d[0], c[1] + d[1]) in shape]
        
        if len(check) == 1 or len(check) == 3: sides += 1
        elif len(check) == 0 or len(check) == 4: pass # nothing happens
        else: 
            diff = (check[0][0] - check[1][0], check[0][1] - check[1][1])
            if diff[0] in (1,-1) and diff[1] in (1,-1): sides +=2
    p2 += sides * len(shape)
    
print(p1, p2)
