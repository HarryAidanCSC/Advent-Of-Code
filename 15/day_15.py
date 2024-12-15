# %%
from pathlib import Path
with open(Path(__file__).parent.parent / '15/input.txt', 'r') as file:
    lines = [line.strip() for line in file]
    grid = [line for line in lines if "#" in line]
    directions = "".join([line for line in lines if any(char in line for char in ("<", ">", "^", "v"))])
    
map ={}
dir = {"^": (-1,0), "v": (1,0), "<": (0,-1), ">": (0,1)}

for i, line in enumerate(grid):
    for j, val in enumerate(line):
        if val == "@": coords = (i,j); map[(i,j)] = "."
        else: map[(i,j)] = val

# Part One
for d in directions:
    c = coords
    trailer = [coords]
    while map[(c[0] + dir[d][0], c[1] + dir[d][1])] == "O":
        c = (c[0] + dir[d][0], c[1] + dir[d][1])
        trailer.append(c)
        
    final_val = map[trailer[-1][0] + dir[d][0], trailer[-1][1] + dir[d][1]]
    if final_val == ".":
        for t in trailer[::-1]:
            map[(t[0] + dir[d][0], t[1] + dir[d][1])] = map[(t)]
    elif final_val == "#":
        continue # Nothing happens
    coords = (coords[0] + dir[d][0], coords[1] + dir[d][1])

p1 = 0
for key in map:
    if map[key] == "O":
        p1 += key[0] *100 + key[1]
print(p1)