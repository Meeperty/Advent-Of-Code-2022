input_file = open("C:/Users/Us/source/repos/Advent Of Code 2022/day3/day3.txt")

def priority(char : str):
    if len(char) != 1:
        raise Exception("input to priority() was over 1 char long")
    code = ord(char)
    if char.upper() == char:
        #27 is A's priority, 65 is A's ASCII code
        return code + (27 - 65)
    else:
        #1 is a's priority, 
        return code + (1 - 97)

sum = 0
i = 1
sack1 : str
sack2 : str
for line in input_file:
    if i % 3 == 1:
        sack1 = line
    elif i % 3 == 2:
        sack2 = line
    else:
        for char in line:
            if (char in sack1) & (char in sack2):
                sum += priority(char)
                break
    i += 1
    
print(str(sum))