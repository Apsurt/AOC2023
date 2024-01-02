from utils import *
import itertools
import numpy as np

class Galaxy:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
    
    def shortest_distance(self, other):
        dx = np.abs(self.x-other.x)
        dy = np.abs(self.y-other.y)
        return dx+dy
    
    def __repr__(self) -> str:
        return f"({self.x}, {self.y})"
    
    def __str__(self) -> str:
        return f"Galaxy({self.x}, {self.y})"

grid = np.array(read_to_2d_array())
galaxies = []
for y in range(len(grid)):
    for x in range(len(grid[y])):
        if grid[y,x] == "#":
            galaxies.append(Galaxy(x,y))


#horizontal expansion
n_lines = 1000000-1
expansions = 0
for y in range(len(grid)):
    true_y = y + (expansions*n_lines)
    if len(set(grid[y])) == 1 and grid[y,0] == ".":
        for gal_idx in range(len(galaxies)):
            if galaxies[gal_idx].y > true_y:
                galaxies[gal_idx].y += n_lines
        expansions += 1

expansions = 0
for x in range(len(grid[0])):
    true_x = x + (expansions*n_lines)
    if len(set(grid[:,x])) == 1 and grid[0,x] == ".":
        for gal_idx in range(len(galaxies)):
            if galaxies[gal_idx].x > true_x:
                galaxies[gal_idx].x += n_lines
        expansions += 1

galaxy_ids = list(itertools.combinations(range(len(galaxies)),2))
answer = 0
for galaxy_pair in galaxy_ids:
    gal_1 = galaxies[galaxy_pair[0]]
    gal_2 = galaxies[galaxy_pair[1]]
    distance = gal_1.shortest_distance(gal_2)
    answer += distance

print(answer)
#upload(answer)