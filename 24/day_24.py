# %%
from pathlib import Path
from collections import deque
with open(Path(__file__).parent.parent / "24/input.txt", "r") as file:
    lines = [line.strip() for line in file]


split_index = lines.index("") if "" in lines else len(lines)
wires = {wire.split(": ")[0]: int(wire.split(": ")[1]) for wire in lines[:split_index]}
gates = {gate.split(" -> ")[1]: gate.split(" -> ")[0] for gate in lines[split_index + 1:]}

queue = deque()
queue.extend(list(gates.keys()))

operations = {
    'AND': lambda x,y: x and y,
    'XOR': lambda x,y: x ^ y,
    'OR': lambda x,y: x or y
}

# Part One
p1_dict = {}
while queue:
    cur = queue.popleft()
    value = gates[cur]
    x,operation, y = value.split(" ")
    
    if x in wires and y in wires:
        bit = operations[operation](wires[x], wires[y])
        if cur.startswith('z'):
            p1_dict[cur] = str(bit)
        else:
            wires[cur] = bit
    else:
        queue.append(cur)


sorted_p1 =  dict(sorted(p1_dict.items()))
p1 = "".join(reversed(list(sorted_p1.values())))
p1 = int(p1,2)
print(p1)