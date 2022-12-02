base = r'C:\Users\raj\OneDrive\Coding\Python\aoc_2022/'
f = open(base + r'02_input.txt')
data = [x.strip() for x in f.readlines()]

# Part 1
pairs1 = {'AX':4, 'AY':8, 'AZ':3, 
         'BX':1, 'BY':5, 'BZ':9, 
         'CX':7, 'CY':2, 'CZ':6}

score = 0
for d in data:
    
    p = ''.join(d.split(' '))
    score += pairs1[p]
    
print('Round 1 Score:', score)

# Part 2
pairs2 = {'AX':3, 'AY':4, 'AZ':8, 
         'BX':1, 'BY':5, 'BZ':9, 
         'CX':2, 'CY':6, 'CZ':7}

score = 0
for d in data:
    
    p = ''.join(d.split(' '))
    score += pairs2[p]
    
print('Round 2 Score:', score)