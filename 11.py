base = r'C:\Users\raj\OneDrive\Coding\Python\aoc_2022/'
f = open(base + r'11_input.txt')
data = f.read().split('\n\n')[:-1]

f = open(base + r'11_unittest.txt')
data = f.read().split('\n\n')[:-1]

import numpy as np

class Monkey:
    
    def __init__(self, items, divisor, true, false, descriptor):
        
        self.items = items
        self.divisor = divisor
        self.monkey_t = true
        self.monkey_f = false
        self.descriptor = descriptor
        self.handles = 0
       
        return
    
    def test_monkey(self, div=True):
        
        oper = self.descriptor[2].split('= ')[-1].split(' ')
        
        item = self.items[0]
        del self.items[0]
        
        if oper[2] == 'old':
            rhs = item
        else:
            rhs = int(oper[2])
            
        if oper[1] == '*':
            func = lambda y: y * rhs
        else:
            func = lambda y: y + rhs
        
        if div:
            worry = int(np.floor(func(item) / 3))
        else:
            worry = int(func(item))
            
        self.handles += 1
        
        if worry % self.divisor == 0:
            return worry, self.monkey_t
        
        return worry, self.monkey_f
    
    # def test_monkey(self, div=True):
    
    #     oper = self.descriptor[2].split('= ')[-1].split(' ')
        
    #     item = self.items[0]
    #     del self.items[0]
        
    #     if oper[2] == 'old':
    #         if item % self.divisor == 0:
    #             return self.divisor, self.monkey_t
    #         else:
    #             rhs = item
    #     else:
    #         rhs = int(oper[2])
            
    #     if oper[1] == '*':
    #         func = lambda y: y * rhs
    #     else:
    #         func = lambda y: y + rhs
        
    #     if div:
    #         worry = int(np.floor(func(item) / 3))
    #     else:
    #         worry = int(func(item))
            
    #     self.handles += 1
        
    #     if worry % self.divisor == 0:
    #         return worry//self.divisor, self.monkey_t
    #         # return np.gcd(worry, self.divisor), self.monkey_t
        
    #     return worry, self.monkey_f

def create_monkey(num, descriptor):
    
    d = descriptor
    
    items = d[1].split(':')[-1].strip()
    items = [int(x.strip()) for x in items.split(',')]
    
    divisor = int(d[3].split(' ')[-1])
   
    monkey_t = int(d[4].split(' ')[-1])
    monkey_f = int(d[5].split(' ')[-1])
    
    
    m = Monkey(items, divisor, monkey_t, monkey_f, d)
        
    return m

# First pass, create the monkeys
def create_monkeys(data):
    monkeys = {}
    for d in data:
        
        descriptor = d.split('\n')
        num = int(descriptor[0].split(' ')[-1].split(':')[0])
        
        monkeys[num] = create_monkey(num, descriptor)
        
    return monkeys

# Test the monkeys
def run_monkeys(monkeys, rounds, div=True):
    for _ in range(rounds):
        for n in range(len(data)):
            m = monkeys[n]
            _list = np.copy(m.items)
            for i in _list:
                witem, target = m.test_monkey(div)
                monkeys[target].items.append(witem)

    return monkeys

rounds = 20

monkeys = create_monkeys(data)
monkeys = run_monkeys(monkeys, rounds, True)

business = [monkeys[m].handles for m in range(len(data))]
business.sort(reverse=True)

print('Part 1:', business[0]*business[1])

# Part 2
# No /3, and 10000 rounds
# The problem is the values quickly explode....definitely a prime number thing
rounds = 20

# monkeys = create_monkeys(data)
# monkeys = run_monkeys(monkeys, rounds, False)

# business = [monkeys[m].handles for m in range(len(data))]
# business.sort(reverse=True)

# print('Part 2:', business[0]*business[1])