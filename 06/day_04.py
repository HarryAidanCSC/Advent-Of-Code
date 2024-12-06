# Just a merry 88592ms solution
from pathlib import Path

with open(Path(__file__).parent / 'input.txt', 'r') as file:
    lines = [line.strip() for line in file]


hashmap = dict()
for i, line in enumerate(lines):
    for j, val in enumerate(line):
        hashmap[(i,j)] = val
        if val == "^" : current = (i,j)
start = current

dir = [(-1,0),(0,1),(1,0),(0,-1)]
dir_index = 0
d = dir[dir_index]
visited = set()

while True:
    visited.add(current)    
    next = tuple(a + b for a,b in zip(current, d))
    value = hashmap.get(next)    
    
    if value == "." or value == "^":
        current = next
    elif value :
        dir_index = (dir_index + 1) % len(dir)
        d = dir[dir_index]
    else: break

print(len(visited))

## Part Two
p2 = 0
for i, line in enumerate(lines):
    for j, val in enumerate(line):
        value_store = hashmap[(i,j)]
        if value_store != ".": continue
        hashmap[(i,j)] = "#"
        
        visited_velo = set()
        dir_index = 0
        d = dir[dir_index]
        current = start
        while True:
            if current + d in visited_velo:
                p2 += 1
                break
            
            next = tuple(a + b for a,b in zip(current, d))
            value = hashmap.get(next)    
            
            if value == "." or value == "^":
                visited_velo.add(current + d)
                current = next
            elif value :
                dir_index = (dir_index + 1) % len(dir)
                d = dir[dir_index]
            else:
                break
            
        hashmap[(i,j)] = value_store

print(p2)
