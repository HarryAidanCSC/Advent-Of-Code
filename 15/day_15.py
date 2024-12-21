# %%
from pathlib import Path
from collections import deque
with open(Path(__file__).parent.parent / '15/hm.txt', 'r') as file:
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
print(p1)


# Part Two

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



import secrets

# Move boxes
for d in directions:
    if d in ["^", "v"]:
        next = map2[(coords[0] + dir[d][0], coords[1])]
        if next == ".": coords = (coords[0] + dir[d][0], coords[1]); continue
        if next == "#": continue

        dy = dir[d][0]
        queue = deque()
        visited = {(coords[0] + dy, coords[1]): coords}
        
        if next == "[":
            visit = ((coords[0] + dy, coords[1]), (coords[0] + dy, coords[1] + 1))
            visited[(coords[0] + dy, coords[1] + 1)] = coords
        elif next == "]":
            visit = ((coords[0] + dy, coords[1] - 1), (coords[0] + dy, coords[1]))
            visited[(coords[0] + dy, coords[1] - 1)] = coords

        queue.append(visit)
        flag = True

        while queue:
            c1, c2 = queue.popleft()
            val1, val2 = map2[(c1[0] + dy, c1[1])], map2[(c2[0] + dy, c2[1])]

            if val1 == "#" or val2 == "#":
                flag = False
                break
            elif val1 == "[" and val2 == "]":
                visited[(c1[0] + dy, c1[1])] = c1; visited[(c2[0] + dy, c2[1])] = c2
                queue.append(((c1[0] + dy, c1[1]), (c2[0] + dy, c2[1])))
            elif val1 == "]" and val2 == ".":
                visited[(c1[0] + dy, c1[1])] = c1; visited[c2[0] + dy, c2[1]] = c2; visited[(c1[0] + dy, c1[1] - 1)] = coords
                queue.append(((c1[0] + dy, c1[1]), (c1[0] + dy, c1[1] - 1)))
            elif val1 == "." and val2 == "[":
                visited[(c1[0] + dy, c1[1])] = c1; visited[(c2[0] + dy, c2[1])] = c2; visited[(c2[0] + dy, c2[1] + 1)] = coords
                queue.append(((c2[0] + dy, c2[1]), (c2[0] + dy, c2[1] + 1)))
            elif val1 == "]" and val2 == "[":
                visited[(c1[0] + dy, c1[1])] = c1; visited[(c1[0] + dy, c1[1] - 1)] = coords
                visited[(c2[0] + dy, c2[1])] = c2; visited[(c2[0] + dy, c2[1] + 1)] = coords
                queue.append(((c1[0] + dy, c1[1] - 1), (c1[0] + dy, c1[1])))
                queue.append(((c2[0] + dy, c2[1] ), (c2[0] + dy, c2[1] + 1)))
            elif val1 == "." and val2 == ".":
                visited[(c1[0] + dy, c1[1])] = c1
                visited[(c2[0] + dy, c2[1] )] = c2

        if flag:
            transform = {}          
            for key in visited:
                #print(key, visited[key])
                transform[key] = map2[visited[key]]
            for k in transform:
                map2[k] = transform[k]

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
        
        
    #print(coords, d)
    i = 0
    lines = []
    line = []
    crap = map2.copy()
    for g in crap:
        line.append(crap[g])
        i += 1
        if i == 100:
            line = "".join(line)
            line = line.replace("[.","[]")
            line = line.replace(".]", "[]")
            lines.append(line)
            i = 0
            line = []
            
            
            
    for i, line in enumerate(lines):
        for j, val in enumerate(line):
            map2[(i,j)] = val
            
            
            
            
            
            
            
            
    

# Sum up
p2 = 0
for key, value in map2.items():
    if value == "[":
        p2 += key[0] * 100 + key[1]
print(p2)















# %%
i = 0
line = []
for g in map2:
    line.append(map2[g])
    i += 1
    if i == 20:
        print("".join(line))
        i = 0
        line = []


# %%
gridy = [
    '####################',
    '##[].......[].[][]##',
    '##[]...........[].##',
    '##[]........[][][]##',
    '##[]......[]....[]##',
    '##..##......[]....##',
    '##..[]............##',
    '##.........[].[][]##',
    '##......[][]..[]..##',
    '####################'
]
map3 = {}
for i, line in enumerate(gridy):
    for j, val in enumerate(line):
        if val == "@": coords = (i,j); map[(i,j)] = "."
        else: map3[(i,j)] = val

###
p2 = 0
for key, value in map3.items():
    if value == "[":
        p2 += key[0] * 100 + key[1]
print(p2)

# %%

print(coords, d)
i = 0
line = []
for g in map2:
    line.append(map2[g])
    i += 1
    if i == 100:
        print("".join(line))
        i = 0
        line = []