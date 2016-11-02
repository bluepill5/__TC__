#!/usr/bin/python

"""

"""
import math

with open('02-team.in', 'r') as input:
    coder = [int(x) for x in input.readline().split(' ')]
    mathemathematics = [int(x) for x in input.readline().split(' ')]
    tester = [int(x) for x in input.readline().split(' ')]

perform = []

for i in range(3):
	perform.append(math.sqrt(coder[i]**2 + mathemathematics[i]**2 + tester[i]**2))

with open('02-team.out', 'w') as output:
    output.write(str(max(perform)))
    output.write('\n')







