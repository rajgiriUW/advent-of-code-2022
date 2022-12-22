base = r'C:\Users\raj\OneDrive\Coding\Python\aoc_2022/' 
f = open(base + r'12_input.txt')
data = f.read().split('\n')[:-1]

# Post-mortem: BFS does a shortest path on a grid! Interesting
# Unfortunately was doing a DFS at first but had to search for help
# Otherwise the actual code usage wasn't different. Re-remembered argsort
# In hindsight I would go through and figure out how to do Dijkstra's algorithm
# I don't know other shortest path algorithms but presumably that suffices here

# f = open(base + r'12_unittest.txt')
# data = f.read().split('\n')[:-1]

import numpy as np
from numpy.linalg import norm
from collections import deque

# Create the height map
# S = -1 (start), E = 100 (end)
# others created via ASCII code
# ord('letter') - 97 = code --> 1 to 26
# ord('S') is 83 --> -14, ord('E') is 69 --> -28 

heights = np.zeros((len(data), len(data[0])))

for n, d in enumerate(data):
    heights[n, :] = [ord(x)-96 for x in d]
heights[np.where(heights == -13)] = 0
heights[np.where(heights == -27)] = 27
heights = np.pad(heights, 1, mode='constant', constant_values=99)

start = tuple([int(x) for x in list(np.where(heights== 0))])
stop = tuple([int(x) for x in list(np.where(heights == 27))])

pos = start

'''
Method: 
    Can create tree where each node sees the four neighbors
    Valid paths are those of difference 1
    
    Then traverse the tree from start to end?

'''

class node:
    def __init__(self, heights, pos):
        
        self.pos = pos
        self.moves = []
        
        for s in [(pos[0]-1, pos[1]), (pos[0]+1, pos[1]), (pos[0], pos[1]-1), (pos[0], pos[1]+1)]:
            if heights[pos] - heights[s] >= -1:
                self.moves.append(s)
            
def normgrid(lt, rt):
    # 1d norm on tuples
    return norm(np.array(lt) - np.array(rt), 1)

def bfs(heights, start, stop):
    
    currentnode = node(heights, start)
    path = deque([currentnode])
    
    pathtaken = [start]
    found = False
    while path:
    
        currentnode = path.popleft()
        
        if currentnode.pos == stop:
            found = True
            break
        
        for p in currentnode.moves:
            _node = node(heights, p)
            if p not in pathtaken:
                path.append(_node)
                pathtaken.append(p)

    # Delete the nonconsecutive ones
    if any(pathtaken) and stop in pathtaken:
        _pathtaken = [stop]
        pathtaken = pathtaken[:pathtaken.index(stop)+1]
        for n, p in enumerate(pathtaken[-2:0:-1], 0):
            if normgrid(p, _pathtaken[-1]) == 1:
                _pathtaken.append(p)
        _pathtaken.reverse()
        
    else:
        _pathtaken = []
        found = False
    
    return _pathtaken, found

path, _ = bfs(heights, start, stop)
visited = np.zeros(heights.shape)
visited[start] = 1
for p in path:
    visited[p] = 1
print('Part 1:', len(path)) 

# Part 2: Stupid slow, I really should just do Dijkstra next time

# All coordinates of value 1
starts = np.where(heights == 1)
distances = []

# Sort by finding the closest level 1, then stopping once that finds a valid path
for r, c in zip(starts[0], starts[1]):
    distances.append(normgrid((r,c), stop))

lt = starts[0][np.argsort(distances)]
rt = starts[1][np.argsort(distances)]
    
mindist = [np.inf, start]
for r, c in zip(lt, rt):
    
    path2, found = bfs(heights, (r, c), stop)
    if found == True and stop in path2:
        mindist[0] = min(len(path2), mindist[0])
        mindist[1] = (r, c)
print('Part 2:', mindist[0], 'location:', mindist[1])
#%%
# Using Wiki for Dijsktra algorithm
# currentnode = node(heights, start, neighbors(heights, start))
# path = deque([currentnode])

# totalsteps = []
# steps = 0
# distances = np.ones(heights.shape) * np.inf

# # minpath = norm(np.array(stop) - np.array(start),1)

# rows, cols = heights.shape
# nodes = []
# nodes1d = []

# for r in range(1, rows-1):
#     for c in range(1, cols-1):
#         nodes1d.append([node(heights, (r, c), neighbors(heights, (r, c)))])

# for r in range(1, rows-1):
#     nodes.append([node(heights, (r, c), neighbors(heights, (r, c))) for c in range(1, cols-1)])

# distances[stop] = 0

# for n in nodes1d:
    
# while path or currentnode.pos == stop:
    
    
#     break

'''
 1  function Dijkstra(Graph, source):
 2      
 3      for each vertex v in Graph.Vertices:
 4          dist[v] ← INFINITY
 5          prev[v] ← UNDEFINED
 6          add v to Q
 7      dist[source] ← 0
 8      
 9      while Q is not empty:
10          u ← vertex in Q with min dist[u]
11          remove u from Q
12          
13          for each neighbor v of u still in Q:
14              alt ← dist[u] + Graph.Edges(u, v)
15              if alt < dist[v]:
16                  dist[v] ← alt
17                  prev[v] ← u
18
19      return dist[], prev[]
'''