#!/usr/bin/python3

# Challenge 10
#-----------------------------------------------------
# Class that contains details about each instruction
class adaptor_node(object):
    def __init__(self, value, valid_hops):
        self.value = value
        self.valid_hops = valid_hops
        self.number_of_paths = ''
        self.checked = False

#-----------------------------------------------------
# Recursive Path search
# returns number of paths for a node. If its a dead end, serach returns 0
def chain_search(a_node, adaptor_list, last_adaptor_value, device_joltage):
    # If the node has no further hops and its value is the device target path is talied
    # Otherwise, path is a dead end and value returned will be 0
    number_of_paths = 0
    if not a_node.valid_hops:
        if device_joltage == a_node.value: number_of_paths = 1
    # If the node has valid hops, tally the valid paths from those
    else:
        for hop in a_node.valid_hops:
            # If number of paths is already known for this hop, add that value
            if adaptor_list[hop].checked == True: 
                number_of_paths += adaptor_list[hop].number_of_paths
            # If hop hasnt been explored, recurse
            else:
                number_of_paths += chain_search(adaptor_list[hop], adaptor_list, a_node.value, device_joltage)
    
    adaptor_list[a_node.value].number_of_paths = number_of_paths
    adaptor_list[a_node.value].checked = True
    return number_of_paths




#-----------------------------------------------------
# MAIN CODE BELOW
#-----------------------------------------------------
# Open input file line by line
with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

adaptors = []
for line in lines:
    adaptors.append(int(line))

adaptors.sort()
one_jolt_counter = 0
three_jolt_counter = 1      #Starts at 1 because last adaptor to device is always a 3 jolt difference
device_joltage = adaptors[-1] + 3

if adaptors[0] == 1: one_jolt_counter += 1
elif adaptors[0] == 3: three_jolt_counter += 1

for it, adaptor in enumerate(adaptors[1:], 1):
    if adaptor - adaptors[it-1] == 1: one_jolt_counter += 1
    elif adaptor - adaptors[it-1] == 3: three_jolt_counter += 1
    else: print(adaptor - adaptors[it-1])

print("Device Joltage: ",device_joltage)
print("Answer Part 1: ", one_jolt_counter * three_jolt_counter)


#### PART 2 ####

adaptors.append(device_joltage)     #add the device jotage as a node for accurate search
adaptors_part_two = {}              # Dict that holds node objects for search

# Determine valid hops for each node and initialize nodes into dictionary for reference in recursion
valid_hops = []
for it, adaptor in enumerate(adaptors):
    for next_node in adaptors[it+1:]:
        if next_node - adaptor <=3: valid_hops.append(next_node)
        else: break
    adaptors_part_two[adaptor] = adaptor_node(adaptor, valid_hops)
    valid_hops = []

# Solve problem
# Use adaptors list for loop instead of adaptors_part_two because it is numerically sorted already
number_of_chains = 0
for a in adaptors:
    if a > 3: break
    else:
        number_of_chains += chain_search(adaptors_part_two[a], adaptors_part_two, 0, device_joltage)

print("Part 2 Answer: ", number_of_chains)