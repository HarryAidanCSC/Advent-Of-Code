from pathlib import Path
from collections import deque
from itertools import combinations
from copy import deepcopy

with open(Path(__file__).parent.parent / "20/input.txt", "r") as file:
    lines = [line.strip() for line in file]

grid = {}
dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
walls = set()
cheats = []

for y in range(0, len(lines)):
    for x in range(0, len(lines[0])):
        if lines[y][x] != "#":
            neighbor = []
            for dx, dy in dirs:
                dxx, dyy = x + dx, y + dy
                if (
                    0 <= dyy < len(lines)
                    and 0 <= dxx < len(lines[0])
                    and lines[dyy][dxx] != "#"
                ):
                    neighbor.append((dxx, dyy))
            grid[(x, y)] = neighbor

            if lines[y][x] == "S":
                coords = (x, y)
            elif lines[y][x] == "E":
                end = (x, y)

        else:
            walls.add((x, y))

queue = deque()
queue.append([coords, 0])
visited = {coords: 0}
while queue:
    xy, n = queue.popleft()
    nodes = grid.get(xy)
    for node in nodes:
        if node not in visited or visited[node] > n + 1:
            visited[node] = n + 1
            if node != end:
                queue.append([node, n + 1])

baseline = visited[end]

part1, part2 = 0, 0
coords_check = list(combinations(list(visited.keys()), 2))
for p1, p2 in coords_check:
    x1, y1 = p1
    x2, y2 = p2
    manhattan = abs(x1 - x2) + abs(y1 - y2)

    if 1 < manhattan <= 20:
        s1, s2 = visited[p1], visited[p2]
        saved = s2 - s1 - manhattan
        if saved >= 100:
            part2 += 1
            if manhattan == 2:
                part1 += 1
print(part1, part2)
