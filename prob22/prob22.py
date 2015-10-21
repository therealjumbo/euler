#!/usr/bin/python3

f = open("p022_names.txt", 'r')
text = f.read()

names_list = text.replace('"', '').split(',')
names_list = [name.lower() for name in names_list]
names_list.sort()

total_value = 0
for position, name in enumerate(names_list):
    alpha_value = 0
    for char in name:
       alpha_value += ord(char) - ord('a') + 1 
    total_value += (position + 1) * alpha_value
    
print(total_value)

f.close()
