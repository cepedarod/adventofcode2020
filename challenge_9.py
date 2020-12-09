#!/usr/bin/python3

# Challenge 9

#-----------------------------------------------------
# MAIN CODE BELOW
#-----------------------------------------------------
# Open input file line by line
with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

preambles = lines[0:25]
#print(preambles)    #DEBUG
data = lines[25:]
valid = False
# Find answer to part 1
while True:
    target = int(data[0])
    #print(target)   #DEBUG
    for it, x in enumerate(preambles):
        for y in preambles[it+1:]:
            #print(x, " + ", y)   #DEBUG
            if int(x) + int(y) == target:
                #print(x, " + ", y, " = ", target)   #DEBUG
                valid = True
                break
        if valid == True: break
    if valid == False:
        #print(preambles)                                #DEBUG
        #print("could not find answer for: ", target)    #DEBUG    
        print("Part 1 Answer: ", target)
        break
    else:
        preambles.pop(0)
        preambles.append(target)
        data.pop(0)
        valid = False
data_2 = lines[:lines.index(str(target))]    #omit all numbers past target
answer_set = []         # List that compiles all numbers added so far
answer_found = False
# Finda answer to part 2
while not answer_found:
    for it, x in enumerate(data_2):
        total_sum = int(x)
        answer_set.append(int(x))
        for y in data_2[it+1:]:
            total_sum += int(y)
            answer_set.append(int(y))

            if total_sum == target:
                answer_set.sort()                               # Once answer is found list needs to be sorted to get LARGEST and SMALLEST values
                answer = answer_set[0] + answer_set[-1]         # Not First and last
                #print(answer_set)                               #DEBUG
                #print( answer_set[0], " + ", answer_set[-1])    #DEBUG
                print("Part 2 Answer: ", answer)
                answer_found = True
                break
            elif total_sum > target: 
                answer_set = []
                break
        if answer_found: break

