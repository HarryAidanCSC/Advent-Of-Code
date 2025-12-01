with open("input.txt", "r") as file:
    lines = [line.strip().split() for line in file]

movement = {
    "R": [(1, 0)],
    "L": [(-1, 0)],
    "U": [(0, -1)],
    "D": [(0, 1)],
    "0": [(1, 0)],
    "2": [(-1, 0)],
    "1": [(0, -1)],
    "3": [(0, 1)],
}


def shoelace(coords):
    n = len(coords)
    area = 0

    for i in range(n):
        x1, y1 = coords[i]
        x2, y2 = coords[(i + 1) % n]
        area += x1 * y2 - y1 * x2

    area = abs(area) / 2
    return area


coords = (0, 0)
pt1 = [coords]
value_store_pt1 = 0
for line in lines:
    value = int(line[1])
    direction = movement[line[0]]
    move = [(x * value, y * value) for x, y in direction]
    coords = (move[0][0] + coords[0], move[0][1] + coords[1])
    pt1.append(coords)
    value_store_pt1 += value

coords = (0, 0)
pt2 = [coords]
value_store_pt2 = 0
for line in lines:
    value = int(line[2][2:-2], 16)
    direction = movement[line[2][-2:-1]]
    move = [(x * value, y * value) for x, y in direction]
    coords = (move[0][0] + coords[0], move[0][1] + coords[1])
    pt2.append(coords)
    value_store_pt2 += value

print(shoelace(pt1) + value_store_pt1 / 2 + 1)
print(shoelace(pt2) + value_store_pt2 / 2 + 1)
