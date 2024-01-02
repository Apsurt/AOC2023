from utils import *
import itertools
import numpy as np

translation_dict = {".": 0, 0: ".",
                    "#": -1, -1: "#",
                    "O": 1, 1: "O"}

class RockMap:
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height
        self.grid = np.zeros((self.height, self.width), dtype=int)
    
    def __getitem__(self, __index):
        return self.grid[__index]
    
    def __setitem__(self, __index, __value):
        self.grid[__index] = __value
    
    def __str__(self) -> str:
        result = ""
        for y in range(len(self.grid)):
            for x in range(len(self.grid[y])):
                result += translation_dict[self.grid[y,x]]
            result += "\n"
        return result[:-1]

data = read_to_2d_array()
height = len(data)
width = len(data[0])

rock_map = RockMap(width, height)

for y in range(len(data)):
    for x in range(len(data[y])):
        print(y,x)
        rock_map[y,x] = translation_dict[data[y][x]]

answer = 0

print(answer)
#upload(answer)