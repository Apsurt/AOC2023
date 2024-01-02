from utils import *
import itertools
import numpy as np

def hash_function(_str):
    val = 0
    for char in _str:
        val += ord(char)
        val *= 17
        val %= 256
    return val

class Lens:
    def __init__(self, label, focal_length) -> None:
        self.label = label
        self.focal_length = focal_length
    
    def __eq__(self, __value: object) -> bool:
        if isinstance(__value, str):
            return self.label == __value
        elif isinstance(__value, int):
            return self.focal_length == __value
        elif isinstance(__value, Lens):
            return self.focal_length == __value and self.label == __value
        else:
            return False
    
    def __repr__(self) -> str:
        return f"{self.label}={self.focal_length}"
    
    def __str__(self) -> str:
        return f"Lens({self.label}={self.focal_length})"

class Box:
    def __init__(self, _id) -> None:
        self.id = _id
        self.lenses = []
        self.index = self.lenses.index
        self.append = self.lenses.append
        self.remove = self.lenses.remove
    
    def calculate_focusing_power(self):
        _sum = 0
        for idx, lens in enumerate(self):
            _sum += (self.id+1) * (idx+1) * lens.focal_length
        return _sum
    
    def __getitem__(self, __index):
        return self.lenses[__index]
    
    def __iter__(self):
        return self.lenses.__iter__()
    
    def __repr__(self) -> str:
        return f"Box({self.id})"
    
    def __str__(self) -> str:
        result = "Box("
        for idx, lens in enumerate(self):
            result += "    " if idx != 0 else ""
            result += lens.__repr__() 
            result += "\n" if idx != len(self.lenses)-1 else ""
        result += ")"
        return result

data = read_stream().strip()
strs = data.split(",")

boxes = [Box(i) for i in range(256)]

for _str in strs:
    if "=" in _str:
        label, focal_length = _str.split("=")
        focal_length = int(focal_length)
        box = boxes[hash_function(label)]
        if not label in box:
            box.append(Lens(label, focal_length))
        else:
            box[box.index(label)].focal_length = focal_length
    elif "-" in _str:
        label = _str.strip("-")
        box = boxes[hash_function(label)]
        try:
            box.remove(label)
        except ValueError:
            pass
    else:
        raise RuntimeError("No key char found")

answer = 0

for box in boxes:
    answer += box.calculate_focusing_power()

print(answer)
#upload(answer)