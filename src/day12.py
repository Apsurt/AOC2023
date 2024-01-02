from utils import *
import itertools
import numpy as np
from operator import add
import cProfile

translation_dict = {"?": 0, 0: "?",
                    "#": 1, 1: "#",
                    ".": -1, -1: "."}

def ami_print(row):
    for char in row:
        print(translation_dict[char], end="")
    print()

class Puzzle:
    def __init__(self, working, damaged, unknown, hints) -> None:
        self.hints = hints
        self.length = np.max(working+damaged+unknown)+1
        self.row = np.zeros(self.length, dtype=int)
        for i in working:
            self.row[i] = -1
        for i in damaged:
            self.row[i] = 1
    
    def unfold(self):
        orginal = self.row.copy()
        orginal_hints = self.hints.copy()
        for _ in range(4):
            self.row = np.append(self.row, 0)
            for char in orginal:
                self.row = np.append(self.row, char)
            for char in orginal_hints:
                self.hints.append(char)
        self.length = len(self.row)
    
    def get_all_possibilities(self):
        possibilities = []
        value = self.hints
        ones = [[1]*x for x in value]
        n_groups = len(value)
        n_empty = self.length - sum(value) - (n_groups-1)
        opts = itertools.combinations(range(n_groups+n_empty), n_groups)
        for opt in opts:
            selected = [-1]*(n_groups+n_empty)
            ones_idx = 0
            for val in opt:
                selected[val] = ones_idx
                ones_idx += 1
            res_opt = [ones[val]+[-1] if val > -1 else [-1] for val in selected]
            res_opt = [item for sublist in res_opt for item in sublist][:-1]
            possibilities.append(res_opt)
        return possibilities
    
    def is_possible(self, possibility):
        _sum = list(map(add, self.row, possibility))
        if 0 in _sum:
            return False
        return True

data = readlines()
puzzles = []
for line in data:
    line.strip()
    line, hints = line.split(" ")
    hints = list(map(int, hints.split(",")))
    working = []
    damaged = []
    unknown = []
    for i in range(len(line)):
        char = line[i]
        match char:
            case "?": unknown.append(i)
            case ".": working.append(i)
            case "#": damaged.append(i)
    puzzles.append(
        Puzzle(working, damaged, unknown, hints))

answer = 0
for puzzle in puzzles:
    puzzle.unfold()
    arangments = 0
    possibilities = puzzle.get_all_possibilities()
    break
    for possibility in possibilities:
        if puzzle.is_possible(possibility):
            arangments += 1
    print(arangments)
    answer += arangments

print(answer)
print('done')
#upload(answer)