#!/usr/bin/python3

# Challenge 12


#-----------------------------------------------------
# MAIN CODE BELOW
#-----------------------------------------------------
# Open input file line by line
with open('input.txt', 'r') as f:
    lines = f.read().splitlines()
#-----------------------------------------------------
n_s = 0                     # Noth is positive, South is negative
e_w = 0                     # East is positive, West is negative
current_direction = 'E'     # Will be on of the 4 cardinal directions
current_direction_index = 1 # Index refers to the list number of current direction of the boat
directions = ['N','E','S','W']

'''
# PART 1
for line in lines:
    if line.startswith('R') or line.startswith('L'):
        index_modifier = 0
        if line[1:] == "90": index_modifier = 1
        elif line[1:] == "180": index_modifier = 2
        elif line[1:] == "270": index_modifier = 3
        if line.startswith('L'): 
            index_modifier = index_modifier * -1
            current_direction = directions[current_direction_index + index_modifier]
        else: current_direction = directions[(current_direction_index + index_modifier) % 4]
        current_direction_index = directions.index(current_direction)               # Reset index value to avoid "index out of range"

    elif line.startswith('N'): n_s += int(line[1:])
    elif line.startswith('S'): n_s -= int(line[1:])
    elif line.startswith('E'): e_w += int(line[1:])
    elif line.startswith('W'): e_w -= int(line[1:])
    elif line.startswith('F'):
        if current_direction == 'N': n_s += int(line[1:])
        elif current_direction == 'S': n_s -= int(line[1:])
        elif current_direction == 'E': e_w += int(line[1:])
        elif current_direction == 'W': e_w -= int(line[1:])

answer = abs(n_s) + abs(e_w)
print("Part 1: ", answer)
'''

# Part 2
# For part 2, current direction corresponding to the second number in waypoint. First number will always be 90 left of that
waypoint = {'N':1,'E':10, 'S':0, 'W':0}   # represents waypoint with first number being n_s relative to ship and second number being e_w relative to ship
for line in lines:
    if line.startswith('R') or line.startswith('L'):
        if line == "R90" or line == "L270": index_modifier = -3
        elif line[1:] == "180": index_modifier = -2
        elif line == "L90" or line == "R270": index_modifier = -1
        new_waypoint = {}
        # iterate through N,E,S,W and rotate cordinate values acordingly
        for direction in directions:
            new_waypoint[directions[directions.index(direction) + index_modifier]] = waypoint[direction]
        waypoint = new_waypoint

    elif line.startswith('F'):
        n_s += int(line[1:]) * (waypoint['N'] - waypoint['S'] )
        e_w += int(line[1:]) * (waypoint['E'] - waypoint['W'] )
    else: waypoint[line[0]] += int(line[1:])


answer = abs(n_s) + abs(e_w)
print("Part 2: ", answer)