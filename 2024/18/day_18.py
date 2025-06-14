from pathlib import Path
from collections import deque

with open(Path(__file__).parent.parent / "18/input.txt", "r") as file:
    lines = [tuple(map(int, line.strip().split(","))) for line in file]

lines_p1 = set(lines[:1024])
grid = {}
dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

for x in range(0, 71):
    for y in range(0, 71):
        if (x, y) in lines_p1:
            continue
        else:
            neighbor = []
            for dx, dy in dirs:
                dxx, dyy = x + dx, y + dy
                if 0 <= dyy <= 70 and 0 <= dxx <= 70 and (dxx, dyy) not in lines_p1:
                    neighbor.append((dxx, dyy))
            grid[(x, y)] = neighbor


# Part One
queue = deque()
queue.append([(0, 0), 0])
visited = {(0, 0): 0}
while queue:
    xy, n = queue.popleft()
    nodes = grid.get(xy)
    for node in nodes:
        if node not in visited or visited[node] > n + 1:
            visited[node] = n + 1
            if node != (70, 70):
                queue.append([node, n + 1])

print(visited[70, 70])


# Part Two
for i in range(1025, len(lines)):
    byte = lines[i]
    del grid[byte]
    for dx, dy in dirs:
        new_byte = (byte[0] + dx, byte[1] + dy)
        if new_byte in grid:
            grid[new_byte].remove(byte)
    # Part One
    queue = deque()
    queue.append([(0, 0), 0])
    visited = {(0, 0): 0}
    flag = True

    while queue:
        xy, n = queue.popleft()
        nodes = grid.get(xy)
        for node in nodes:
            if node not in visited or visited[node] > n + 1:
                visited[node] = n + 1
                if node == (70, 70):
                    flag = False
                    break
                else:
                    queue.append([node, n + 1])

    if flag:
        print(byte)
        break
