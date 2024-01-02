from utils import *
import itertools
import numpy as np


class Vector2:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
    
    def __str__(self) -> str:
        return f"Vector2({self.x}, {self.y})"
    
    def __repr__(self) -> str:
        return f"({self.x}, {self.y})"

translation_dict = {"up": Vector2(0, -1),
                    "down": Vector2(0, 1),
                    "left": Vector2(-1, 0),
                    "right": Vector2(1, 0)}

class PipeCell:
    def __init__(self, x, y, symbol) -> None:
        self.x = x
        self.y = y
        self.symbol = symbol
        self.connections = self.connections_from_symbol()
        self.distance = 0
    
    def connections_from_symbol(self):
        if self.symbol == "|":
            return ["up", "down"]
        elif self.symbol == "-":
            return ["left", "right"]
        elif self.symbol == "L":
            return ["up", "right"]
        elif self.symbol == "J":
            return ["up", "left"]
        elif self.symbol == "7":
            return ["down", "left"]
        elif self.symbol == "F":
            return ["down", "right"]
        elif self.symbol == ".":
            return []
        elif self.symbol == "S":
            return ["up", "down", "left", "right"]
        else:
            raise ValueError("Invalid symbol")
        
    def __str__(self) -> str:
        return f"({self.x}, {self.y}): {self.symbol}"
    
    def __repr__(self) -> str:
        return str(self.symbol)
    
    def __eq__(self, __value: object) -> bool:
        if isinstance(__value, PipeCell):
            return self.x == __value.x and self.y == __value.y and self.symbol == __value.symbol
        elif isinstance(__value, tuple):
            return (self.x, self.y) == __value
        elif isinstance(__value, str):
            return self.symbol == __value
        else:
            raise TypeError("Incorrect type")

class PipeMap:
    def __init__(self, width, height) -> None:
        self.grid = np.empty((width, height), dtype=PipeCell)
    
    def set_cell(self, x, y, symbol):
        self.grid[x, y] = PipeCell(x, y, symbol)
    
    def get_cell(self, x, y):
        if y < 0 or y >= len(self.grid):
            raise IndexError("Out of bounds")
        if x < 0 or x >= len(self.grid[y]):
            raise IndexError("Out of bounds")
        return self.grid[x,y]
    
    def get_symbol(self, symbol):
        locations = []
        for y in range(len(self.grid)):
            for x in range(len(self.grid[y])):
                if self.get_cell(x,y).symbol == symbol:
                    locations.append(self.get_cell(x,y))
        return locations
    
    def __str__(self) -> str:
        result = ""
        for y in range(self.grid.shape[1]):
            for x in range(self.grid.shape[0]):
                result += self.grid[x, y].__repr__()
            result += "\n"
        return result

data = read_to_2d_array()
width = len(data[0])
height = len(data)
pipes = PipeMap(width, height)
for y in range(len(data)):
    for x in range(len(data[y])):
        pipes.set_cell(x, y, data[y][x])
print(pipes)

def traverse_pipe_map(pipe_map):
    start = pipe_map.get_symbol("S")[0]
    q = [start]
    v = []
    while len(q) > 0:
        current_node = q.pop(0)
        if current_node in v:
            raise RuntimeError("in visited")
        v.append(current_node)
        for connection in current_node.connections:
            vec = translation_dict[connection]
            new_x = current_node.x+vec.x
            new_y = current_node.y+vec.y
            try:
                new_pipe_cell = pipe_map.get_cell(new_x,new_y)
                if new_pipe_cell.symbol != ".":
                    if not new_pipe_cell in v:
                        if not new_pipe_cell in q:
                            new_pipe_cell.distance = current_node.distance+1
                            q.append(new_pipe_cell)
            except:
                pass
    return v

answer = 0
vis = traverse_pipe_map(pipes)
for v in vis:
    if v.distance > answer:
        answer = v.distance

print(answer)
#upload(answer)