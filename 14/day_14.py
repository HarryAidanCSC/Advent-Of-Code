from pathlib import Path
from re import findall
from math import prod
import matplotlib.pyplot as plt
import os

with open(Path(__file__).parent / 'input.txt', 'r') as file:
    lines = [line.strip().split(" ") for line in file]
    lines = [[tuple(map(int, findall(r'-?\d+', line[0]))), tuple(map(int,findall(r'-?\d+', line[1])))] for line in lines]

maxx, maxy = 100, 102
quadrants = {(0,0): 0, (1,0): 0, (0,1): 0, (1,1): 0}

for line in lines:
    x, y = line[0][0] + 100 * line[1][0],  line[0][1] + 100 * line[1][1]
    x, y =  x % (maxx + 1), y % (maxy + 1)
    if x == maxx // 2 or y == maxy // 2:
        continue
    q = (x > maxx // 2, y > maxy // 2)
    quadrants[q] += 1

coords = [line[0] for line in lines]
velo = [line[1] for line in lines]
sec = 1
start = coords

for _ in range(10000):
    coord_store = []
    for j, coord in enumerate(coords):
        x, y = coord[0] + velo[j][0], coord[1] + velo[j][1]
        x, y =  x % (maxx + 1), y % (maxy + 1)
        coord_store.append((x,y))

    coords = coord_store
    x = [c[0] for c in coords]
    y = [c[1] for c in coords]
    plt.figure(figsize=(5,5))
    plt.scatter(x, y, c='blue')
    plot_filename = os.path.join(f"plots/plot_{sec:04d}.png")
    plt.savefig(plot_filename, dpi=20)
    plt.close() 
    sec += 1 

# I'm guessing it wont take over 10k iterations to find the plot # %%
smallest_file = min([f for f in os.listdir("plots") if f.endswith('.png')], key=lambda f: os.path.getsize(os.path.join("plots", f)))
print(prod(quadrants.values()))
print(findall(r'\d+', smallest_file)[0])