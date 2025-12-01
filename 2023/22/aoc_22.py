import itertools

with open("input.txt", "r") as file:
    lines = [
        [tuple(list(map(int, part.split(",")))) for part in line.strip().split("~")]
        for line in file
    ]

lines = sorted(lines, key=lambda x: x[0][2])
maxx = max(part[0] for line in lines for part in line)
maxy = max(part[1] for line in lines for part in line)
minx = min(part[0] for line in lines for part in line)
miny = min(part[1] for line in lines for part in line)

grid_squares = list(itertools.product(range(minx, maxx + 1), range(miny, maxy + 1)))
grid = {grid_square: 0 for grid_square in grid_squares}
occupant = {grid_square: None for grid_square in grid_squares}
safe = list(range(len(lines)))
rest_dict = {item: None for item in list(range(len(lines)))}


for i, l in enumerate(lines):
    item1, item2 = l

    x = list(range(item1[0], item2[0] + 1))
    y = list(range(item1[1], item2[1] + 1))
    z = item1[2]

    coords = list(itertools.product(x, y))

    max_val = 0

    # For all x-y find the highest point on the grid
    for coord in coords:
        check = (coord[0], coord[1])
        val = grid[check]
        max_val = max(max_val, val)

    resting_ons = set()

    # Find what blocks occupy the supprting sqaures in the grid
    for coord in coords:
        check = (coord[0], coord[1])
        val = grid[check]
        if val == max_val:
            resting_on = occupant[check]
            resting_ons.add(resting_on)

    if len(resting_ons) == 1:
        if list(resting_ons)[0] in safe:
            safe.remove(list(resting_ons)[0])

    zdiff = item2[2] - item1[2]
    max_val += 1 + zdiff

    for coord in coords:
        check = (coord[0], coord[1])
        grid[check] = max_val
        occupant[check] = i

    rest_dict[i] = resting_ons
print(len(safe))

from collections import deque


def bfs(graph, start, secondary_graph):

    result = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()
        result.add(node)

        for neighbor in graph[node]:
            if neighbor is not None:
                supporting_nodes = secondary_graph[neighbor]
                if all(
                    supporting_node in result for supporting_node in supporting_nodes
                ):
                    print("x")
                    queue.append((neighbor))

    return len(result) - 1


support_dict = {item: set() for item in list(range(len(lines)))}
for i, item in enumerate(rest_dict.values()):
    for val in item:
        if val is not None:
            support_dict[val].add(i)
counter = 0

for i in range(len(lines)):
    a = bfs(support_dict, i, rest_dict)
    counter += a
print(counter)
