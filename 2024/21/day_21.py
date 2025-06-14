# %%
from pathlib import Path
from functools import lru_cache
with open(Path(__file__).parent.parent / '21/input.txt', 'r') as file:
    lines = [list(line.split()[0]) for line in file]

dfs_dict = {
    "pad_one": {
    'A': (0, 2), '0': (0, 1),
    '1': (1, 0), '2': (1, 1), '3': (1, 2),
    '4': (2, 0), '5': (2, 1), '6': (2, 2),
    '7': (3, 0), '8': (3, 1), '9': (3, 2)
    }
}
dirs_dict = {
    (0,1): ">",
    (1,0): "^",
    (0,-1): "<",
    (-1,0): "v"
}
pad_two = {
    "A": (1, 2), '^': (1, 1), "v": (0, 1),
    "<": (0, 0), ">": (0, 2)
}

@lru_cache(None)
def dfs_pad(graph_string: str, start, end):
    if start == end: return ""
    
    graph = dfs_dict[graph_string]
    
    reversed_graph = {v: k for k, v in graph.items()}
    visited = {start: 0}
    path_visit = set((start))
    end_stack = []

    # Get the starting node's coordinates
    y,x = graph[start]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    dfs_stack = [(y,x, tuple(start),[])]
    
    while dfs_stack:
        y,x,seen,velo = dfs_stack.pop()
        steps = len(seen)
        for dx, dy in directions:
            neighbor_coords = (y + dy, x + dx)
            char = reversed_graph.get((neighbor_coords))
            
            if char:
                new_seen = seen + (char,)
                if tuple(set(new_seen)) not in path_visit:
                    path_visit.add(tuple(set(new_seen)))                    
                    
                    velo_new = velo + [(dy,dx)]
                    if char == end:
                        end_stack.append(velo_new)
                    else:
                        dfs_stack.append((neighbor_coords[0], neighbor_coords[1], new_seen, velo_new))
                    
                    nc = visited.get((char))
                    if nc is None or nc > steps + 1:
                        visited[char] = steps + 1
                    
    end_stack = [item for item in end_stack if len(item) == visited[end] - 1]
    output = []
    for stack in end_stack:
        output.append("".join([dirs_dict[i] for i in stack]))
        
    return output


# %%
# Create different stacks

def create_new_stacks(stack_input):
    stack1 = [""]
    for item in stack_input:
        if len(item) == 1:
            stack1 = [s1 + item[0] + "A" for s1 in stack1]
        elif len(item) > 1:
            stack1_1 = []
            for i in item:
                stack1_1.extend([s1 + i + "A" for s1 in stack1])
            stack1 = stack1_1
    return stack1

@lru_cache(None)
def parse_stack(stack):
    brand_new_stack = []

    prevy,prevx = pad_two['A']
    for inp in stack:
        y,x = pad_two[inp]
        diff = (y-prevy, x-prevx)
        
        # Arrows
        y_arrow = "^" * diff[0] if diff[0] > 0 else "v" * -diff[0]
        x_arrow = ">" * diff[1] if diff[1] > 0 else "<" * -diff[1]
        
        # Mix of directions
        directions = [str(y_arrow + x_arrow).strip(),
                    str(x_arrow + y_arrow).strip()]
        
        # If down into empty
        if prevx == 0 and prevy == 0 and diff[1] > 0 and diff[0] > 0:
            del directions[0]
        elif prevy == 1 and diff[1] < 0 and diff[0] < 0 and x == 0 and y == 0:
            del directions[-1]
        elif diff[0] == 0 and diff[1] == 0:
            directions = [""]
        elif diff[0] == 0 or diff[1] == 0:
            del directions[0]
        
        
        brand_new_stack.append(directions)
        prevy, prevx = y, x
    return brand_new_stack


p1 = 0
# Directional

for line in lines:
    stack0 = []
    start = "A"
    for l in line:
        stack0.append(dfs_pad("pad_one", start, l))
        start = l

    # Generate and process stacks
    stack1 = [parse_stack(new_stack) for new_stack in create_new_stacks(stack0)]
    stack2 = [parse_stack(new_stack) for stack in stack1 for new_stack in create_new_stacks(stack)]
    
    # End of iteration
    stacks2_2 = set()
    for stack in stack2:
        s = create_new_stacks(stack)
        stacks2_2 = stacks2_2.union(set(s))
    stacks2_2
    p1_1 = min([len(s) for s in stacks2_2])
    p1_2 = int("".join(filter(str.isdigit, line)))
    
    print(set([len(s) for s in stacks2_2]))
    print(f"{p1_1} * {p1_2} = {p1_1 * p1_2}")
    p1 += p1_1 * p1_2


# %% 
# Part Two
p2 = 0
for line in lines:
    stack0 = []
    start = "A"
    for l in line:
        stack0.append(dfs_pad("pad_one", start, l))
        start = l
    
    stacks = [parse_stack(new_stack) for new_stack in create_new_stacks(stack0)]
    for _ in range(24):
        stacks = [parse_stack(new_stack) for stack in stacks for new_stack in create_new_stacks(stack)]
    
    p2_1 = set()
    for stack in stacks:
        s = create_new_stacks(stack)
        p2_1 = p2_1.union(set(s))
    p1_1 = min([len(s) for s in p2_1])
    p1_2 = int("".join(filter(str.isdigit, line)))
    
    print(set([len(s) for s in p2_1]))
    print(f"{p1_1} * {p1_2} = {p1_1 * p1_2}")
    p2 += p1_1 * p1_2

print(p1, p2)