#The score for a single round is the score for the shape you selected 
#(1 for Rock, 2 for Paper, and 3 for Scissors) 
# plus the score for the outcome of the round 
# (0 if you lost, 3 if the round was a draw, and 6 if you won).

input_file = open("day2.txt")

total_points = 0
for line in input_file:
    opponent_move = line[0]
    desired_result = line[2]
    
    points = 0
    match opponent_move:
        case 'A':
            match desired_result:
                case 'X':
                    points += 0 + 3
                case 'Y':
                    points += 3 + 1
                case 'Z':
                    points += 6 + 2
        case 'B':
            match desired_result:
                case 'X':
                    points += 0 + 1
                case 'Y':
                    points += 3 + 2
                case 'Z':
                    points += 6 + 3
        case 'C':
            match desired_result:
                case 'X':
                    points += 0 + 2
                case 'Y':
                    points += 3 + 3
                case 'Z':
                    points += 6 + 1
    
    #print(" ".join([str(opponent_move), str(desired_result), str(points)]))
    total_points += points
print(total_points)