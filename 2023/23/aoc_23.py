from collections import deque

with open("test.txt", "r") as file:
    lines = [list(line.strip().replace(",", "").split()[0]) for line in file]

graph = {}

for y, line in enumerate(lines):
    for x, val in enumerate(line):
        graph[x, y] = val


nodes = {}

maxx = len(lines[0])
maxy = len(lines)

for key in graph.keys():

    value = graph[key]

    if value == "#":
        continue

    coord_store = []

    if value == ">":
        coord_store.append((key[0] + 1, key[1]))
    elif value == "<":
        coord_store.append((key[0] - 1, key[1]))
    elif value == "^":
        coord_store.append((key[0], key[1] - 1))
    elif value == "v":
        coord_store.append((key[0], key[1] + 1))
    else:

        possible_coords = [
            (key[0] + 1, key[1]),
            (key[0] - 1, key[1]),
            (key[0], key[1] + 1),
            (key[0], key[1] - 1),
        ]

        for coords in possible_coords:
            if 0 <= coords[0] < maxx and 0 < coords[1] < maxy:
                char = graph[coords]
                if char != "#":
                    coord_store.append(coords)

    nodes[key] = coord_store


def bfs_longest_path(graph, start, goal):
    queue = deque([(start, [start])])
    longest_path = []

    while queue:
        current_node, path = queue.popleft()
        if current_node == goal:
            if len(path) > len(longest_path):
                longest_path = path
            continue

        for neighbor in graph[current_node]:
            if neighbor not in path:
                queue.append((neighbor, path + [neighbor]))

    return longest_path if longest_path else None


longest_path = bfs_longest_path(nodes, (1, 0), (maxx - 2, maxy - 1))
print(len(longest_path) - 1)

########### P2

from collections import deque
from copy import deepcopy

with open("input.txt", "r") as file:
    lines = [list(line.strip().replace(",", "").split()[0]) for line in file]

graph = {}

for y, line in enumerate(lines):
    for x, val in enumerate(line):
        graph[x, y] = val


nodes = {}

maxx = len(lines[0])
maxy = len(lines)

for key in graph.keys():

    value = graph[key]
    coord_store = []

    if value == "#":
        continue

    else:
        possible_coords = [
            (key[0] + 1, key[1]),
            (key[0] - 1, key[1]),
            (key[0], key[1] + 1),
            (key[0], key[1] - 1),
        ]

        for coords in possible_coords:
            if 0 <= coords[0] < maxx and 0 <= coords[1] < maxy:
                char = graph[coords]
                if char != "#":
                    coord_store.append(coords)

    nodes[key] = coord_store
junctions = {}

for n in nodes:
    if len(nodes[n]) >= 3:
        output = deepcopy(nodes[n])
        output = [[x, 1] for x in output]
        junctions[n] = output

banlist = set()
hallways = {}

queue_major = deque([(1, 0)])

while queue_major:
    n = queue_major.popleft()

    if n in banlist:
        continue

    start = n
    hallway = set()
    hallway.add(n)
    queue = deque([n])
    breakflag = False

    while queue:
        key = queue.popleft()
        val = nodes[key]
        if len(val) <= 2:
            for v in val:
                if v not in hallway:
                    hallway.add(v)
                    queue.append(v)
        else:
            hallway.add(v)
            for v2 in val:
                if v2 not in hallway:
                    queue_major.append(v2)
            continue

    banlist.update(hallway)

    if (13, 14) in hallway:
        print(start, "\n", hallway)
        break

    if (21, 22) in hallway:
        hallways[start] = [[(21, 22), len(hallway) - 1]]
    else:
        hallways[start] = [[key, len(hallway) - 1]]
    if key != (21, 22):

        feeders = junctions[key]
        for f in feeders:
            if f[0] in hallway:
                f[0] = start  # Update the first element
                f[1] = len(hallway) - 1


nodes2 = deepcopy(junctions)
nodes2.update(hallways)


def get(coords):
    x, y = coords
    print(
        lines[y - 1][x - 1 : x + 2],
        "\n",
        lines[y][x - 1 : x + 2],
        "\n",
        lines[y + 1][x - 1 : x + 2],
    )


get((13, 14))
nodes[13, 14]


def bfs_longest_path_to_target(graph, start, target):
    queue = deque([(start, 0, {start})])  # (current_node, current_length, visited_set)
    longest_path = 0  # Initialize to -1 to check if the target is reachable

    po = []

    while queue:
        current_node, current_length, visited = queue.popleft()
        # print(current_node, current_length, visited)
        # Check if we've reached the target node
        if current_node == target:
            longest_path = max(longest_path, current_length)
            po.append([current_length, visited])
            continue  # Continue to explore other paths

        # Explore neighbors
        for neighbor, weight in graph.get(current_node, []):
            if neighbor not in visited:  # Check if neighbor is already visited
                new_visited = visited | {neighbor}  # Create new visited set
                queue.append((neighbor, current_length + weight, new_visited))

    return longest_path, po


longest_path_length, tank = bfs_longest_path_to_target(nodes2, (1, 0), (21, 22))

longest_path_length

visited = {(1, 0), (13, 9)}
current_length = 65

for neighbor, weight in nodes2.get((13, 9), []):
    print(neighbor, weight)
    if neighbor not in visited:  # Check if neighbor is already visited
        new_visited = visited | {neighbor}
        print((neighbor, current_length + weight, new_visited))

import pandas as pd

df = pd.DataFrame(lines)
# 1

junctions = {}

for n in nodes:
    if len(nodes[n]) >= 3:
        output = deepcopy(nodes[n])
        output = [[x, 1] for x in output]
        junctions[n] = output


banlist = set(junctions.keys())
hallways = {}

queue_major = deque([(1, 0)])

while queue_major:
    n = queue_major.popleft()

    if n in banlist:
        continue

    start = n
    hallway = set()
    hallway.add(n)
    queue = deque([n])
    breakflag = False

    while queue:
        key = queue.popleft()
        val = nodes[key]
        if len(val) <= 2:
            for v in val:
                if v not in hallway:
                    hallway.add(v)
                    queue.append(v)
                    quay = key
        else:
            for v2 in val:
                if v2 not in hallway and v2 not in banlist:
                    queue_major.append(v2)
            continue

    banlist.update(hallway)

    if (13, 18) in hallway:
        print(start, key, hallway)
        print(quay)

    if (21, 22) in hallway:
        hallways[start] = [[(21, 22), len(hallway) - 1]]
    elif key in banlist:
        hallways[start] = [[quay, len(hallway) - 1]]
    else:
        hallways[start] = [[key, len(hallway) - 1]]


nodes2 = deepcopy(junctions)
nodes2.update(hallways)
nodes3 = deepcopy(nodes2)

for val in nodes2:
    for val1 in nodes2[val]:
        if nodes3.get(val1[0]) is not None:
            nodes3[val1[0]].append([val, val1[-1]])
        else:
            nodes3[val1[0]] = [[val, val1[-1]]]
nodes3[(1, 0)]
nodes3[3, 4]
nodes3[3, 5]
nodes3[3, 6]
nodes3[5, 12]
nodes3[5, 13]
nodes3[5, 14]
nodes3[12, 19]
nodes3[13, 19]
nodes3[13, 18]
nodes3[13, 14]
nodes3[13, 13]
nodes3[13, 12]
nodes3[11, 4]
nodes3[11, 3]
nodes3[12, 3]
nodes3[21, 10]
nodes3[21, 11]
nodes3[21, 12]
nodes3[19, 18]
nodes3[19, 19]
nodes3[19, 20]
nodes3[21, 22]


def bfs_longest_path_to_target(graph, start, target):
    queue = deque([(start, 0, {start})])  # (current_node, current_length, visited_set)
    longest_path = 0  # Initialize to -1 to check if the target is reachable

    while queue:
        current_node, current_length, visited = queue.popleft()
        # print(current_node, current_length, visited)
        # Check if we've reached the target node
        if current_node == target:
            longest_path = max(longest_path, current_length)
            continue  # Continue to explore other paths

        # Explore neighbors
        print(current_node)
        # for neighbor, weight in graph.get(tuple(current_node), []):
        for neighbor, weight in graph[current_node]:
            if neighbor not in visited:  # Check if neighbor is already visited
                new_visited = visited | {neighbor}  # Create new visited set
                queue.append((neighbor, current_length + weight, new_visited))

    return longest_path


longest_path_length = bfs_longest_path_to_target(nodes3, (1, 0), (140, 139))

print(longest_path_length)
print(nodes3)
