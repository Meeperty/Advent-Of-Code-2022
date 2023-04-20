from copy import deepcopy

def contains(list_to_check : list, element):
    for object in list_to_check:
        if element == object:
            return True
    return False

input_file = open("C:/Users/Us/source/repos/Advent Of Code 2022/day6/day6.txt")

def has_duplicate_characters(string : str) -> bool:
    for i in range(len(string) - 1):
        occurences = string.count(string[i])
        if occurences > 1:
            return True
    return False

def str_from_list(l : list) -> str:
    s = str()
    
    for item in l:
        s += str(item)
    
    return s

assert(not has_duplicate_characters("abcd"))
assert(has_duplicate_characters("aaaa"))
assert(has_duplicate_characters("ajab"))
assert(has_duplicate_characters("ajbj"))
#assert(not has_duplicate_characters(str(['j', 'p', 'q', 'm'])))

index = 0
window = ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0']
for line in input_file:
    for char in line:
        if (not has_duplicate_characters(str_from_list(window)) and index > 3):
            print(index)
            exit()
        window.remove(window[0])
        window.append(char)
        index += 1