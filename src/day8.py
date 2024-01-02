from utils import *
import numpy as np

class Node:
    def __init__(self, value, left, rigth) -> None:
        self.value = value
        self.left = left
        self.right = right
    
    def __repr__(self) -> str:
        return f'{self.value}'
    
    def __str__(self) -> str:
        return f'{self.value} ({self.left}, {self.right})'
    
    def __eq__(self, o: object) -> bool:
        return self.value == o
    
    def __getitem__(self, index):
        return self.value[index]

data = lines_separated_by_blank()
data = func_every_element(data, lambda x: x.strip())

instructions = data.pop(0)[0]
data = data[0]

nodes = []

for idx, node in enumerate(data):
    parent, children = node.split(' = ')
    children = children.strip('(')
    children = children.strip(')')
    children = children.split(', ')
    left, right = children
    nodes.append(Node(parent, left, right))

starts = []
goals = []
for node in nodes:
    if node.value[-1] == 'A':
        starts.append(node)
    if node.value[-1] == 'Z':
        goals.append(node)

periods = []
for node in starts:
    steps = 0
    last_z_steps = 0
    period = 0
    pointer = 0
    found_count = 0
    while found_count<1:
        try:
            instruction = instructions[pointer]
        except:
            pointer = 0
            instruction = instructions[pointer]

        if node[-1] == "Z":
            period = steps-last_z_steps
            found_count += 1
            last_z_steps = steps
            break

        match instruction:
            case "R":
                node_str = node.right
            case "L":
                node_str = node.left

        node_idx = nodes.index(node_str)
        node = nodes[node_idx]

        pointer += 1
        steps += 1
    periods.append(period)

print(periods)

answer = 11678319315857

print(answer)
#upload(answer)