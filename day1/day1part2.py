input_file = open("day1.txt")

first = 0
second = 0
third = 0
current_total = 0
for line in input_file:
    if line != "\n":
        current_total += int(line)
    else:
        if current_total > first:
            third = second
            second = first
            first = current_total
        elif current_total > second:
            third = second
            second = current_total
        elif current_total > third:
            third = current_total
        current_total = 0

print("first is " + str(first))
print("second is " + str(second))
print("third is " + str(third))
print("total: " + str(first + second + third))