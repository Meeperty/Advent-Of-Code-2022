input_file = open('C:/Users/Us/source/repos/Advent Of Code 2022/day10/day10.txt')

sum = 0
x_register = 1
cycles_left_in_inst = 0
total_cycles = 0
done = False
while not done:
    total_cycles += 1
    if total_cycles == 20 or (total_cycles - 20) % 40 == 0:
        print(f"strength at cycle {total_cycles} is {total_cycles * x_register}")
        sum += total_cycles * x_register
        
    if cycles_left_in_inst == 0:
        line = input_file.readline()
        instruction = line[:4]
        if instruction == '':
            break
        
    
        
    if cycles_left_in_inst == 0:
        if instruction == "noop":
            cycles_left_in_inst = 1
        if instruction == "addx":
            cycles_left_in_inst = 2
            argument = int(line[4:].strip())
    
    if instruction == "addx" and cycles_left_in_inst == 1:
        x_register += argument
    cycles_left_in_inst -= 1

print(f"total strength is {sum}")