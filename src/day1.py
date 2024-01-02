from utils import *
import re
import itertools
import numpy as np

answer = 0

DIGITS = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}

data = readlines()
#data = ["two1nine", "eightwothree", "abcone2threexyz", "xtwone3four", "4nineeightseven2", "zoneight234", "7pqrstsixteen"]
for line in data:
    print(line)
    for d in range(1, 10):
        if DIGITS[d] in line:
            old = DIGITS[d]
            index = len(old)//2
            new = old[:index] + str(d) + old[index:]
            line = line.replace(old, new)
    print(line)
    _digits = re.findall(r"([^\W\D*])", line)
    _digits = list("".join(_digits))
    print(_digits)
    answer += int(_digits[0]+_digits[-1])
    print(int(_digits[0]+_digits[-1]))
    print()

print(answer)
#upload(answer)