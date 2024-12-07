# %%
from itertools import product
from pathlib import Path

with open(Path(__file__).parent / 'input.txt', 'r') as file:
    lines = [list(map(int, line.strip().replace(":", "").split())) for line in file]

# Part One
operators = {
    'multiply': lambda a, b: a * b,
    'add': lambda a,b: a + b,
}

p1 = 0
for line in lines:
    final_score = line.pop(0)
    combinations = list(product(list(operators.keys()), repeat=len(line) - 1))
    
    start = line.pop(0)
    for combo in combinations:
        score = start
        for i in range(len(line)):
            score = operators[combo[i]](score, line[i])
        if score == final_score:
            p1 += score
            break

# %%
# Part Two
with open(Path(__file__).parent / 'input.txt', 'r') as file:
    lines = [list(map(int, line.strip().replace(":", "").split())) for line in file]

operators['concat'] =  lambda a,b: int(str(a) + str(b))

p2 = 0
for line in lines:
    final_score = line.pop(0)
    combinations = list(product(list(operators.keys()), repeat=len(line) - 1))
    start = line.pop(0)
    for combo in combinations:
        score = start
        for i in range(len(line)):
            score = operators[combo[i]](score, line[i])
        if score == final_score:
            p2 += score
            break
    print("x")
    
print(p2)