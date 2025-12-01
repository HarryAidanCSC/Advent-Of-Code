from collections import deque
import numpy as np
import math

with open("input.txt", "r") as file:
    lines = [line.strip().replace(",", "").split() for line in file]
# Initialise coordinate lists
plot_coords = []
rock_coords = []
start_coords = []

# Dictionary to map characters to coordinate lists
store_dictionary = {"S": "start", "#": "rock", ".": "plot"}


def process_lines(lines):
    for i1 in range(len(lines)):
        for i2 in range(len(lines[i1][0])):
            char = lines[i1][0][i2]
            coord_list_name = store_dictionary[char] + "_coords"
            globals()[coord_list_name].append((i2, i1))


process_lines(lines)

# Add the first start coordinate to plot coordinates
plot_coords.append(start_coords[0])


# Function to generate node connections
def generate_nodes(plot_coords):
    nodes = {}
    for entry in plot_coords:
        x, y = entry
        combinations = [(x, y + 1), (x + 1, y), (x, y - 1), (x - 1, y)]
        valid_combinations = [comb for comb in combinations if comb in plot_coords]
        nodes[entry] = valid_combinations
    return nodes


# Generate nodes with connections
nodes = generate_nodes(plot_coords)


def bfs_with_max_steps(graph, start, max_steps):
    queue = deque([(start, 0)])
    visited_at_level = {start: 0}
    result = []

    while queue:
        node, steps = queue.popleft()

        if steps <= max_steps:
            result.append((node, steps))

        if steps >= max_steps:
            continue

        for neighbor in graph[node]:
            if (
                neighbor not in visited_at_level
                or visited_at_level[neighbor] > steps + 1
            ):
                visited_at_level[neighbor] = steps + 1
                queue.append((neighbor, steps + 1))

    return result


# Perform BFS with a maximum of 64 steps
ans = bfs_with_max_steps(nodes, start_coords[0], 64)


# Filter nodes where the number of steps is even
def filter_even_steps(ans):
    return [node for node, steps in ans if steps % 2 == 0]


# Part 1 solution
print(len(filter_even_steps(ans)))


# Part 2
# Function to replace 'S' with '.' and repeat the line 5 times
def process_lines(lines):
    pines = []
    for line in lines:
        pines.append([line[0].replace("S", ".") * 5])
    return pines


# Function to create a repeated list based on the number of repetitions
def create_repeated_list(pines, num_repeats):
    repeated_list = []
    num_sublists = len(pines)
    for _ in range(num_repeats):
        for j in range(num_sublists):
            repeated_list.append(pines[j])
    return repeated_list


pines = process_lines(lines)

repeated_list = create_repeated_list(pines, 5)

central_x = (len(repeated_list[0][0]) - 1) / 2
central_y = (len(repeated_list) - 1) / 2
plot_coords_pt2 = []
rock_coords_pt2 = []


def process_repeated_list(repeated_list):
    for row_index, row in enumerate(repeated_list):
        for col_index, char in enumerate(row[0]):
            coord_list_name = store_dictionary[char] + "_coords_pt2"
            globals()[coord_list_name].append((col_index, row_index))


process_repeated_list(repeated_list)


# Function to generate valid node connections
def generate_nodes_pt2(plot_coords):
    plot_coords_array = np.array(plot_coords)
    plot_coords_set = set(map(tuple, plot_coords_array))
    nodes = {}

    for entry in plot_coords_array:
        x, y = entry

        possible_combinations = np.array(
            [(x, y + 1), (x + 1, y), (x, y - 1), (x - 1, y)]
        )

        valid_combinations = [
            tuple(combination)
            for combination in possible_combinations
            if tuple(combination) in plot_coords_set
        ]

        nodes[tuple(entry)] = valid_combinations

    return nodes


nodes_pt2 = generate_nodes_pt2(plot_coords_pt2)
part_two = []

# Find number of reachable plots for each size
for p2 in range(0, 3):
    steps = 65 + (131 * p2)
    ans = bfs_with_max_steps(nodes_pt2, (int(central_x), int(central_y)), steps)

    if p2 % 2 == 0:
        remainder = 1
    else:
        remainder = 0

    temp_part_two = []

    for a in ans:
        if a[1] % 2 == remainder:
            temp_part_two.append(a[0])

    part_two.append((p2, len(temp_part_two)))
coefficients = np.polyfit(*zip(*part_two), 2)
result = np.polyval(coefficients, 202300)

# Part 2 solution
print(math.ceil(result))
