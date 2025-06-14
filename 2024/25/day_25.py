# %%
from pathlib import Path
with open(Path(__file__).parent.parent / "25/input.txt", "r") as file:
    lines = [line.strip() for line in file]

prev = 0
keys, locks = [], []
for i in range(7, len(lines) + 7, 8):
    if all(char == "#" for char in lines[prev]):
        locks.append(lines[prev:i])
    else:
        keys.append(lines[prev:i])
    prev = i + 1

# Locks
locks_num = [[
        max(0, 8 - sum(1 for row in lock if row[i] == "#"))
        for i in range(len(lock[0]))]
    for lock in locks
    ]

# Keys
keys_num = [[
        sum(1 for row in key if row[i] == "#")
        for i in range(len(key[0]))]
    for key in keys
    ]

# Part one
p1 = 0
for lock in locks_num:
    for key in keys_num:
            if all(key[i] < lock[i] for i in range(len(key))):
                p1 += 1
p1