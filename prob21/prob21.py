#!/usr/bin/python3

import sys
sys.path.append("../..")
import euler.mymath

all_amicables = []
for a in range(1, 10000):
    b = sum(euler.mymath.proper_divisors(a))
    if euler.mymath.is_amicable(a, b) == True and (a != b):
        if (b, a) not in all_amicables: 
            all_amicables.append((a, b))
    
total = 0
for amicable in all_amicables:
    total += amicable[0] + amicable[1]
print(total)
