# %%
import re
from collections import defaultdict

with open("input.txt", "r") as f:
    lines = [
        line.strip().replace("bags", "").replace("bag", "").replace(".", "")
        for line in f
    ]

containers = defaultdict(list)

for line in lines:
    bags = [bag.strip() for bag in line.split(r" contain ")]
    for bag in bags[1].split(", "):
        if bag != "no other":
            containers[re.sub(r"[0-9]", "", bag).strip()].append(bags[0])

visited = set()
stack = ["shiny gold"]

while stack:
    color = stack.pop()
    visited.add(color)
    next_colors = containers.get(color)
    if next_colors:
        for next_color in next_colors:
            if next_color not in visited:
                stack.append(next_color)

print(f"Part One: {len(visited) - 1}")
