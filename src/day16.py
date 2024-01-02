from utils import *
import itertools
import numpy as np
import cProfile

#type 1: / or |
#type 2: \ or -

class Cell:
    def __init__(self, pos) -> None:
        self.pos = pos
        self.energized = False

    def energize(self):
        self.energized = True

    def __eq__(self, __value: object) -> bool:
        return self.pos == __value

class Mirror(Cell):
    def __init__(self, pos, _type) -> None:
        super().__init__(pos)
        self.type = _type

    def reflect(self, direction):
        if self.type == 1:
            if direction == "up":
                return "right"
            elif direction == "down":
                return "left"
            elif direction == "left":
                return "down"
            elif direction == "right":
                return "up"
        if self.type == 2:
            if direction == "up":
                return "left"
            elif direction == "down":
                return "right"
            elif direction == "left":
                return "up"
            elif direction == "right":
                return "down"

class Splitter(Cell):
    def __init__(self, pos, _type) -> None:
        super().__init__(pos)
        self.type = _type

    def split(self, direction):
        if self.type == 1:
            if direction == "left" or direction == "right":
                return ["up", "down"]
            elif direction == "up" or direction == "down":
                return direction
        elif self.type == 2:
            if direction == "left" or direction == "right":
                return direction
            elif direction == "up" or direction == "down":
                return ["left", "right"]

class Beam:
    def __init__(self, pos, direction, parent=None) -> None:
        self.id = 0 #np.random.randint(0, 1000000)
        self.pos = pos
        self.init_pos = pos.__copy__()
        self.history = []
        self.direction = direction
        self.init_direction = direction
        self.parent = parent

    def move(self):
        self.history.append({"pos": self.pos, "direction": self.direction})
        self.pos += direction_dict[self.direction]

    def change_direction(self, direction):
        self.direction = direction

    def is_out_of_bounds(self, width, height):
        return self.pos.x < 0 or self.pos.x >= width or self.pos.y < 0 or self.pos.y >= height

    def is_in_history(self, pos, direction):
        for h in self.history:
            if h["pos"] == pos and h["direction"] == direction:
                return True
        return False

    def __hash__(self) -> int:
        return hash((self.init_pos, self.init_direction))

    def __eq__(self, __value: object) -> bool:
        if isinstance(__value, Vector2):
            return self.pos == __value
        if isinstance(__value, Beam):
            return hash(self) == hash(__value)

    def __repr__(self) -> str:
        return f"Beam({self.init_pos}, {self.init_direction})"

    def __str__(self) -> str:
        return f"Beam({self.init_pos}, {self.init_direction})"

def main():
    data = read_to_2d_array()
    width = len(data[0])
    height = len(data)

    possible_starting_beams = []
    for y in range(len(data)):
        for x in range(len(data[y])):
            if x == 0:
                possible_starting_beams.append(Beam(Vector2(x, y), "right"))
            if x == width - 1:
                possible_starting_beams.append(Beam(Vector2(x, y), "left"))
            if y == 0:
                possible_starting_beams.append(Beam(Vector2(x, y), "down"))
            if y == height - 1:
                possible_starting_beams.append(Beam(Vector2(x, y), "up"))

    answer = 0
    for idx, beam in enumerate(possible_starting_beams):

        empty_space = []
        mirrors = []
        splitters = []
        for y in range(len(data)):
            for x in range(len(data[y])):
                pos = Vector2(x, y)
                if data[y][x] == '/':
                    mirrors.append(Mirror(pos, 1))
                elif data[y][x] == '\\':
                    mirrors.append(Mirror(pos, 2))
                elif data[y][x] == '|':
                    splitters.append(Splitter(pos, 1))
                elif data[y][x] == '-':
                    splitters.append(Splitter(pos, 2))
                elif data[y][x] == '.':
                    empty_space.append(Cell(pos))

        print("---------")
        print(f"{idx+1}/{len(possible_starting_beams)}")
        print(beam)
        beams = [beam]
        dead_beams = []
        _sum = 0
        while len(beams) > 0:
            beam = beams[0]
            if beam.is_out_of_bounds(width, height):
                beams.remove(beam)
                dead_beams.append(beam)
                continue
            if beam.is_in_history(beam.pos, beam.direction):
                beams.remove(beam)
                dead_beams.append(beam)
                continue

            try:
                current_empty = empty_space[empty_space.index(beam.pos)]
                if not current_empty.energized:
                    _sum += 1
                current_empty.energize()
            except ValueError:
                try:
                    m = mirrors[mirrors.index(beam.pos)]
                    if m == beam.pos:
                        if not m.energized:
                            _sum += 1
                        m.energize()
                        m.energize()
                        beam.change_direction(m.reflect(beam.direction))
                except ValueError:
                    try:
                        s = splitters[splitters.index(beam.pos)]
                        if s == beam.pos:
                            if not s.energized:
                                _sum += 1
                            s.energize()
                            new_direction = s.split(beam.direction)
                            if isinstance(new_direction, list):
                                beam.change_direction(new_direction[0])
                                for i in range(1, len(new_direction)):
                                    new_beam = Beam(beam.pos, new_direction[i], beam)
                                    if new_beam not in beams and new_beam not in dead_beams:
                                        beams.append(new_beam)
                            else:
                                beam.change_direction(new_direction)
                    except ValueError:
                        raise ValueError(f"Beam is not in any list: {beam}")
            beam.move()
            #print(_sum, len(beams), len(dead_beams))

        print(f"Sum: {_sum}")
        grid = np.zeros((height, width), dtype=int)
        for e in empty_space:
            if e.energized:
                grid[e.pos.y][e.pos.x] = 1
        for m in mirrors:
            if m.energized:
                grid[m.pos.y][m.pos.x] = 1
        for s in splitters:
            if s.energized:
                grid[s.pos.y][s.pos.x] = 1
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                if grid[y][x] == 0:
                    print(".", end="")
                elif grid[y][x] == 1:
                    print("#", end="")
            print()
        if _sum > answer:
            answer = _sum
        print(f"Current best answer: {answer}")

    print("---------")
    print(answer)
    #upload(answer)

if __name__ == "__main__":
    main()
    #cProfile.run("main()", sort="tottime")