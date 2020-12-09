#!/usr/bin/python3

def find_Seat(boarding_pass):
    row_val = 0
    col_val = 0
    mod_row = 64
    mod_col = 4
    for letter in boarding_pass:
       if letter == 'B': row_val += mod_row
       elif letter == 'R': col_val += mod_col

       if letter == 'B' or letter == 'F': mod_row = mod_row / 2
       elif letter == 'L' or letter == 'R': mod_col = mod_col / 2
    
    return row_val, col_val

def list_empty(map):
    list_of_empty = []
    for row_num, row in enumerate(map):
        for col_num, col in enumerate(row):
            if col == 0: list_of_empty.append((row_num, col_num))
    return list_of_empty

def list_missing_ids(id_list):
    last_id = 0
    possible_solutions = []
    for i in id_list:
        if last_id == 0: last_id = i
        elif i != last_id + 1: possible_solutions.append(last_id+1)
        last_id = i
    return possible_solutions


with open('input.txt', 'r') as f:
    #lines = f.readlines()
    lines = f.read().splitlines()

map = [[0 for c in range(8)] for r in range(128)]

max_id = 0
id_list = []
for line in lines:
    row, col = find_Seat(line)
    map[int(row)][int(col)] = 1
    id = (int(row) * 8 + int(col))
    id_list.append(id)
    if (int(row) * 8 + int(col)) > max_id: max_id = (int(row) * 8 + int(col))

'''
# Visual printing of info
open_seats = list_empty(map)
for seat in open_seats:
    print(seat)

for i in id_list:
    print(i)
'''

id_list.sort()
possible_solutions = list_missing_ids(id_list)
for p in possible_solutions:
    print(p)

print("Max ID: ", max_id)