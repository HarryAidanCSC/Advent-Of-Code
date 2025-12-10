import re
import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds

with open("input.txt", "r") as f:
    lines = f.read().splitlines()

machines = []
for line in lines:
    t_match = re.search(r"\{([\d,]+)\}", line)
    targets = [int(x) for x in t_match.group(1).split(",")]
    buttons_part = line.split("{")[0]
    b_matches = re.findall(r"\(([\d,]+)\)", buttons_part)

    buttons = []
    for b in b_matches:
        buttons.append([int(x) for x in b.split(",")])
    machines.append([targets, buttons])

p2 = 0
for targets, buttons in machines:
    n_buttons = len(buttons)
    n_counters = len(targets)
    A = np.zeros((n_counters, n_buttons))
    for col, btn_indices in enumerate(buttons):
        for row in btn_indices:
            if row < n_counters:
                A[row, col] = 1
    c = np.ones(n_buttons)
    constraints = LinearConstraint(A, lb=targets, ub=targets)
    variable_bounds = Bounds(lb=np.zeros(n_buttons), ub=np.inf)
    res = milp(
        c=c,
        constraints=constraints,
        integrality=np.ones(n_buttons),
        bounds=variable_bounds,
    )
    p2 += int(np.round(np.sum(res.x)))

print(f"Part Two: {p2}")
