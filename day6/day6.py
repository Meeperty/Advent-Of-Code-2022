import collections

def contains(list_to_check : list, element):
    for object in list_to_check:
        if element == object:
            return True
    return False

input_file = open("C:/Users/Us/source/repos/Advent Of Code 2022/day6/day6.txt")

index = 0
window = [0, 0, 0, 0]
for line in input_file:
    for char in line:
        index += 1
        window.remove(window[0])
        if (not contains(window, char)) and index > 3:
            print(index)
            exit()
        window.append(char)