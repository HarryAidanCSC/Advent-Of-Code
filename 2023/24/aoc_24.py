# %%
# Day 24
import numpy as np

with open('input.txt', 'r') as file:
    lines = [line.strip().split() for line in file]
    lines = [[int(word.replace(",", "")) for word in line if word != "@"] for line in lines]
lines
# %%
## Part 1 Data
lines1 = []
for l in lines:
    lines1.append(l[:2] + l[3:5])


# %%
def check(a,b, boundaries = (200000000000000, 400000000000000)):
    try:
        A = np.array([[-a[2],b[2]], [-a[3],b[3]]])
        B = np.array([a[0]-b[0], a[1]-b[1]])
        x,y  = np.linalg.solve(A,B)
        xcoord = int(a[0]) + int(a[2]) * x
        ycoord = int(b[1]) + int(b[3]) * y 
        if boundaries[0] <=  xcoord <= boundaries[1] and boundaries[0] <=  ycoord <= boundaries[1]:
            if x >= 0 and y >= 0:
                return True
            else:
                return False
        else:
            return False
    except:
        return False


# %%
score = 0 
lines1 = []
for l in lines:
    lines1.append(l[:2] + l[3:5])

while len(lines1) > 0:
    l0 = lines1.pop()
    
    for l1 in lines:
        ans = check(l0, l1)
        if ans is True:
            score += 1

print(score)