#!/usr/bin/python

"""
    As the guys know each other very well, it didn’t take much 
    time for them to determine, how good is every person in 
    every role. Now, they have a 3 × 3 table, where the ﬁrst 
    row is for Andrew, the second row is for Peter, and the 
    third one is for Paul. The columns correspond to the roles:
    ﬁrst to a “coder”, second to a “mathematician”, third to a
    “tester”. As an example, the number in the third column of
    the second row shows how good is Peter as a “tester”. 

    How the guys want to distribute the roles in such a way 
    that the team performs in a most eﬃcient way. Of course,
    every person can take exactly one role, and every role 
    should be occupied by exactly one person. The eﬃciency of 
    the assignment where Andrew performs with the eﬃciency of 
    A, Peter performs with the eﬃciency of B and Paul with C,
    is equal to sqrt(A^2 + B^2 + C^2). 
"""
import math
from sets import Set

with open('team.in', 'r') as input:
    coder = [int(x) for x in input.readline().split(' ')]
    mathemathematics = [int(x) for x in input.readline().split(' ')]
    tester = [int(x) for x in input.readline().split(' ')]

perform = []

# Iterate over the abilities
cases = Set([0, 1, 2])

for i in cases:
    for j in cases - Set([i]):
        for k in cases - Set([i, j]):
            perform.append(math.sqrt(coder[i]**2 + mathemathematics[j]**2 + tester[k]**2))

with open('team.out', 'w') as output:
    output.write(str(max(perform)))
    output.write('\n')





