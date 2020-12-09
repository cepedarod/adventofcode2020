#!/usr/bin/python3

numbers = []


with open('input.txt', 'r') as f:
    numbers = f.readlines()

while True:
    leftover = numbers[1:]
    it_1 = 1
    for n in numbers:
        others = leftover[it_1:]
        it_2 = 1
        for i in leftover:
            others = leftover[it_2:]
            for ii in others:
                if int(n) + int(i) + int(ii) == 2020:
                    print(int(n) * int(i) * int(ii))
                    return
            it_2 += 1
        it_1 += 1