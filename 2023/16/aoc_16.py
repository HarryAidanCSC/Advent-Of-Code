with open("input.txt", "r") as file:
    lines = [line.strip().split() for line in file]

for i, line in enumerate(lines):
    lines[i] = list(line[0].replace("\\", "¬"))

slash_dictionary = {"south": "west", "west": "south", "east": "north", "north": "east"}
gun_dictionary = {"south": "east", "east": "south", "north": "west", "west": "north"}
directions = {"north": (-1, 0), "south": (1, 0), "west": (0, -1), "east": (0, 1)}

from functools import lru_cache


@lru_cache(maxsize=None)
def player_move(starting_position, input_direction, max_position):

    movement = directions[input_direction]

    end_position = (
        starting_position[0] + movement[0],
        starting_position[1] + movement[1],
    )

    # Is end position out of bounds
    if max(end_position) >= max_position or min(end_position) < 0:
        return None
    else:
        return end_position


@lru_cache(maxsize=None)
def player_behave(input_direction, char, starting_position):

    # If char is a blank
    if char == ".":
        return input_direction
    elif char == "/":
        return slash_dictionary[input_direction]
    elif char == "¬":
        return gun_dictionary[input_direction]
    elif char == "|":
        if input_direction in ["north", "south"]:
            return input_direction
        else:
            secondary_coord_dump.append([starting_position, "south"])
            return "north"
    elif char == "-":
        if input_direction in ["east", "west"]:
            return input_direction
        else:
            secondary_coord_dump.append([starting_position, "east"])
            return "west"


secondary_coord_dump = [[(0, 110), "north"]]
coord_store = set()
max_position = len(lines)

while secondary_coord_dump:

    starting_position = secondary_coord_dump[0][0]
    input_direction = secondary_coord_dump[0][1]
    del secondary_coord_dump[0]

    while starting_position is not None:
        starting_position = player_move(
            starting_position, input_direction, max_position
        )
        if starting_position is None:
            break
        char = lines[starting_position[0]][starting_position[1]]
        input_direction = player_behave(input_direction, char, starting_position)
        velodrome = (starting_position, input_direction)
        if velodrome in coord_store:
            break
        coord_store.add(velodrome)

print(len({t[0] for t in coord_store}))

nested_list = [
    [[(x, -1), "east"] for x in range(0, 110)],
    [[(110, x), "north"] for x in range(110)],
    [[(x, 110), "west"] for x in range(110)],
    [[(-1, x), "south"] for x in range(110)],
]

primary_coord_dump = [item for sublist in nested_list for item in sublist]

pt2_store = []

for y in flattened_list:
    player_behave.cache_clear()

    secondary_coord_dump = [y]
    coord_store = set()
    max_position = len(lines)

    while secondary_coord_dump:

        starting_position = secondary_coord_dump[0][0]
        input_direction = secondary_coord_dump[0][1]
        del secondary_coord_dump[0]

        while starting_position is not None:
            starting_position = player_move(
                starting_position, input_direction, max_position
            )
            if starting_position is None:
                break
            char = lines[starting_position[0]][starting_position[1]]
            input_direction = player_behave(input_direction, char, starting_position)
            velodrome = (starting_position, input_direction)
            if velodrome in coord_store:
                break
            coord_store.add(velodrome)

    pt2_store.append(len({t[0] for t in coord_store}))

print(max(pt2_store))
