import collections

input_file = open("/Users/brothers/source/Advent-Of-Code-2022/day5/day5.txt")

sum = 0
line = input_file.readline()
setup_lines = list()
num_stacks = 9
#get the first few lines that have initial position
while line != '\n':
    setup_lines.append(line)

setup_lines.reverse()

print(sum)