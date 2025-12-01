from math import prod

with open("input.txt", "r") as file:
    lines = file.readlines()

for index, line in enumerate(lines):
    line_clean = line.rstrip("\n").split()[1:]
    lines[index] = [int(num) for num in line_clean]

partone = []
for index, time in enumerate(lines[0]):
    winners = 0
    time_range = range(0, time + 1)
    distance = lines[1][index]

    for button_press in time_range:
        value = (time - button_press) * button_press
        if value > distance:
            winners += 1
    partone.append(winners)

prod(partone)

for index, line in enumerate(lines):
    line = int("".join([str(item).strip() for item in line]))
    lines[index] = line

winners = 0
time_range = range(0, lines[0] + 1)
distance = lines[1]

for button_press in time_range:
    value = (int(lines[0]) - button_press) * button_press
    if value > distance:
        winners += 1
print(winners)
