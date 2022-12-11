input_file = open('day10test.txt', 'r')

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
    
    if instruction == "addx" and cycles_left_in_inst == 1:
        x_register += argument
    cycles_left_in_inst -= 1
    
    total_cycles += 1
    if total_cycles == 20 or (total_cycles - 20) % 40 == 0:
        print("strength at cycle " + str(total_cycles) + " is " + str(total_cycles * x_register))
        sum += total_cycles * x_register
print("total strength is " + str(sum))