# -*- coding: utf-8 -*-
"""
Created on Fri Nov 02 19:05:57 2012

@author: n3wp0llut10n
"""

res = 0
max_len = 0
for i in range(1, 10**6):
    len_counter = 0
    n = i
    while(n != 1):
        if(n % 2 == 0):
            n = n/2
        else:
            n = 3*n+1
        len_counter += 1
    if(len_counter > max_len):
        max_len = len_counter
        res = i
        
print(res)
print(max_len)
