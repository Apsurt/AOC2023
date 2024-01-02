from typing import Any
from utils import *
import itertools
import numpy as np

class Vertex(Vector2):
    def __init__(self, x, y, parent, child) -> None:
        super().__init__(x, y)
        self.parent = parent
        self.child = child

class Line:
    def __init__(self, point_1: Vertex, point_2: Vertex) -> None:
        if not isinstance(point_1, Vertex) or not isinstance(point_2, Vertex):
            raise TypeError("Points have to be objects of Vertex class")
        if not (point_1.x == point_2.x or point_1.y == point_2.y):
            raise ValueError("Line is gay (not straight)")
        self.point_1 = point_1
        self.point_2 = point_2
        self.length = np.abs(self.point_1.x-self.point_2.x)+np.abs(self.point_1.y-self.point_2.y)

def main():
    data = readlines()
    for line in data:
        line = line.strip('\n')
        _dir, n, color = line.split(" ")
        #color = color[2:-1]
        #translation = {0: "r", 1: "d", 2: "l", 3: "u"}
        #_dir = translation[int(color[-1])]
        #n = hex_to_dec(color[:-1])
        #print(_dir, n, color)

    answer = 0
    print(answer)

if __name__ == "__main__":
    import cProfile
    main()
    #cProfile.run("main()", sort="tottime")