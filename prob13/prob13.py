# -*- coding: utf-8 -*-

"""
Created on Thu Nov 01 18:55:41 2012

@author: n3wp0llut10n
"""

f = open('data.txt')

string_list = []

for line in f:
    string_list.append(line)

f.close()

num_list = [list(i.replace('\n', '')) for i in string_list]

num_list = [map(int, num_list[i]) for i in range(0, len(num_list))]

"""
the immediately preceding comprehension is equivalent to this loop
which one is more readable?
for i in range(0, len(num_list)):
    for j in range(0, len(num_list[i])):
        num_list[i][j] = int(num_list[i][j])
"""

num_list_tr = map(list, zip(*num_list))

temp = 0
temp_str = ""
stack = []
for j in reversed(num_list_tr):
    temp = temp + sum(j)
    temp_str = str(temp)
    stack.append(int(temp_str[-1]))
    temp = int(temp_str[:-1])

temp_str = temp_str[:-1]
for i in range(0, len(temp_str)) :
    stack.append( int( temp_str[len(temp_str) - 1 - i] ) )
    
print stack
new_str = ""
for i in range(0, 10):
    new_str += str(stack.pop())
    
print new_str

