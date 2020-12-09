#!/usr/bin/python3


valid_count = 0

with open('input.txt', 'r') as f:
    lines = f.readlines()

for line in lines:
    temp = line.split(" ")
    pswd = temp[2]
    target = temp[1][0]
    mini = int(temp[0].split("-")[0])
    maxi = int(temp[0].split("-")[1])

    if (pswd[(mini-1)] == target and pswd[(maxi-1)] != target) or (pswd[(mini-1)] != target and pswd[(maxi-1)] == target):
        valid_count += 1
print(valid_count)

    
