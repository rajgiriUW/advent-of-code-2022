base = r'C:\Users\raj\OneDrive\Coding\Python\aoc_2022/'
f = open(base + r'05_input.txt')
data = f.read().split('\n\n')

crates = data[0].split('\n')
moves = data[1].split('\n')[:-1]

# Learned today: 1) remember deques are great 2) regex, forgot how to search for numbers

# Part 1
from collections import deque
import re

# # Create initial deques for each crate 1 to 9
cratedeq = {}
for n in range(1, 10):
    cratedeq[n] = deque()
for c in crates:
    letters = [c[x:x+4] for x in range(0, len(c)+1, 4)] #splits into substrings
    for n, l in enumerate(letters, 1):
        if '[' in l:
            cratedeq[n].appendleft(l[1])
        
# Perform moves
for m in moves:
    
    num, src, dst = [int(x) for x in re.findall('\d+', m)]
    for n in range(num):
        cratedeq[dst].append(cratedeq[src].pop())

print('Part 1:', ''.join([cratedeq[x][-1] for x in range(1,10)]))


#Part 2

# Our deques for each crate 1 to 9
cratedeq = {}
for n in range(1, 10):
    cratedeq[n] = deque()
for c in crates:
    letters = [c[x:x+4] for x in range(0, len(c)+1, 4)] #splits into substrings
    for n, l in enumerate(letters, 1):
        if '[' in l:
            cratedeq[n].appendleft(l[1])
            
# Perform moves
for m in moves:
    
    num, src, dst = [int(x) for x in re.findall('\d+', m)]
    
    # Create temporary deque to pop from in reverse order
    _deq = deque()
    for n in range(num):
        _deq.append(cratedeq[src].pop())
    for n in range(num):
        cratedeq[dst].append(_deq.pop())

print('Part 2:', ''.join([cratedeq[x][-1] for x in range(1,10)]))