base = r'C:\Users\raj\OneDrive\Coding\Python\aoc_2022/'
f = open(base + r'02_input.txt')
data = [x.strip() for x in f.readlines()]

# Part 1
pairs1 = {'A X':4, 'A Y':8, 'A Z':3, 
         'B X':1, 'B Y':5, 'B Z':9, 
         'C X':7, 'C Y':2, 'C Z':6}

score = sum([pairs1[x] for x in data])
    
print('Round 1 Score:', score)

# Part 2
pairs2 = {'A X':3, 'A Y':4, 'A Z':8, 
         'B X':1, 'B Y':5, 'B Z':9, 
         'C X':2, 'C Y':6, 'C Z':7}

score = sum([pairs2[x] for x in data])
    
print('Round 2 Score:', score)