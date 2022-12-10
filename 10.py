base = r'C:\Users\raj\OneDrive\Coding\Python\aoc_2022/'
f = open(base + r'10_input.txt')
data = f.read().split('\n')[:-1]


# Post-Mortem: Just reused deques, this one was fun but pretty easy

# Unittest
# f = open(base + r'10_unittest.txt')
# data = f.read().split('\n')[:-1]

# Simple unittest
# data = ['noop', 'addx 3', 'addx -5']

signals = [20, 60, 100, 140, 180, 220]

X = 1

from collections import deque
import numpy as np

ops = deque([0]) 
strengths = [0] #cycles in problem are 1-indexed

n = 0
while ops:
    
    if n < len(data):
        d = data[n]
    
        ops.append(0) # always does nothing in first cycle
        if 'addx' in d:
            
            val = int(d.split(' ')[-1])
            ops.append(val)
            
    X += ops.popleft() # a queue
    strengths.append(X)
    
    n += 1

print('Part 1:', sum([strengths[n]*n for n in signals]))

# Part 2

# Dimensions of the screen
cmax = 40
rmax = 6
X = 1

img = np.zeros((6, 40)).astype(int)
ops = deque([0]) 

n = 0
while ops and n < cmax*rmax:
    
    if n < len(data):
        d = data[n]
    
        ops.append(0) # always does nothing in first cycle
        if 'addx' in d:
            
            val = int(d.split(' ')[-1])
            ops.append(val)
            
    X += ops.popleft() # a queue
    
    pixel = np.unravel_index(n, (rmax, cmax))
    if pixel[1] in [X-1, X, X+1]: 
        img[pixel] = 1
    
    n += 1

import matplotlib.pyplot as plt
plt.imshow(img, cmap='inferno')