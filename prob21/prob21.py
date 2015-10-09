#!/usr/bin/python3

import sys
sys.path.append("..")

import euler.mymath

for i in range(1, 10000):
    all_amicables = []
    a = i
    b = sum(euler.mymath.proper_divisors(a))
    
        all_amicables.append((a, b))
    
total = 0
for amicable in all_amicables:
    total += amicable[0] + amicable[1]

print(total)
