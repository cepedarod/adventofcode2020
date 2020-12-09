#!/usr/bin/python3

def split(word): 
    return [char for char in word]  

map = []
x_coordinate = 0
trees_hit = 0

with open('input.txt', 'r') as f:
    lines = f.readlines()

for line in lines:
    map.append(split(line.strip('\n')))
width = len(map[0])

for level in map:
    if x_coordinate == 0: x_coordinate += 1
    else:
        x = x_coordinate % width
        if level[x] == '#': trees_hit += 1
        x_coordinate += 1
track_1 = trees_hit
trees_hit = 0
x_coordinate = 0


for level in map:
    if x_coordinate == 0: x_coordinate += 3
    else:
        x = x_coordinate % width
        if level[x] == '#': trees_hit += 1
        x_coordinate += 3
track_2 = trees_hit
trees_hit = 0
x_coordinate = 0

for level in map:
    if x_coordinate == 0: x_coordinate += 5
    else:
        x = x_coordinate % width
        if level[x] == '#': trees_hit += 1
        x_coordinate += 5
track_3 = trees_hit
trees_hit = 0
x_coordinate = 0

for level in map:
    if x_coordinate == 0: x_coordinate += 7
    else:
        x = x_coordinate % width
        if level[x] == '#': trees_hit += 1
        x_coordinate += 7
track_4 = trees_hit
trees_hit = 0
x_coordinate = 0

skip = False
for level in map:
    
    if skip == True:
        skip = False
    elif x_coordinate == 0: 
        x_coordinate += 1
        skip = True
    else:
        x = x_coordinate % width
        if level[x] == '#': trees_hit += 1
        x_coordinate += 1
        skip = True
track_5 = trees_hit
trees_hit = 0

print("Track 1: ", track_1)
print("Track 2: ", track_2)
print("Track 3: ", track_3)
print("Track 4: ", track_4)
print("Track 5: ", track_5)

print("Answer: ", track_1 * track_2 * track_3 * track_4 * track_5)


