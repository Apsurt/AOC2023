from typing import Any
from utils import *
import itertools
import numpy as np
from operator import gt, lt
import re

class Part:
    def __init__(self, x, m, a, s) -> None:
        self.x = x
        self.m = m
        self.a = a
        self.s = s
        self.dict = {"x": x, "m": m, "a": a, "s": s}
    
    def __str__(self) -> str:
        return self.dict.__repr__()
    
    def __repr__(self) -> str:
        return f"Part({self.x}, {self.m}, {self.a}, {self.s})"
    
    def sum(self):
        _sum = 0
        for v in self.dict.values():
            _sum += v
        return _sum

class Rule:
    def __init__(self, category, operator, value, outcome) -> None:
        self.category = category
        self.operator = operator
        self.value = value
        self.outcome = outcome
    
    def __call__(self, part) -> Any:
        if self.category:
            return self.operator(part.dict[self.category], self.value)
        else:
            return True
    
    def __repr__(self) -> str:
        if self.category:
            return category + (">" if self.operator == gt else "<") + str(value) + ":" + self.outcome
        else:
            return self.outcome

class Workflow:
    def __init__(self, name) -> None:
        self.name = name
        self.rules = []
    
    def add_rule(self, rule):
        self.rules.append(rule)
    
    def __call__(self, part) -> Any:
        for rule in self.rules:
            if rule(part):
                return rule.outcome
        raise RuntimeError("All rules false")
    
    def __eq__(self, __value: object) -> bool:
        return self.name == __value
    
    def __repr__(self) -> str:
        return self.name
    
    def __str__(self) -> str:
        res = "Workflow("
        res += ", ".join([self.name]+[rule.__repr__() for rule in self.rules])
        res += ")"
        return res

data = lines_separated_by_blank(readlines())

workflows = []
for wf_str in data[0]:
    wf_str = wf_str.strip().strip("}")
    name, wf_str = wf_str.split("{")
    workflow_object = Workflow(name)
    
    rules_str = wf_str.split(",")
    for rule in rules_str:
        if ":" in rule:
            rule, outcome = rule.split(":")
            if ">" in rule:
                operator = gt
                category, value = rule.split(">")
            elif "<" in rule:
                operator = lt
                category, value = rule.split("<")
            else:
                raise ValueError(rule)
            rule = Rule(category, operator, int(value), outcome)
        else:
            rule = Rule(None, None, None, rule)
        workflow_object.add_rule(rule)
    workflows.append(workflow_object)

answer = 0
n = 0
all_x = np.arange(1,4001,1)
outcome_list = [0]*len(all_x)

while n<len(all_x):
    part = Part(all_x[n], 4000, 1, 1)
    current_workflow = workflows[workflows.index("in")]
    outcome = None
    while not outcome in ["A", "R"]:
        outcome = current_workflow(part)
        if not outcome in ["A", "R"]:
            try:
                current_workflow = workflows[workflows.index(outcome)]
            except ValueError:
                outcome = "R"
    if outcome == "A":
        outcome_list[n] = 1
    print(part, outcome)
    n += 1
from matplotlib import pyplot as plt

plt.scatter(all_x,outcome_list)
plt.show()
#upload(answer)