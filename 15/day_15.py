# %%
from pathlib import Path
from collections import deque
with open(Path(__file__).parent.parent / '15/input.txt', 'r') as file:
    lines = [line.strip() for line in file]
    grid = [line for line in lines if "#" in line]
    directions = "".join([line for line in lines if any(char in line for char in ("<", ">", "^", "v"))])
    
map = {}
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


grid2 = grid.copy()
dbl_wide = {"#": "##", "O": "[]", ".": "..", "@": "@."}

map2 = {}
for i, line in enumerate(grid2):
    for key in dbl_wide:
        line = line.replace(key, dbl_wide[key])
    grid2[i] = line
    for j, val in enumerate(line):
        if val == "@": coords = (i,j); map2[(i,j)] = "."
        else: map2[(i,j)] = val


# Move boxes
for d in directions:
    if d in ["^", "v"]:
        next = map2[(coords[0] + dir[d][0], coords[1])]
        if next == ".": coords = (coords[0] + dir[d][0], coords[1]); continue
        elif next == "#": continue
        else:
            dy = dir[d][0]; queue = deque()
            visited = {(coords[0] + dy, coords[1]): coords}
            
            if next == "[":
                visit = ((coords[0] + dy, coords[1]), (coords[0] + dy, coords[1] + 1))
            elif next == "]":
                visit = ((coords[0] + dy, coords[1] - 1), (coords[0] + dy, coords[1]))
            
            flag = True
            queue.append(visit)
            while queue:
                c = queue.pop()
                c = sorted(c, key = lambda x: x[1])
                c1, c2 = c
                
                val1, val2 = map2[(c1[0] + dy, c1[1])], map2[(c2[0] + dy, c2[1])]
                
                if c1[1] >= c2[1]: print(c1,c2); print(map2[c1], map2[c2])
                if val1 == "#" or val2 == "#":
                    flag = False
                    break
                elif val1 == "[" and val2 == "]":
                    visited[(c1[0] + dy, c1[1])] = c1; visited[(c2[0] + dy, c2[1])] = c2
                    queue.append(((c1[0] + dy, c1[1]), (c2[0] + dy, c2[1])))
                elif val1 == "]" and val2 == ".":
                    visited[(c1[0] + dy, c1[1])] = c1; visited[c2[0] + dy, c2[1]] = c2
                    queue.append(((c1[0] + dy, c1[1]), (c1[0] + dy, c1[1] - 1)))
                elif val1 == "." and val2 == "[":
                    visited[(c1[0] + dy, c1[1])] = c1; visited[(c2[0] + dy, c2[1])] = c2
                    queue.append(((c2[0] + dy, c2[1]), (c2[0] + dy, c2[1] + 1)))
                elif val1 == "]" and val2 == "[":
                    visited[(c1[0] + dy, c1[1])] = c1
                    visited[(c2[0] + dy, c2[1])] = c2
                    queue.append(((c1[0] + dy, c1[1] - 1), (c1[0] + dy, c1[1])))
                    queue.append(((c2[0] + dy, c2[1] ), (c2[0] + dy, c2[1] + 1)))
                elif val1 == "." and val2 == ".":
                    visited[(c1[0] + dy, c1[1])] = c1
                    visited[(c2[0] + dy, c2[1] )] = c2
            from copy import deepcopy
            if flag == True:
                transform = {}   
                
                for key in visited:
                    transform[key] = map2[visited[key]]
                trans = deepcopy(transform)
                
                for val in visited.values():
                    map2[val]="."            
                
                for k in trans:
                    map2[k] = trans[k]

                # Move
                coords = (coords[0] + dy, coords[1])

        # Left or right
    elif d in ["<", ">"]:
        c = coords
        trailer = [coords]
        while map2[(c[0], c[1] + dir[d][1])] in ["[","]"]:
            c = (c[0], c[1] + dir[d][1])
            trailer.append(c)
        final_val = map2[trailer[-1][0], trailer[-1][1] + dir[d][1]]
        if final_val == ".":
            for t in trailer[::-1]:
                map2[(t[0], t[1] + dir[d][1])] = map2[(t)]
            coords = (coords[0], coords[1] + dir[d][1])
        elif final_val == "#":
            continue # Nothing happens
        

# Sum up
p2 = 0
for key, value in map2.items():
    if value == "[":
        p2 += key[0] * 100 + key[1]
print(p1)
print(p2)
