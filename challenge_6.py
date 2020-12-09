#!/usr/bin/python3
import string

class group_answers(object):
    def __init__(self):
        self.answer_map = dict.fromkeys(string.ascii_lowercase, 0)
    
    def add_tally(self, letter):
        self.answer_map[letter] += 1
    
    def count_all_answered(self, num_members):
        answer = 0
        for key in self.answer_map:
            if self.answer_map[key] == num_members: answer += 1
        
        return answer

with open('input.txt', 'r') as f:
    lines = f.read().splitlines()


total_count = 0
common_answers = 0
group_answered = []
num_members = 0
current_group = group_answers()
for line in lines:
    if line == "":
        total_count += len(group_answered)
        common_answers += current_group.count_all_answered(num_members)
        group_answered = []
        num_members = 0
        current_group = group_answers()
    else:
        num_members += 1
        for q in line:
            current_group.add_tally(q)
            if q not in group_answered: group_answered.append(q)
total_count += len(group_answered)
common_answers += current_group.count_all_answered(num_members)

print("Total Count: ", total_count)
print("Part 2: ", common_answers)