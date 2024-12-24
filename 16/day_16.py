# %%
from pathlib import Path
from collections import deque
with open(Path(__file__).parent.parent / '16/input.txt', 'r') as file:
    lines = [line.strip() for line in file]

# Define grid hashmap
grid = {}
for i, line in enumerate(lines):
    for j, val in enumerate(line):
        if val == "S": grid[(i,j)] = "."; coords = (i,j)
        else: grid[(i,j)] = val

start_coords = coords

# Init variables
queue = deque()
dirs = [(0,1),(1,0),(0,-1),(-1,0)]
points = 0
queue.append((coords, points, (0,1)))
visited = {(coords, (0,1)): points}
p1 = []

# BFS
while queue:
    coords, points, d = queue.popleft()
    for direct in dirs:
        c = (coords[0] + direct[0], coords[1] + direct[1])
        
        # if same direction only add 1
        if direct == d: p = points + 1
        else: p = points + 1001
        
        # If end
        if grid[c] == "E": p1.append(p); continue
        elif grid[c] == ".":
        
            # Check if visited before with current direction
            check = visited.get((c, direct))
            if check is None or check > p :
                visited[(c, direct)] = p
                queue.append((c, p, direct))

p1 = min(p1)
print(p1)

# Part Two
coords = start_coords
queue = deque()
steps = 0
queue.append((coords, 0, (0,1), set(), 0))
visited = {(coords, (0,1)): 0}
seen = {}
p2 = []

# BFS
while queue:
    coords, points, direction, seen, steps = queue.popleft()
    
    
    for new_direction in dirs:
        new_seen = set(seen)
        new_coords = (coords[0] + new_direction[0], coords[1] + new_direction[1])
        
        # if same direction only add 1
        new_points = points + (1 if new_direction == direction else 1001)

        
        if grid[new_coords] == "E" and new_points == p1:
            p2.append((new_seen, steps + 1)); continue
        elif grid[new_coords] == ".":
            check = visited.get((new_coords, new_direction))
            if check is None or check > new_points :
                new_seen.add(coords)
                visited[(new_coords, new_direction)] = new_points
                queue.append((new_coords, new_points, new_direction, new_seen, steps + 1))
            if check == new_points:
                new_seen.add(coords)
                queue.append((new_coords, new_points, new_direction, new_seen, steps + 1))

ans = set()
for p in p2:
    ans = ans | p[0]
print(len(ans) + 2)
