# -*- coding: utf-8 -*-

"""
Created on Thu Nov 01 18:55:41 2012

@author: n3wp0llut10n
"""
import functools

f = open('data.txt')

string_list = []
for line in f:
    string_list.append(line)

f.close()

num_list = [(i.replace('\n', '')) for i in string_list]

for i in range(0, len(num_list)):
    num_list[i] = int(num_list[i])

total = 0
for i in reversed(num_list):
   total += i

total_str = str(total)

for i in range(0, 10):
    print(total_str[i])
