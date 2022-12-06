base = r'C:\Users\raj\OneDrive\Coding\Python\aoc_2022/'
f = open(base + r'06_input.txt')
data = f.read().split('\n')[0]

# Post-mortem:
# Didn't really learn anything new in this puzzle. I could do this with set, maybe?
# Zipping an iterable might work, according to Reddit


# Part 1 
# Find 4 consecutive unique chars

import numpy as np

def find_marker(code, length):

    for n in range(len(code) - length + 1):
        
        if len(np.unique(list(data[n:n+length]))) == length:
        
                return n+length
            
print('Part 1:', find_marker(data, 4))

# Part 2
# Find 14 consecutive unique chars

print('Part 2:', find_marker(data, 14))
