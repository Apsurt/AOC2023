from utils import *
import itertools
import numpy as np

class Scratchcard:
    def __init__(self, id, winning_numbers, your_ticket) -> None:
        self.id = id
        self.winning_numbers = winning_numbers
        self.your_ticket = your_ticket
        self.matching_numbers = 0
    
    def new_scratchcards_ids(self):
        for number in self.your_ticket:
            if number in self.winning_numbers:
                self.matching_numbers += 1
        return list(range(self.id+1, self.id+1+self.matching_numbers))
    
    def copy(self):
        return Scratchcard(self.id, self.winning_numbers.copy(), self.your_ticket.copy())
    
    def __repr__(self) -> str:
        return "Scratchcard(" + str(self.id) +")"
    
    def __str__(self) -> str:
        result = " ".join(map(str, self.winning_numbers)) + " | " + " ".join(map(str, self.your_ticket))
        return result

data = readlines()
data = func_every_element(data, lambda x: x.strip('\n'))
data = func_every_element(data, lambda x: x.split(": ")[1])
data = func_every_element(data, lambda x: multi_split([" | ", " "], [x])[0])

scratchcards = []

for i in range(len(data)):
    new_scratchcard = Scratchcard(i+1, None, None)
    for _type in range(len(data[i])):
        data[i][_type] = list(map(int, filter(lambda x: x != "", data[i][_type])))
        if _type == 0:
            new_scratchcard.winning_numbers = data[i][_type]
        else:
            new_scratchcard.your_ticket = data[i][_type]
    scratchcards.append(new_scratchcard)

answer = 0

pointer = 0
while pointer < len(scratchcards):
    print(pointer)
    scratchcard = scratchcards[pointer]
    new_ids = scratchcard.new_scratchcards_ids()
    for _id in new_ids:
        scratchcards.append(scratchcards[_id-1].copy())
    pointer += 1

answer = len(scratchcards)
print(answer)
#upload(answer)