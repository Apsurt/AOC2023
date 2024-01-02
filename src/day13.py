from utils import *
import itertools
import numpy as np

"""
#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.
"""

class Grid(np.ndarray):
    def __init__(self, shape) -> None:
        super().__init__()
        self.shape = shape
        self.dtype = int
        self.width = shape[1]
        self.height = shape[0]
        self.sum = 0
    
    def compare_halfs_columns(self, first, second):
        for f_pointer, s_pointer in zip(range(len(first[0])), range(len(second[0])-1, -1, -1)):
            if np.any(first[:,f_pointer] != second[:,s_pointer]):
                return False
        return True
    
    def find_vertical_reflection(self):
        max_half_width = int(np.floor(self.width/2))
        for half_width in range(max_half_width):
            half_width += 1
            
            l_pointer = half_width
            lf_half = self[:,:half_width]
            ls_half = self[:,half_width:half_width*2]
            are_reflection = self.compare_halfs_columns(lf_half, ls_half)
            if are_reflection:
                self.print_halfs(lf_half, ls_half, "v")
                print(l_pointer)
                self.sum += l_pointer
            
            r_pointer = self.width - half_width
            rf_half = self[:,-half_width:]
            rs_half = self[:,-half_width*2:-half_width]
            are_reflection = self.compare_halfs_columns(rf_half, rs_half)
            if are_reflection:
                self.print_halfs(rf_half, rs_half, "v")
                print(r_pointer, self.width)
                self.sum += r_pointer
    
    def compare_halfs_rows(self, first, second):
        for f_pointer, s_pointer in zip(range(len(first)), range(len(second)-1, -1, -1)):
            if np.any(first[f_pointer] != second[s_pointer]):
                return False
        return True
    
    def find_horizontal_reflection(self):
        max_half_height = int(np.floor(self.height/2))
        for half_height in range(max_half_height):
            half_height += 1
            
            u_pointer = half_height
            uf_half = self[:half_height]
            us_half = self[half_height:half_height*2]
            are_reflection = self.compare_halfs_rows(uf_half, us_half)
            if are_reflection:
                self.print_halfs(uf_half, us_half, "h")
                print(u_pointer)
                self.sum += u_pointer*100
            
            d_pointer = self.height - half_height
            ds_half = self[-half_height:]
            df_half = self[-half_height*2:-half_height]
            are_reflection = self.compare_halfs_rows(df_half, ds_half)
            if are_reflection:
                self.print_halfs(df_half, ds_half, "h")
                print(d_pointer, self.height)
                self.sum += d_pointer*100
    
    def print_halfs(self, first, second, mode):
        if mode == "v":
            for y in range(len(first)):
                for _ in range(2):
                    if _ == 1:
                        print("|", end="")
                    for x in range(len(first[0])):
                        if _ == 0:
                            val = first[y,x]
                        else:
                            val = second[y,x]
                        if val == 0:
                            print(" ", end="")
                        else:
                            print("#", end="")
                print()
        elif mode == "h":
            for idx, half in enumerate([first, second]):
                for y in range(len(half)):
                    for x in range(len(half[y])):
                        print(" " if half[y,x] == 0 else "#", end="")
                    print()
                if idx == 0:
                    print("-"*len(half[0])*2)

data = lines_separated_by_blank()
data = func_every_element(data, lambda x: x.strip())
grids = []
for grd in data:
    height = len(grd)
    width = len(grd[0])
    grid = Grid((height, width))
    for y in range(len(grd)):
        for x in range(len(grd[y])):
            if grd[y][x] == "#":
                grid[y,x] = 1
    grids.append(grid)

answer = 0
for grid in grids:
    grid.find_horizontal_reflection()
    grid.find_vertical_reflection()
    print()
    answer += grid.sum

print(answer)
#upload(answer)