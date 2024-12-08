# %%
from pathlib import Path

with open(Path(__file__).parent / 'input.txt', 'r') as file:
    lines = [list(line.strip()) for line in file]

maxi, maxj = len(lines) - 1, len(lines[0]) - 1

nodes = {}
p1 = set()
p2 = set()

for i, line in enumerate(lines):
    for j, val in enumerate(line):
        if val != ".": 
            if val in nodes:
                matching_nodes = nodes[val]               
                
                for i2, j2 in matching_nodes:
                    p2.add((i2, j2))
                    
                    for fx in range(-50, 50):
                        idiff = i - i2
                        jdiff = j - j2
                        v1 = (i + (fx * idiff), j + (fx * jdiff))
                        
                        if 0 <= v1[0] <= maxi and 0 <= v1[1] <= maxj:
                            p2.add(v1)
                            if fx == 1 or fx == -2:
                                p1.add(v1)

                nodes[val].append((i, j))
            else:
                nodes[val] = [(i, j)]

# Output results
print(len(p1))
print(len(p2))