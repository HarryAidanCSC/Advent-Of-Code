from pathlib import Path
from itertools import combinations

with open(Path(__file__).parent.parent / '23/input.txt', 'r') as file:
    lines = set([tuple(line.strip().split("-")) for line in file])

unique_nodes = {val for line in lines for val in line}
t_nodes = {t for t in unique_nodes if t.startswith("t")}
groups = [group for group in combinations(unique_nodes, 3)]

p1 = 0
for group in groups:
    if not t_nodes.intersection(group):
        continue
    
    pairs = list(combinations(group, 2))
    
    if all(pair in lines or pair[::-1] in lines for pair in pairs):
            p1 += 1

# Part one
print(p1)