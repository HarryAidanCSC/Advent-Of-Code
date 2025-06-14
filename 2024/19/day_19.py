# %%
from pathlib import Path
from collections import defaultdict
from functools import lru_cache

with open(Path(__file__).parent.parent / '19/input.txt', 'r') as file:
    towels, _, *patterns = file.read().strip().split('\n')

# Create dictionary
towels = towels.replace(",","").split()
towels_match = defaultdict(set)
for towel in towels:
    towels_match[towel[0]].add(towel)
for towel in towels_match:
    towels_match[towel] = sorted(towels_match[towel], key=len)

# For p2
patterns2 = []

p1 = 0
for p in patterns:
    lenp = len(p)
    visited = set()
    stack = [""]

    while stack:
        current_str = stack.pop()
        
        if current_str == p:
            p1 += 1
            patterns2.append(p)
            break

        idx = len(current_str)
        if idx >= lenp:
            continue

        char = p[idx]
        
        # Generate next states and avoid revisiting
        next_states = [
            current_str + towel
            for towel in towels_match[char]
            if current_str + towel not in visited and p.startswith(current_str + towel)
        ]
        
        visited.update(next_states)
        stack.extend(next_states)

@lru_cache(None)
def count_matches(p, idx):
    if idx == len(p):
        return 1

    if idx > len(p):
        return 0

    count = 0
    char = p[idx]

    for towel in towels_match[char]:
        next_idx = idx + len(towel)
        if p[idx:next_idx] == towel:
            count += count_matches(p, next_idx)

    return count

p2 = sum(count_matches(p, 0) for p in patterns2)

print(p1, p2)