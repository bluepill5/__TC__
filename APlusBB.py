#!/usr/bin/python

"""
    Program that return the sum of two numbers 
"""

with open('aplusbb.in', 'r') as input:
    a, b = [int(x) for x in input.readline().split(' ')]
with open('aplusbb.out', 'w') as output:
    output.write(str(a + b**2))
    output.write('\n')






