#!/usr/bin/python

"""

"""
import math
from sets import Set

with open('02-team.in', 'r') as input:
    coder = [int(x) for x in input.readline().split(' ')]
    mathemathematics = [int(x) for x in input.readline().split(' ')]
    tester = [int(x) for x in input.readline().split(' ')]

perform = []

for i in cases:
    for j in cases - Set([i]):
        for k in cases - Set([i, j]):
            perform.append(math.sqrt(coder[i]**2 + mathemathematics[j]**2 + tester[k]**2))

with open('02-team.out', 'w') as output:
    output.write(str(max(perform)))
    output.write('\n')
