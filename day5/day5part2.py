import collections

input_file = open(r"C:\Users\Us\source\repos\Advent Of Code 2022\day5\day5.txt")

sum = 0
line = input_file.readline()
setup_lines : list[str] = list()
num_stacks = len(line) / 4
print(str(num_stacks) + " stacks")
assert(num_stacks % 1 == 0)
num_stacks = int(num_stacks)

stacks_end_line : int = 0
#get the first few lines that have initial position
while line != '\n' and line != '':
    print(line)
    setup_lines.append(line)
    stacks_end_line += 1
    
    line = input_file.readline()
setup_lines.reverse()
setup_lines.pop(0) # remove line with stack numbers

stacks : list[list[str]] = list()
for i in range(0, num_stacks):
    stacks.append([])
#stacks[0] is the first stack, stacks[0][0] is the bottom item on said stack
for j in range(0, len(setup_lines)):
    for i in range(0, num_stacks):
        item = setup_lines[j][i * 4 + 1]
        print(item, end='')
        if item != ' ':
            stacks[i].append(item)
    print('\n')

#get operation instructions
instructions : list[str] = list()
while line != '':
    instructions.append(line)
    
    line = input_file.readline()
instructions.pop(0) #remove leading '\n'

def pop_multiple(l : list, num_items : int) -> list:
    o = list()
    o.append(l.pop())
    
    start_index = len(l) - num_items
    end_index = len(l) - 1
    for i in range(end_index, start_index, -1): # start from end of array so popping doesn't mess up indexing
        o.insert(0, l.pop(i))
        
    return o

#execute instructions
while len(instructions) != 0:
    inst = instructions.pop(0)
    inst = inst.split()
    count = int(inst[1])
    origin = int(inst[3]) - 1
    destination = int(inst[5]) - 1
    stacks[destination].extend(pop_multiple(stacks[origin], count))

output : str = ""
for i in range(0, num_stacks):
    output += str(stacks[i][len(stacks[i]) - 1])
    
print(output)