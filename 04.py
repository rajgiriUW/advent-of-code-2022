base = r'C:\Users\raj\OneDrive\Coding\Python\aoc_2022/'
f = open(base + r'04_input.txt')
data = [x.strip() for x in f.readlines()]

# Part 1
import numpy as np

overlaps = 0 
for d in data:
    
    elves = d.split(',')
    elf1 = elves[0]
    elf2 = elves[1]
    
    # Find the range on the left
    _lg = elf1.split('-')
    elf1 = np.arange(int(_lg[0]), int(_lg[1])+1)
    
    _rg = elf2.split('-')
    elf2 = np.arange(int(_rg[0]), int(_rg[1])+1)
    
    if len(set(elf1).intersection(elf2)) >= len(elf1):
        overlaps += 1
    elif len(set(elf1).intersection(elf2)) >= len(elf2):
        overlaps +=1

print('Part 1:', overlaps)

#Part 2
overlaps = 0 
for d in data:
    
    elves = d.split(',')
    elf1 = elves[0]
    elf2 = elves[1]
    
    # Find the range on the left
    _lg = elf1.split('-')
    elf1 = np.arange(int(_lg[0]), int(_lg[1])+1)
    
    _rg = elf2.split('-')
    elf2 = np.arange(int(_rg[0]), int(_rg[1])+1)
    
    if len(set(elf1).intersection(elf2)) > 0:
        overlaps += 1

print('Part 2:', overlaps)