# AOC Day 25
with open("input.txt", "r") as file:
    lines = [line.strip().split() for line in file]

for i, line in enumerate(lines):
    lines[i][0] = line[0][:-1]
clean = set()
for line in lines:
    for elem in line:
        clean.add(elem)

lookup = {}
for i, v in enumerate(list(clean)):
    lookup[v] = i
lines1 = []
for line in lines:
    value = lookup[line[0]]
    for elem in line[1:]:
        val = lookup[elem]
        edge = (value, val)
        lines1.append(edge)
import random
import copy


def karger_min_cut(graph):
    edges = copy.deepcopy(graph.edges)
    nodes = copy.deepcopy(graph.nodes)

    cuts_made = []
    supernodes = {node: [node] for node in nodes}

    while len(nodes) > 2:

        # Pick random edge
        u, v = random.choice(edges)
        cuts_made.append((u, v))
        # Merge u into v
        nodes.remove(u)

        supernodes[v].extend(supernodes[u])
        del supernodes[u]

        # Contract edges
        new_edges = []
        for edge in edges:
            if edge[0] == u:
                new_edge = (v, edge[1])
            elif edge[1] == u:
                new_edge = (edge[0], v)
            else:
                new_edge = edge

            # Remvoe self loops
            if new_edge[0] != new_edge[1]:
                new_edges.append(new_edge)

        edges = new_edges

    # The remaining edges are the cuts in the graph
    remaining_nodes = list(supernodes.keys())
    size_of_cut_group1, size_of_cut_group2 = (
        len(supernodes[remaining_nodes[0]]),
        len(supernodes[remaining_nodes[1]]),
    )

    # The number of edges between the two remaining nodes is the cut size
    cut_size = len(edges)
    return cut_size, size_of_cut_group1, size_of_cut_group2, nodes


class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.nodes = set([y for x in lines1 for y in x])


graph = Graph(lines1)

while True:
    cuts, size1, size2, nodes = karger_min_cut(graph)
    if cuts == 3:
        print(size1 * size2)
        break
