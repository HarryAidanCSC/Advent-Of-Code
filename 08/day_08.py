# %%
from pathlib import Path

with open(Path(__file__).parent / 'input.txt', 'r') as file:
    lines = [list(line.strip()) for line in file]

# Find Node locations
maxi, maxj = len(lines) - 1, len(lines[0]) - 1

nodes= {}
p1 = set()

for i, line in enumerate(lines):
    for j, val in enumerate(line):
        if val != ".": 
            if nodes.get(val): 
                matching_nodes = nodes[val]
                for i2,j2 in matching_nodes:
                    v1 = (2 * i - i2, 2 * j - j2)
                    if v1[0] >= 0 and v1[0] <= maxi and v1[1] >= 0 and v1[1] <= maxj:
                        p1.add(v1)
                    v2 = (2 * i2 - i, 2 * j2 - j)
                    if v2[0] >= 0 and v2[0] <= maxi and v2[1] >= 0 and v2[1] <= maxj:
                        p1.add(v2)
                nodes[val].append((i,j))
            else: nodes[val] = [(i,j)]
print(len(p1))