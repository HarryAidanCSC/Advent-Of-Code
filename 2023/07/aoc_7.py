from collections import Counter

# Read lines from input file
with open("input.txt", "r") as file:
    lines = [line.strip().split() for line in file]

# Define strength of cards
strength_cards = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
strength_value = list(range(len(strength_cards), 0, -1))  # Reversed range
strength_dict = dict(zip(strength_cards, strength_value))

# Iterate over each line in lines
for line in lines:
    # Extract characters from the first element of the line
    chars = list(line[0])

    # Count occurrences of characters
    count_dict = Counter(chars)

    # Extend line with maximum count and count of unique characters
    line.extend([max(count_dict.values()), len(count_dict.values())])

    # Calculate strength of each character and extend line with strengths
    strength = [strength_dict[char] for char in chars]
    line.extend(strength)

# Sort lines based on specified criteria
lines = sorted(lines, key=lambda x: (x[2], -x[3], x[4], x[5], x[6], x[7], x[8]))

# Calculate part_one
part_one = 0
for index, line in enumerate(lines):
    value = int(line[1]) * (index + 1)
    part_one += value

print(part_one)


# Read lines from input file
with open("input.txt", "r") as file:
    lines = [line.strip().split() for line in file]

# Define strength of cards
strength_cards = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]
strength_value = list(range(len(strength_cards), 0, -1))  # Reversed range
strength_dict = dict(zip(strength_cards, strength_value))

# Iterate over each line in lines
for line in lines:
    # Extract characters from the first element of the line
    chars = list(line[0])

    # Filter out 'J' characters
    noj_chars = [x for x in chars if x != "J"]

    # Count occurrences of characters
    count_dict = Counter(chars)
    count_dict_noj = Counter(noj_chars)

    # Calculate the number of 'J' characters
    number_jokers = count_dict["J"]

    # Extend line based on number of 'J' characters
    if number_jokers == 5:
        line.extend([5, 1])
    else:
        line.extend(
            [
                int(max(count_dict_noj.values()) + number_jokers),
                len(count_dict_noj.values()),
            ]
        )

    # Calculate strength of each character and extend line with strengths
    strength = [strength_dict[char] for char in chars]
    line.extend(strength)

# Sort lines based on specified criteria
lines = sorted(lines, key=lambda x: (x[2], -x[3], x[4], x[5], x[6], x[7], x[8]))

# Calculate part_two
part_two = 0
for index, line in enumerate(lines):
    value = int(line[1]) * (index + 1)
    part_two += value

print(part_two)
