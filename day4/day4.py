input_file = open("/Users/brothers/source/Advent-Of-Code-2022/day4/day4.txt")

sum = 0
for line in input_file:
    r1, r2 = line.split(',', 1)
    r1n1, r1n2 = r1.split('-')
    r2n1, r2n2 = r2.split('-')
    r1n1 = int(r1n1)
    r1n2 = int(r1n2)
    r2n1 = int(r2n1)
    r2n2 = r2n2.rstrip()
    r2n2 = int(r2n2)
    
    if ((r1n1 <= r2n1) and (r1n2 >= r2n2)) or ((r2n1 <= r1n1) and (r2n2 >= r1n2)):
        sum += 1
        print(line.rstrip())
        
print(sum)