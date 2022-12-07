base = r'C:\Users\raj\OneDrive\Coding\Python\aoc_2022/'
f = open(base + r'07_input.txt')
data = f.read().split('\n')[:-1]

# Part 1

# Unit test
# f = open(base + r'07_unittest.txt')
# data = f.read().split('\n')

from collections import deque


class Folder:
    '''
    files : Dict
        Contains all files with associated filesize (int)
    folders : Dict
        Contains all folders, each of class Folder
    name : str
        Name of the current directory
    '''
    
    def __init__(self, name='/', parent=None):
        self.files = {}
        self.folders = {}
        self.name = name
        self.parent = parent
        
        self.size = 0
    
    def val(self):
        return sum(self.files.values())
    
def parse(folder, command = '$ cd /'):
    '''
    Parse the file system command, given object folder of Folder
    Default: return to root
    '''
    cmd = command.split(' ')
    
    if cmd[1] == 'ls':
        return folder #does nothing, we assume all non-$ are ls outputs
    
    if cmd[0] == '$':
        if cmd[1] == 'cd':
            
            if cmd[2] == '..':
                return folder.parent
            elif cmd[2] == '/':
                while (folder.parent):
                    folder = folder.parent
                return folder
            else:
                return folder.folders[cmd[2]]
        
    elif cmd[0] == 'dir':
        folder.folders[cmd[1]] = Folder(name=cmd[1], parent = folder)
        
    else:
        folder.files[cmd[1]] = int(cmd[0]) #e.g. 29116 f

        _folder = folder
        folder.size += int(cmd[0])
        while _folder.parent:
            _folder.parent.size += int(cmd[0])
            _folder = _folder.parent
    
    return folder

# Part 1
cpu = Folder()
for d in data:
    cpu = parse(cpu, d)
cpu = parse(cpu) #return home

# Traverse tree
folders_searched = deque()
folders_searched.append(cpu)

total_vals = 0
while folders_searched:
    current_folder = folders_searched.pop()
    for _, v in current_folder.folders.items():
        folders_searched.append(v)
    if current_folder.size <= 100000:
        total_vals += current_folder.size

print('Part 1:', total_vals)

# Part 2
total = 70000000
target = 30000000

folders_searched = deque()
folders_searched.append(cpu)

usage = 70000000 - cpu.size
min_folder = cpu.size
while folders_searched:
    current_folder = folders_searched.pop()
    for _, v in current_folder.folders.items():
        folders_searched.append(v)
    if usage + current_folder.size >= target:
        min_folder = min(min_folder, current_folder.size)

print('Part 2:', min_folder)