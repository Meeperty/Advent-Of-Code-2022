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
for line in input_file:
    half1, half2 = line[:len(line)//2], line[len(line)//2:]
    
    shared_char : str
    found = False
    for char1 in half1:
        for char2 in half2:
            if char1 == char2:
                shared_char = char1
                found = True
            if found:
                break
        if found:
            break
    
    sum += priority(shared_char)
    
print(str(sum))
# print(" ".join(["priority of \'A\' is ", str(priority('A'))]))
# print(" ".join(["priority of \'a\' is ", str(priority('a'))]))
# print(" ".join(["priority of \'Z\' is ", str(priority('Z'))]))
# print(" ".join(["priority of \'z\' is ", str(priority('z'))]))