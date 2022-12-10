base = r'C:\Users\raj\OneDrive\Coding\Python\aoc_2022/'
f = open(base + r'09_input.txt')
data = f.read().split('\n')[:-1]

# Unittest
# f = open(base + r'09_unittest2.txt')
# data = f.read().split('\n')[:-1]

# Post-Mortem: Should have used sets to aggregate the coordinates, that automatically
# saves as unique values, rather than tedious coordinates

import numpy as np

def move_ht(command, snake, visited, numsegments=9):
    
    direction, steps = command.split(' ')
    steps = int(steps)
    
    moves = {'R': [1, 0], 'L': [-1, 0], 'U': [0, 1], 'D': [0, -1]}
        
    for _ in range(1, steps+1):

        snake[0][0] = snake[0][0] + moves[direction][0]
        snake[0][1] = snake[0][1] + moves[direction][1]
        
        for n in range(1, numsegments+1):
            if move_tail(snake[n-1], snake[n]):
                snake[n][0], snake[n][1] = diagonal(direction, snake[n-1], snake[n])

                if n == numsegments:
                    visited[0].append(snake[n][0])
                    visited[1].append(snake[n][1])
                    
    return snake, visited

def move_tail(head, tail):
    
    if np.abs(head[0] - tail[0]) <= 1 and np.abs(head[1] - tail[1]) <= 1:
        return False
    
    return True

def diagonal(direction, head, tail):
    
    if not np.allclose(head, tail):
        
        x = head[0]
        y = head[1]
        
        if head[1] - tail[1] == 2:
            y = head[1] - 1
        if head[1] - tail[1] == -2:
            y = head[1] + 1
        if head[0] - tail[0] == 2:
            x = head[0] - 1
        if head[0] - tail[0] == -2:
            x = head[0] + 1
        
        return x, y
 
    return tail[0], tail[1]

# Part 1

snake = np.zeros((2, 2))
visited = [[0], [0]]

for d in data:

    snake, visited = move_ht(d, snake, visited, 1)

visited_coords = np.array([visited[0], visited[1]]).astype(int)
_mat = int(max(np.abs(visited[0]).max(), np.abs(visited[1]).max())) # coordinates need to be >= 0 for ravel
visited_index = np.ravel_multi_index(visited_coords+_mat, (2*_mat+1, 2*_mat + 1))

print('Part 1:', len(np.unique(visited_index)))

# Part 2, 9-segment tail
snake = np.zeros((10, 2)) # head is first row
visited = [[0], [0]]

for d in data:

    snake, visited = move_ht(d, snake, visited, 9)
    
visited_coords = np.array([visited[0], visited[1]]).astype(int)
_mat = int(max(np.abs(visited[0]).max(), np.abs(visited[1]).max())) # coordinates need to be >= 0 for ravel
visited_index = np.ravel_multi_index(visited_coords+_mat, (2*_mat+1, 2*_mat + 1))

print('Part 2:', len(np.unique(visited_index)))
