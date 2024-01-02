from utils import *
import itertools
import numpy as np

class Sequence:
    def __init__(self, initial) -> None:
        self.sequences = [initial]
    
    def get_differences(self):
        while set(self.sequences[-1]) != set([0]) and len(self.sequences) > 0:
            differences = []
            for idx, element in enumerate(self.sequences[-1]):
                if idx == 0:
                    continue
                differences.append(element - self.sequences[-1][idx-1])
            self.sequences.append(differences)
    
    def extrapolate(self):
        for idx in range(len(self.sequences)-1, -1, -1):
            if idx == len(self.sequences)-1:
                self.sequences[idx].append(self.sequences[idx][-1])
            else:
                old_last = self.sequences[idx][-1]
                difference = self.sequences[idx+1][-1]
                new_last = old_last + difference
                self.sequences[idx].append(new_last)
    
    def extrapolate_backwards(self):
        for idx in range(len(self.sequences)-1, -1, -1):
            if idx == len(self.sequences)-1:
                self.sequences[idx].insert(0, self.sequences[idx][0])
            else:
                old_first = self.sequences[idx][0]
                difference = self.sequences[idx+1][0]
                new_first = old_first - difference
                self.sequences[idx].insert(0, new_first)

data = readlines()
data = func_every_element(data, lambda x: x.split(' '))
data = func_every_element(data, lambda x: int(x))

answer = 0

sequences = [Sequence(i) for i in data]
for seq in sequences:
    seq.get_differences()
    #seq.extrapolate()
    seq.extrapolate_backwards()
    #print(seq.sequences)
    answer += seq.sequences[0][0]

print(answer)
#upload(answer)