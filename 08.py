base = r'C:\Users\raj\OneDrive\Coding\Python\aoc_2022/'
f = open(base + r'08_input.txt')
data = f.read().split('\n')[:-1]

# f = open(base + r'08_unittest.txt')
# data = f.read().split('\n')[:-1]

# Post-mortem:
# Nothing really new, just used numpy array. I don't use np.alltrue often, though
# Might have been clever with using gradients or something

import numpy as np

# Read in the tree map as a numpy matrix
trees = np.zeros((len(data), len(data[0])))
for n, d in enumerate(data):
    trees[n,:] = np.array([int(x) for x in d])
trees = np.pad(trees, 1, 'constant', constant_values=-1)
# Part 1
'''
Find for given r, c, if all numbers orthognal to the end are less than or equal
then it is visible
'''
visible = 0 
vis_mat = np.zeros(trees.shape)

for m, r in enumerate(trees[1:-1],1):
    for n, c in enumerate(r[1:-1],1):
        left = np.alltrue(trees[m, :n] < c) 
        right = np.alltrue(trees[m, n+1:] < c)
        up = np.alltrue(trees[:m, n] < c)
        down = np.alltrue(trees[m+1:, n] < c)
        
        if left or right or up or down:
            visible += 1
            vis_mat[m,n] = 1

trees = trees[1:-1, 1:-1]

print('Part 1:', visible)

# Part 2
'''
For each element, find the first in each direction >= element num and count
spaces between. 
'''
vis_mat = np.zeros(trees.shape)

for m, r in enumerate(trees[1:-1],1):
    for n, c in enumerate(r[1:-1],1):
        
        lt = np.where(trees[m, :n][::-1] >= c)[0]
        rt = np.where(trees[m, n+1:] >= c)[0]
        up = np.where(trees[:m, n][::-1] >= c)[0]
        dn = np.where(trees[m+1:, n] >= c)[0]
        
        if lt.size == 0:
            lt = np.array([n-1])
        if rt.size == 0:
            rt = np.array([trees.shape[1] - n -2])
        if up.size == 0:
            up = np.array([m-1])
        if dn.size == 0:
            dn = np.array([trees.shape[0] - m - 2])

        vis_mat[m,n] = (lt[0]+1)*(rt[0]+1)*(up[0]+1)*(dn[0]+1)
        
print('Part 2:', int(np.max(vis_mat)))
