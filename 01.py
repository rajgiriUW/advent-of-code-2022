# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 22:02:11 2022

@author: raj
"""

base = r'C:\Users\raj\OneDrive\Coding\Python\aoc_2022/'
f = open(base + r'01_input.txt')

# Part 1
elves = []
elfsum = 0 
for f in f.readlines():
    if f != '\n':
        elfsum += int(f)
    else:
        elves.append(elfsum)
        elfsum = 0

print('Max elf:', max(elves))

# Part 2: Find top 3
elves.sort()
print('Top 3 sum:', sum(elves[-3:]))

# Alternate to learn: using map function
f = open(base + r'01_input.txt')
data = f.read().split('\n\n')

elves = []
for d in data:
    elves.append(tuple([int(x) for x in d.strip().split('\n')]))

elfsum = list(map(sum, elves))
print(max(elfsum))

elves.sort(key=sum, reverse=True)
elfsum = list(map(sum, elves))
print(sum(elfsum[:3]))