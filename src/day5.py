from typing import Any
from utils import *
import itertools
import numpy as np

class Map:
    def __init__(self, readlines_input) -> None:
        self.name = readlines_input[0].split(' ')[0].replace('-', ' ').replace(' to ', '->')
        readlines_input = readlines_input[1:]
        self.destination_starts = []
        self.source_starts = []
        self.lengths = []
        for line in readlines_input:
            splt = line.split(' ')
            self.destination_starts.append(int(splt[0]))
            self.source_starts.append(int(splt[1]))
            self.lengths.append(int(splt[2]))
    
    def __call__(self, x, reverse=False) -> Any:
        if reverse:
            return self.reverse(x)
        else:
            return self.forward(x)
    
    def forward(self, x) -> Any:
        for idx in range(len(self.destination_starts)):
            if x >= self.source_starts[idx] and x < self.source_starts[idx] + self.lengths[idx]:
                return self.destination_starts[idx] + (x - self.source_starts[idx])
        return x
    
    def reverse(self, x) -> Any:
        for idx in range(len(self.destination_starts)):
            if x >= self.destination_starts[idx] and x < self.destination_starts[idx] + self.lengths[idx]:
                return self.source_starts[idx] + (x - self.destination_starts[idx])
        return x
        
    def __repr__(self) -> str:
        return f"<Map {self.name}>"
    
    def __str__(self) -> str:
        pass

maps = lines_separated_by_blank(readlines())
maps = func_every_element(maps, lambda x: x.strip('\n'))
seeds = func_every_element(maps[0][0].split(' ')[1:], int)
maps = maps[1:]
for idx, _map in enumerate(maps):
    maps[idx] = Map(_map)

def is_seed(seed_starts, seed_lenghts, x):
    if x is None:
        return False
    for idx in range(len(seed_starts)):
        if x >= seed_starts[idx] and x < seed_starts[idx] + seed_lenghts[idx]:
            return True
    return False


maps.reverse()

seed_starts = seeds[::2]
seed_lenghts = seeds[1::2]
seed_starts, seed_lenghts = (list(t) for t in zip(*sorted(zip(seed_starts, seed_lenghts))))

print(seed_starts)
print(seed_lenghts)

current_location = 0
current_seed = None

while not is_seed(seed_starts, seed_lenghts, current_seed):
    if current_location % 100000 == 0:
        print(current_location)
    loaction = current_location
    for _map in maps:
        loaction = _map(loaction, reverse=True)
    current_location += 1
    current_seed = loaction

answer = current_location - 1

print(answer)
#upload(answer)