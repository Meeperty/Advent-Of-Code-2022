input_file = open('C:/Users/Us/source/repos/Advent Of Code 2022/day10/day10.txt')

sum = 0
x_register = 1
cycles_left_in_inst = 0
total_cycles = 0
done = False
while not done:
    
    
    if cycles_left_in_inst == 0:
        line = input_file.readline()
        instruction = line[:4]
        if instruction == '':
            break
        if instruction == "noop":
            cycles_left_in_inst = 1
        if instruction == "addx":
            cycles_left_in_inst = 2
            argument = int(line[4:].strip())
    
    pos_in_row = total_cycles % 40
    if pos_in_row - 1 == x_register or pos_in_row == x_register or pos_in_row + 1 == x_register:
        print('#', end='')
    else:
        print('.', end='')
    if pos_in_row == 0:
        print('\n', end='')
    
    if instruction == "addx" and cycles_left_in_inst == 1:
        x_register += argument
    cycles_left_in_inst -= 1
    total_cycles += 1