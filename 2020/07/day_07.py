import re
from collections import defaultdict

with open("input.txt", "r") as f:
    lines = [
        line.strip().replace("bags", "").replace("bag", "").replace(".", "")
        for line in f
    ]

containers = defaultdict(list)
inverseContainer = defaultdict(list)

for line in lines:
    bags = [bag.strip() for bag in line.split(r" contain ")]
    for bag in bags[1].split(", "):
        if bag != "no other":
            containers[re.sub(r"[0-9]", "", bag).strip()].append(bags[0])
            inverseContainer[bags[0]].append(bag.strip())

visited = set()
stack = ["shiny gold"]
while stack:
    color = stack.pop()
    visited.add(color)
    next_colors = containers.get(color)
    if next_colors:
        for next_color in next_colors:
            stack.append(next_color)


stack = [(1, "shiny gold")]
p2 = 0
while stack:
    num, color = stack.pop()
    p2 += num
    next_colors = inverseContainer.get(color, None)
    if next_colors:
        for next_color in next_colors:
            next_num, col0, col1 = next_color.split(" ")
            next_num = int(next_num) * num
            col = col0 + " " + col1
            stack.append((next_num, col))


print(f"Part One: {len(visited) - 1}")
print(f"Part Two: {p2 - 1}")
