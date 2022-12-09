input_file = open("C:/Users/Us/source/repos/Advent Of Code 2022/day8/day8.txt")

def get_column(c : int, l : list):
    o = list()
    for r in range(len(l)):
        o.append(l[r][c])
    return o

min = 0
max = 99

highest_score = 0
trees = list()
for r in range(max):
    line = list()
    text_line = input_file.readline()
    for c in range(max):
        line.append(int(text_line[c]))
    trees.append(line)

for r in range(0, max):
    for c in range(0, max):
        row = trees[r]
        col = get_column(c, trees)
        this_height = trees[r][c]
        
        earlier_in_row, later_in_row = row[:c], row[c + 1:]
        earlier_in_col, later_in_col = col[:r], col[r + 1:]
        earlier_in_row = list(reversed(earlier_in_row))
        earlier_in_col = list(reversed(earlier_in_col))
        
        visible_left, visible_right, visible_up, visible_down = 0, 0, 0 ,0
        
        for h in earlier_in_row:
            visible_left += 1
            if h >= this_height:
                break
        for h in later_in_row:
            visible_right += 1
            if h >= this_height:
                break
        for h in earlier_in_col:
            visible_up += 1
            if h >= this_height:
                break
        for h in later_in_col:
            visible_down += 1
            if h >= this_height:
                break
        visibility_score = visible_left * visible_right * visible_up * visible_down
        
        print("height " + str(this_height) + " at " + str(r) + ", " + str(c) + " has " + str(visibility_score))
        if (visibility_score > highest_score):
            highest_score = visibility_score

print(highest_score)