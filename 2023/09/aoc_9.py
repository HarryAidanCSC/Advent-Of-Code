with open("input.txt", "r") as file:
    lines = [line.strip().split() for line in file]

for line in lines:
    for i, val in enumerate(line):
        line[i] = int(val)

import copy

partone = 0
part_one_lines = copy.deepcopy(lines)
x_diff_store = []

for line in part_one_lines:
    x_diff = []
    x_diff_store = [line]

    while True:
        for x in range(1, len(line)):
            x_diff.append(line[x] - line[x - 1])

        zero_test = all(item == 0 for item in x_diff)

        x_diff_store.append(x_diff)

        if zero_test:
            break
        else:
            line = x_diff
            x_diff = []

    for index, diff in enumerate(reversed(x_diff_store)):
        if index > 0:
            diff.append(diff[-1] + x_diff_store[len(x_diff_store) - index][-1])

    partone += x_diff_store[0][-1]

print(partone)

part_two_lines = copy.deepcopy(lines)
parttwo = 0


for line in part_two_lines:
    x_diff = []
    x_diff_store = [line]

    while True:
        for x in range(1, len(line)):
            x_diff.append(line[x] - line[x - 1])

        zero_test = all(item == 0 for item in x_diff)

        x_diff_store.append(x_diff)

        if zero_test:
            break
        else:
            line = x_diff
            x_diff = []

    for index, diff in enumerate(reversed(x_diff_store)):
        if index > 0:
            diff.insert(0, diff[0] - x_diff_store[len(x_diff_store) - index][0])

    parttwo += x_diff_store[0][0]

print(parttwo)
