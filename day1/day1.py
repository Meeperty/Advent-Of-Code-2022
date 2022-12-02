input_file = open("day1.txt")

current_total = 0
largest_total = 0
for line in input_file:
    if line != "\n":
        current_total += int(line)
    else:
        if current_total > largest_total:
            largest_total = current_total
        current_total = 0

print(largest_total)