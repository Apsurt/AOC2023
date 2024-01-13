from web_engine import WebEngine
import datetime

def get_day_from_date():
    datetime_object = datetime.datetime.now()
    if datetime_object.month != 12:
        raise Exception("Not in December")
    if datetime_object.day > 25:
        raise Exception("After December 25th")
    return datetime_object.day

def get_year_from_date():
    datetime_object = datetime.datetime.now()
    return datetime_object.year

#config = {"day": get_day_from_date(), "year": get_year_from_date()}
config = {"day": 19, "year": 2023}

def upload(answer):
    web = WebEngine(config)
    web.login()
    web.load_day_page()
    web.upload_answer(answer)

def read_stream():
    return "".join(readlines()).replace("\n", "")

def readlines():
    with open("/Users/tymonbecella/Desktop/AOC2023/src/inputs/day{}.txt".format(config["day"]), "r") as f:
        return f.readlines()

def read_to_2d_array():
    with open("/Users/tymonbecella/Desktop/AOC2023/src/inputs/day{}.txt".format(config["day"]), "r") as f:
        data = f.readlines()
        data = func_every_element(data, lambda x: x.strip('\n'))
        data = func_every_element(data, lambda x: list(x))
    return data

def func_every_element(iterable, func):
    for i in range(len(iterable)):
        try:
            if type(iterable[i]) == str:
                raise TypeError
            iterable[i] = func_every_element(iterable[i], func)
        except TypeError:
            iterable[i] = func(iterable[i])
    return iterable

def remove_empty(_list):
    while "" in _list:
        _list.remove("")
    while None in _list:
        _list.remove(None)
    while [] in _list:
        _list.remove([])
    return _list

def lines_separated_by_blank(lines=None):
    if lines is None:
        lines = readlines()
    groups = [[]]
    for line in lines:
        if line == "\n":
            groups.append([])
        else:
            groups[-1].append(line)
    func_every_element(lines, lambda x: x.strip('\n'))
    return groups

def single_split(char, lines=None):
    if lines is None:
        lines = readlines()
    func_every_element(lines, lambda x: x.strip('\n'))
    func_every_element(lines, lambda x: x.split(char))
    return lines

def double_split(char1, char2, lines=None):
    if lines is None:
        lines = readlines()
    func_every_element(lines, lambda x: x.strip('\n'))
    func_every_element(lines, lambda x: x.split(char1))
    func_every_element(lines, lambda x: x.split(char2))
    return lines

def multi_split(chars, lines=None):
    if lines is None:
        lines = readlines()
    func_every_element(lines, lambda x: x.strip('\n'))
    for char in chars:
        func_every_element(lines, lambda x: x.split(char))
    return lines

def multi_strip(chars, lines=None, replace=""):
    if lines is None:
        lines = readlines()
    for char in chars:
        func_every_element(lines, lambda x: x.replace(char, replace))
    return lines

class Vector2:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"({self.x}, {self.y})"

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    def __eq__(self, __value: object) -> bool:
        if isinstance(__value, Vector2):
            return self.x == __value.x and self.y == __value.y
        return False

    def __add__(self, __value: object):
        if isinstance(__value, Vector2):
            return Vector2(self.x + __value.x, self.y + __value.y)
        if isinstance(__value, int):
            return Vector2(self.x + __value, self.y + __value)
        raise TypeError(f"unsupported operand type(s) for +=: '{self.__class__.__name__}' and '{__value.__class__.__name__}'")

    def __hash__(self) -> int:
        return hash((self.x, self.y))

    def __copy__(self):
        return Vector2(self.x, self.y)
    
    def __iter__(self):
        yield self.x
        yield self.y

direction_dict = {"left": Vector2(-1, 0), "right": Vector2(1, 0), "up": Vector2(0, -1), "down": Vector2(0, 1)}
direction_translation_dict = {"left": "l", "l": "left",
                              "right": "r", "r": "right",
                              "up": "u", "u": "up",
                              "down": "d", "d": "down"}

def hex_to_dec(hex):
    if hex[0] == "#":
        hex = hex[1:]
    return int(hex, 16)