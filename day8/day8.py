input_file = open("C:/Users/Us/source/repos/Advent Of Code 2022/day8/day8.txt")

def get_column(c : int, l : list):
    o = list()
    for r in range(len(l)):
        o.append(l[r][c])
    return o

min = 0
max = 99

sum = 0
trees = list()
for r in range(max):
    tree_line = list()
    text_line = input_file.readline()
    for c in range(max):
        tree_line.append(text_line[c])
    trees.append(tree_line)

for r in range(0, max):
    for c in range(0, max):
        if r != min and r != max - 1 and c != min and c != max - 1:
            row = trees[r]
            col = get_column(c, trees)
            this_height = trees[r][c]
            earlier_in_row, later_in_row = row[:c], row[c + 1:]
            earlier_in_col, later_in_col = col[:r], col[r + 1:]
            visible_left, visible_right, visible_up, visible_down = True, True, True, True
            for height in earlier_in_row:
                if height >= this_height:
                    visible_left = False
            for height in later_in_row:
                if height >= this_height:
                    visible_right = False
            for height in earlier_in_col:
                if height >= this_height:
                    visible_up = False
            for height in later_in_col:
                if height >= this_height:
                    visible_down = False
            if visible_left or visible_right or visible_up or visible_down:
                sum += 1
                print(this_height + " at " + str(r) + ", " + str(c) + " is visible")
        else:
            sum += 1
            print(trees[r][c] + " at " + str(r) + ", " + str(c) + " is visible")

print(sum)