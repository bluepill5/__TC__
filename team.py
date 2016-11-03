#!/usr/bin/python
"""
    Optimize to sqrt(A^2 + B^2 + C^2) where A, B, C, are the rows.
"""
import math

def ls_del (ls, idxs):
    t_ls = ls[:]
    t_ls = [i for j, i in enumerate(t_ls) if j not in idxs]
    return t_ls


with open('team.in', 'r') as input:
    coder = [int(x) for x in input.readline().split(' ')]
    mathemathematics = [int(x) for x in input.readline().split(' ')]
    tester = [int(x) for x in input.readline().split(' ')]

perform = []

# Iterate over the abilities
cases = [0, 1, 2]

for i in cases:
    for j in ls_del(cases, [i]):
        for k in ls_del(cases, [i, j]):
            perform.append(math.sqrt(coder[i]**2 + mathemathematics[j]**2 + tester[k]**2))

with open('team.out', 'w') as output:
    output.write(str(max(perform)))
    output.write('\n')
