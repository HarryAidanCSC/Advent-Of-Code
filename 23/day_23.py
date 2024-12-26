# %%
from pathlib import Path
from itertools import combinations
from collections import defaultdict

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

def bron_kerbosch(R, P, X, graph, cliques):
    if not P and not X:
        cliques.append(R)
        return
    
    for v in list(P):
        bron_kerbosch(
            R.union({v}),
            P.intersection(graph[v]),
            X.intersection(graph[v]),
            graph,
            cliques
        )
        P.remove(v)
        X.add(v)

graph = defaultdict(list)

for l1, l2 in lines:
    graph[l1].append(l2)
    graph[l2].append(l1)

R, P, X = set(), set(graph.keys()), set()
cliques = []
bron_kerbosch(R, P, X, graph, cliques)

# P1 and P2
print(p1)
print(",".join(sorted(max(cliques, key=len))))
