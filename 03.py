base = r'C:\Users\raj\OneDrive\Coding\Python\aoc_2022/'
f = open(base + r'03_input.txt')
data = [x.strip() for x in f.readlines()]

# Part 1

#Learned that 'ord' exists! returns ascii code for a character
def letsum(letter):
    if letter == letter.upper():
        return ord(letter) - 65 + 27 # the ASCII code for 'A', +27 because of the directions
    return ord(letter) - 96 # the ASCII code for 'a', + 1

sumletters = 0
for d in data:
    
    ln = len(d)//2
    lt = list(d[:ln])
    rt = list(d[ln:])

    overlap = set(lt).intersection(rt)   
    letter = list(overlap)[0]
    sumletters += letsum(letter)

print('Sum for Round 1:', sumletters)
            
# Part 2
import numpy as np

sumletters = 0

dataspl = np.split(np.array(data), len(data)//3)

for d in dataspl:
    
    overlap = set(d[0]).intersection(d[1], d[2])
    letter = list(overlap)[0]
    sumletters += letsum(letter)
    
print('Sum for Round 2:', sumletters)