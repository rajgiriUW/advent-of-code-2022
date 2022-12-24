base = r'C:\Users\raj\OneDrive\Coding\Python\aoc_2022/' 
f = open(base + r'15_input.txt')
data = f.read().split('\n')[:-1]

line = 2000000 # Part1
rmax = 4000000 # Part 2
cmax = 4000000

# f = open(base + r'15_unittest.txt')
# data = f.read().split('\n')[:-1]
# line = 10
# rmax = 20
# cmax = 20

import numpy as np
from numpy.linalg import norm

coords = []
beacons = []
dists = []
edges = [0, 0, 0, 0] #row top, row bot, col left, col right
for d in data:
    
    coord = d.split('=')
    c = int(coord[1].split(',')[0])
    r = int(coord[2].split(':')[0])
    coords.append((r, c))

    beacon_c = int(coord[-2].split(',')[0])
    beacon_r = int(coord[-1].split(',')[0])
    beacons.append((beacon_r, beacon_c))
    
    dist = norm(np.array((r,c)) - np.array((beacon_r, beacon_c)), 1)
    dists.append(dist)
    
    _coords = np.array(coords)
    _beacons = np.array(beacons)
    
    # find the ends of the grid
    _d = max(dists)
    edges[0] = np.min(_coords[:,0] - _d)
    edges[1] = np.max(_coords[:,0] + _d)
    edges[2] = np.min(_coords[:,1] - _d)
    edges[3] = np.max(_coords[:,1] + _d)

# Part 1

grid = [edges[1] - edges[0], edges[3] - edges[2]]
row = np.arange(edges[2], edges[3], 1)
nobeacon = np.zeros(len(row))
for coord, dist in zip(coords, dists):
    
    coord = np.array(coord)
    dist = np.array(dist)
    
    # L1 norm, find missing column coordinate that would be dist units away
    lt = int(-(dist - np.abs(coord[0] - line)) + coord[1])
    rt = int(dist - np.abs(coord[0] - line) + coord[1])
    
    lt = np.where(row==lt)[0][0]
    rt = np.where(row==rt)[0][0]
    nobeacon[lt:rt] = 1
    
print('Part 1:', len(np.where(nobeacon==1)[0]))

# Part 2


