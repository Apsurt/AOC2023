from utils import *
import itertools
import numpy as np

class Bag:
    def __init__(self, bag_id):
        self.id = bag_id
        self.r = 0
        self.g = 0
        self.b = 0
    
    def update(self, r=0, g=0, b=0):
        self.r = max(self.r, r)
        self.g = max(self.g, g)
        self.b = max(self.b, b)


data = readlines()
data = func_every_element(data, lambda x: x.split(': ')[1])
bags = func_every_element(data, lambda x: x.split('; '))

bag_objects = []

for bag_id in range(len(bags)):
    bag_objects.append(Bag(bag_id))
    for set_id in range(len(bags[bag_id])):
        string = bags[bag_id][set_id]
        string = string.replace('red', 'r')
        string = string.replace('green', 'g')
        string = string.replace('blue', 'b')
        string = string.replace(' ', '')
        string = string.replace('\n', '')
        string = string.split(',')
        for i in string:
            print(bag_objects[bag_id].id)
            print(i)
            if i == '':
                continue
            if i[-1] == 'r':
                bag_objects[bag_id].update(r = int(i[:-1]))
            elif i[-1] == 'g':
                bag_objects[bag_id].update(g = int(i[:-1]))
            elif i[-1] == 'b':
                bag_objects[bag_id].update(b = int(i[:-1]))
            print(bag_objects[bag_id].r, bag_objects[bag_id].g, bag_objects[bag_id].b)
            print()

answer1 = 0
answer2 = 0

for bag in bag_objects:
    answer1 += (bag.id+1)
    if bag.r > 12 or bag.g > 13 or bag.b > 14:
        answer1 -= (bag.id+1)
    answer2 += bag.r*bag.g*bag.b

print(answer1)
print(answer2)

#upload(answer)