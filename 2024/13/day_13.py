from pathlib import Path
import re
from sympy import symbols, Eq, solve

with open(Path(__file__).parent / 'input.txt', 'r') as file:
    data = [line.strip() for line in file if line.strip() != ""]

p1, p2 = 0, 0
for i in range(0, len(data) - 1, 3):
    n = list(map(int, re.findall(r'\d+', "".join(data[i:i+3]))))
    A,B = symbols('A B', integer = True)
    # Part One
    eq1, eq2 = Eq(n[0] * A + n[2] * B, n[4]), Eq(n[1] * A + n[3] * B, n[5])
    solutions = solve([eq1, eq2], (A, B))
    if solutions: p1 += solutions[A] * 3 + solutions[B]
    
    # Part Two
    eq1, eq2 = Eq(n[0] * A + n[2] * B, n[4] + 10000000000000), Eq(n[1] * A + n[3] * B, n[5] + 10000000000000)
    solutions = solve([eq1, eq2], (A, B))
    if solutions: p2 += solutions[A] * 3 + solutions[B]

print(p1, p2)
