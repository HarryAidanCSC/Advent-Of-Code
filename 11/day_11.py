# %%
from pathlib import Path
with open(Path(__file__).parent / 'input.txt', 'r') as file:
    line = [line.strip().split(" ") for line in file][0]
line = [int(char) for char in line]

cache = {}
for _ in range(25):
    new_line = []
    for val in line:
        if val in cache.keys():
            new_line.extend(cache[val])
        else:
            if val == 0:
                new_val = [1]
            elif len(str(val)) % 2 == 0:
                n = len(str(val)) // 2
                left_val = int(str(val)[:n])
                right_val = int(str(val)[n:])
                new_val = [left_val, right_val]
            else:
                new_val = [val* 2024]
            
            new_line.extend(new_val)
                
            cache[val] = new_val
    line = new_line
print(len(line))


# %%
with open(Path(__file__).parent / 'input.txt', 'r') as file:
    line = [line.strip().split(" ") for line in file][0]
line = {int(char): 1 for char in line}

for _ in range(75):
    new_line = {}
    for key in line.keys():
        appear = line[key]
        
        if key in cache.keys():
            new_val = cache[key]
        else:
            if key == 0:
                new_val = [1]
            elif len(str(key)) % 2 == 0:
                n = len(str(key)) // 2
                left_val = int(str(key)[:n])
                right_val = int(str(key)[n:])
                new_val = [left_val, right_val]
            else:
                new_val = [key * 2024]
            cache[key] = new_val
            
        for nv in new_val:
            if nv in new_line.keys():
                new_line[nv] += appear
            else:
                new_line[nv] = appear
    
    line = new_line

p2 = sum(line.values())
print(p2)