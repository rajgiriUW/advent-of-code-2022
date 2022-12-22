base = r'C:\Users\raj\OneDrive\Coding\Python\aoc_2022/' 
f = open(base + r'14_input.txt')
data = f.read().split('\n')[:-1]


# Post-mortem: Didn't really learn anything new. Use np.where reasonably
# Used linspace since that does check for negative ranges, unlike arange, but 
# the code was a little clunky

# f = open(base + r'14_unittest.txt')
# data = f.read().split('\n')[:-1]

import numpy as np
import matplotlib.pyplot as plt

# 0 = empty, 1 = wall, -1 = sand

def makecave(data, floor=0):
    cave = np.zeros((1000, 1000)) #just pick some default size first
    for d in data:
        
        line = d.split(' ')
        ends = []
        for ln in line:
            _coord = ln.split(',')
            if len(_coord) == 2: #is a coordinate
               coords = [int(x) for x in _coord]
               coords.reverse()
               ends.append(coords)
        for n, _ in enumerate(ends[:-1]):
            
            lt = np.linspace(ends[n][0], ends[n+1][0], np.abs(ends[n+1][0] - ends[n][0]) + 1).astype(int)
            rt = np.linspace(ends[n][1], ends[n+1][1], np.abs(ends[n+1][1] - ends[n][1]) + 1).astype(int)
            
            if len(lt) < len(rt): #along columns
                for r in rt:
                    cave[lt, r] = 1
            else:
                for l in lt:
                    cave[l, rt] = 1

    if floor > 0:
        r, _ = np.where(cave == 1)
        cave[r[-1]+2,:] = 1
        
    r, _ = np.where(cave == 1)
    cave = cave[:r[-1]+1, :]
        
    return cave

def nextmove(cave, pos):
    '''
    Returns new position, whether it has moved, and whether it is off the map
    '''
    r, c = pos
    
    if r+1 >= cave.shape[0] or c+1 >= cave.shape[1] or c-1 < 0:
        return (r, c), False, True
    
    if cave[r+1, c] == 0:
        return (r+1, c), True, False
    elif cave[r+1, c-1] == 0:
        return (r+1, c-1), True, False
    elif cave[r+1, c+1] == 0:
        return (r+1, c+1), True, False
    else:
        return (r, c), False, False

# Part 1
cave = makecave(data)
start = (0, 500)
fallen = False
n = 0
while not fallen:
    
    pos = (0, 500)
    moved = True
    
    while moved and not fallen:
        nextpos, moved, fallen = nextmove(cave, pos)
        pos = nextpos
        
    if not fallen:
        cave[pos] = -1
        n +=1

print('Part 1:', n)  

_, c = np.where(cave == 1)
plt.figure()
plt.imshow(cave[:, min(c):max(c)], cmap='inferno')

# Part2
cave = makecave(data, floor=2)

stopped = False
n = 0
while not stopped:
    
    pos = (0, 500)
    moved = True
    
    while moved:
        nextpos, moved, _ = nextmove(cave, pos)
        pos = nextpos
        
    if pos != start:
        cave[pos] = -1
        n +=1
    else:
        n += 1 # for the last grain of sand
        stopped = True

print('Part 2:', n)  

_, c = np.where(cave == -1)

plt.figure()
plt.imshow(cave[:, min(c):max(c)], cmap='inferno')
