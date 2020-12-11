#!/usr/bin/python3

numbers = []
with open('input.txt', 'r') as f:
    numbers = f.readlines()

still_looking = True
while still_looking:
    for i, num_1 in enumerate(numbers):
        for ii, num_2 in enumerate(numbers[i+1:]):
            for num_3 in numbers[i+ii+1:]:
                if int(num_1) + int(num_2) + int(num_3) == 2020:
                    print(int(num_1) * int(num_2) * int(num_3))
                    still_looking = False
                    break
            if still_looking == False: break
        if still_looking == False: break