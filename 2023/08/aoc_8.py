import math

with open("input.txt", "r") as file:
    lines = [line.strip().split() for line in file]

instructions = list(str(lines[0]))[2:-2] * 10000

lines = lines[2:]
for line in lines:
    del line[1]
    line[1] = line[1].replace("(", "").replace(",", "")
    line[2] = line[2].replace(")", "")


def get_output(input_value, instruct):

    for x in lines:
        if x[0] == input:
            input_list = x
            continue

    if instruct == "L":
        output = input_list[1]
    if instruct == "R":
        output = input_list[2]

    return output


input = "AAA"
counter = 0

for ins in instructions:
    counter += 1
    input = get_output(input_value=input, instruct=ins)
    if input == "ZZZ":
        print(counter)
        break

start = []
for line in lines:
    if line[0][-1] == "A":
        start.append(line)

part_two = []

for input_list in start:
    input = input_list[0]
    counter = 0
    for ins in instructions:
        counter += 1
        input = get_output(input_value=input, instruct=ins)
        if input.endswith("Z"):
            part_two.append(counter)
            break


def lcm_multiple(args):
    result = args[0]
    for num in args[1:]:
        result = math.lcm(result, num)
    return result


print(lcm_multiple(part_two))
