#!/usr/bin/python

"""
    After reading some books on competitive programming, 
    Jamie understood that there are two ways to improve his skills: 
    studying theory and practicing a lot. There are n days before the 
    next programming competition. Based on his biorhythm calendar, 
    Jamie determined two numbers for each of these days: ti is how much
     his ability to solve problems will improve if he studies theory at 
     the i-th day, and pi is how much it will improve if he practices a 
     lot at the i-th day. Every day should be entirely dedicated to either
     ory or practice. Additionally, at least one of these days should be 
     theoretical, and at least one should be practical. 
"""

with open('prepare.in', 'r') as input:
    ds = [int(x) for x in input.readline().split(' ')]
    ts = [int(x) for x in input.readline().split(' ')]
    ps = [int(x) for x in input.readline().split(' ')]

max_ts = max(ts)
i_ts = 0
count_ts = 0
max_ps = max(ps)
i_ps = 0
count_ps = 0

max_train = 0

for i in range(ds[0]):
	if ts[i] >= ps[i]:
		max_train += ts[i]
		count_ts += 1
	else:
		max_train += ps[i]
		count_ps +=1
	if ts[i] == max_ts:
		i_ts = i
	if ps[i] == max_ps:
		i_ps = i

if count_ts == 0:
	max_train = max_train - ps[i_ts] + ts[i_ts]
if count_ps == 0:
	max_train = max_train - ts[i_ps] + ps[i_ps]

# maxPreparation = map(lambda x: max(x), zip(ts, ps))

with open('prepare.out', 'w') as output:
    output.write(str(max_train))
    output.write('\n')






