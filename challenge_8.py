#!/usr/bin/python3
#-----------------------------------------------------
# Class that contains details about each instruction
class instruction(object):
    def __init__(self, name, value):
        self.name = name
        self.value = value
        self.excecuted = False
    def flip(self):
        if self.name == "jmp": self.name = "nop"
        elif self.name == "nop": self.name = "jmp"

#-----------------------------------------------------
# This function processes each isntruction and sets the accumulator value and the next instruction index
def exec(instruc, accumulator, current_instruction):
    instruc.excecuted = True
    if instruc.name == "jmp":
        next_instruction = current_instruction + instruc.value
        return next_instruction, accumulator
    elif instruc.name == "acc":
        accumulator = accumulator + instruc.value
    next_instruction = current_instruction + 1
    return next_instruction, accumulator

#-----------------------------------------------------
# MAIN CODE BELOW
#-----------------------------------------------------
# Open input file line by line
with open('input.txt', 'r') as f:
    lines = f.read().splitlines()


instructions = []               # stores all instructions in order given
flippable_instructions = []     # used to store instruction index that could be the cause of the problem
                                # sort input data into instructions objects and place in list
for count, line in enumerate(lines):
    instruction_name = line.split(" ")[0]
    val = int(line.split(" ")[1])
    instructions.append(instruction(instruction_name, val))
    if instruction_name == "jmp" or instruction_name == "nop":
        flippable_instructions.append(count)
#print(flippable_instructions) #DEBUG

accumulator = 0
current_instruction = 0
next_instruction = 1

instructions[flippable_instructions[0]].flip()      # Used for part 2 only
while current_instruction <= len(instructions):
    # Process current instruction
    next_instruction, accumulator = exec(instructions[current_instruction], accumulator, current_instruction)
    instructions[current_instruction].excecuted = True 

    if next_instruction >= len(instructions): break # If condition is met, code ran successfuly
    elif instructions[next_instruction].excecuted == True:
        #print("Part 1: ", accumulator)                 # Used for part 1 only
        #break                                          # Used for part 1 only
        instructions[flippable_instructions[0]].flip()  # Used for part 2 only
        flippable_instructions.pop(0)                   # Used for part 2 only
        #print("Flipping: ", flippable_instructions[0]) #DEBUG
        instructions[flippable_instructions[0]].flip()  # Used for part 2 only
        for i in instructions: i.excecuted = False      # Used for part 2 only
        accumulator = 0                                 # Used for part 2 only
        current_instruction = 0                         # Used for part 2 only
        next_instruction = 1                            # Used for part 2 only
    else:
        current_instruction = next_instruction
        
print("Program Fully Ran. Final Accumulator value: ", accumulator)