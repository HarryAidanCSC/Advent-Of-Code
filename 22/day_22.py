
from pathlib import Path
from collections import defaultdict

with open(Path(__file__).parent.parent / "22/input.txt", "r") as file:
    lines = list(map(int, [line.strip() for line in file]))

p1 = 0
for a in lines:
    for _ in range(2000):
        b = ((a * 64) ^ a) % 16777216
        c = ((b // 32) ^ b) % 16777216
        a = ((c * 2048) ^ c) % 16777216

    p1 += a
  
king = defaultdict(int)

for a in lines:
    prev = int(str(a)[-1])
    p2a, p2b = [], []
    ans = {}
    for i in range(2000):

        b = ((a * 64) ^ a) % 16777216
        c = ((b // 32) ^ b) % 16777216
        a = ((c * 2048) ^ c) % 16777216

        val = int(str(a)[-1])

        if len(p2a) == 4:
            p2a.pop(0)
            p2b.pop(0)

        p2a.append(val)
        p2b.append(val - prev)

        if len(p2a) == 4:
            p2bb = tuple(p2b)
            maxval = p2a[-1]
            if p2bb not in ans.keys():
                ans[p2bb] = maxval
        prev = val

    for key, value in ans.items():
        king[key] += value

p2 = max(king, key=king.get)
print(p1, king[p2])
