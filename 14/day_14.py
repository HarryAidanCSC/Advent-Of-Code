from pathlib import Path
from re import findall
from math import prod
from statistics import stdev

with open(Path(__file__).parent / 'input.txt', 'r') as file:
    lines = [line.strip().split(" ") for line in file]
    lines = [[tuple(map(int, findall(r'-?\d+', line[0]))), tuple(map(int,findall(r'-?\d+', line[1])))] for line in lines]

maxx, maxy = 100, 102
quadrants = {(0,0): 0, (1,0): 0, (0,1): 0, (1,1): 0}

for line in lines:
    x, y = line[0][0] + 100 * line[1][0],  line[0][1] + 100 * line[1][1]
    x, y =  x % (maxx + 1), y % (maxy + 1)
    if x == maxx // 2 or y == maxy // 2:
        continue
    q = (x > maxx // 2, y > maxy // 2)
    quadrants[q] += 1

coords = [line[0] for line in lines]
velo = [line[1] for line in lines]
sec = 1
variance = []

for _ in range(10000):
    coord_store = []
    for j, coord in enumerate(coords):
        x, y = coord[0] + velo[j][0], coord[1] + velo[j][1]
        x, y =  x % (maxx + 1), y % (maxy + 1)
        coord_store.append((x,y))

    coords = coord_store
    x = [c[0] for c in coords]
    y = [c[1] for c in coords]
    variance.append(stdev(x) + stdev(y))
    sec += 1 
    
print(prod(quadrants.values()))
print(variance.index(min(variance)) + 1) 