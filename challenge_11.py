#!/usr/bin/python3

# Challenge 11



#-----------------------------------------------------
# Class that contains details about each instruction
class seat_node(object):
    def __init__(self, static, occupied):
        self.static = static
        self.occupied = occupied
        self.adjacent_nodes = []
        self.next_node_value = ''

    def add_adjacent(self, list_of_nodes):
        self.adjacent_nodes = list_of_nodes

    def print_state(self):
        if self.static == True: return "."
        elif self.occupied == True: return "#"
        else: return "L"
    
    def determine_new_value(self):
        # If seat is originally unoccupied
        if self.occupied == False and not self.static:
            for node in self.adjacent_nodes:
                # If any adjacent seats are full, seat stays empty
                if node.occupied == True:
                    self.next_node_value = False
                    return False
            self.next_node_value = True
            return True
        # If seat is originally occupied
        elif self.occupied == True:
            adjacent_counter = 0
            for node in self.adjacent_nodes:
                if node.occupied == True: adjacent_counter += 1
                # if 4 adjacent seats are occupied, seat will empty
                # Value updated to 5 for part 2
                if adjacent_counter == 5:
                    self.next_node_value = False
                    return False     
            self.next_node_value = True
            return True
    # This function updates the node value and returns True if value changed or False if it didnt
    def update_value(self):
        if self.static == True: return False
        elif self.occupied == self.next_node_value:
            return False
        else:
            self.occupied = self.next_node_value
            return True
#-----------------------------------------------------
# This Function takes a reference map, corrdinates of the node in question and a dirrection of search
# dirrections are abreviated to the first letters of each word  (e.g. 'T'op 'L'eft = tl, 'R'ight = r, 'B'ottom = b, etc)
# Function returns y_coordinate and x_coordinate of the found seat
# Function will return -1, -1 if no seat of interest was found
def seat_search(seat_map, y_coordinate, x_coordinate, dirrection):

    seat_found = False
    # Search left
    if dirrection == "l":
        x_coordinate -= 1
        while x_coordinate >= 0:
            if seat_map[y_coordinate][x_coordinate].static == False: 
                seat_found = True
                break
            x_coordinate -= 1

    # Search Right
    elif dirrection == "r":
        x_coordinate += 1
        while x_coordinate < len(seat_map[0]):
            if seat_map[y_coordinate][x_coordinate].static == False:
                seat_found = True
                break
            x_coordinate += 1
    # Search top (up)
    elif dirrection == "t":
        y_coordinate -= 1
        while y_coordinate >= 0:
            if seat_map[y_coordinate][x_coordinate].static == False:
                seat_found = True
                break
            y_coordinate -= 1
    # Search bottom (down)
    elif dirrection == "b":
        y_coordinate += 1
        while y_coordinate < len(seat_map):
            if seat_map[y_coordinate][x_coordinate].static == False:
                seat_found = True
                break
            y_coordinate += 1
    # Search top right
    elif dirrection == "tr":
        x_coordinate += 1
        y_coordinate -= 1
        while x_coordinate < len(seat_map[0]) and y_coordinate >= 0:
            if seat_map[y_coordinate][x_coordinate].static == False:
                seat_found = True
                break
            x_coordinate += 1
            y_coordinate -= 1
    # Search top left
    elif dirrection == "tl":
        x_coordinate -= 1
        y_coordinate -= 1
        while x_coordinate >= 0 and y_coordinate >= 0:
            if seat_map[y_coordinate][x_coordinate].static == False:
                seat_found = True
                break
            x_coordinate -= 1
            y_coordinate -= 1
    # Search bottom right
    elif dirrection == "br":
        x_coordinate += 1
        y_coordinate += 1
        while x_coordinate < len(seat_map[0]) and y_coordinate < len(seat_map):
            if seat_map[y_coordinate][x_coordinate].static == False:
                seat_found = True
                break
            x_coordinate += 1
            y_coordinate += 1
    # Search bottom left
    elif dirrection == "bl":
        x_coordinate -= 1
        y_coordinate += 1
        while x_coordinate >= 0 and y_coordinate < len(seat_map):
            if seat_map[y_coordinate][x_coordinate].static == False:
                seat_found = True
                break
            x_coordinate -= 1
            y_coordinate += 1
    # Return result
    if seat_found: return y_coordinate, x_coordinate
    else: return -1, -1
#-----------------------------------------------------
# This Function prints a visual of the map for debugging
def print_map(seat_map):
    row_chars = ''
    for row in seat_map:
        for node in row:
            if node.static == True: row_chars += "."
            elif node.occupied == True: row_chars += "#"
            else: row_chars += "L"
        print(row_chars)
        row_chars = ''
    print("------------------------------")

#-----------------------------------------------------
# MAIN CODE BELOW
#-----------------------------------------------------
# Open input file line by line
with open('input.txt', 'r') as f:
    lines = f.read().splitlines()


seat_map = []
row = []
# initialize seat_map using input. Each item in the 2D array is a node_object with initial seat value
for line in lines:
    for c in line:
        if c == "L": row.append(seat_node(False, False))
        elif c == ".": row.append(seat_node(True, False))
    seat_map.append(row)
    row = []

'''
#-----------------------------------------------------
# Determine relevant adjacent nodes for each node in seat_map  *Part 1* 
column_end = len(seat_map) - 1
row_end = len(seat_map[0]) - 1
relevant_nodes = []
for y, line in enumerate(seat_map):
    for x, node in enumerate(line):
        if x != 0:
            if y != 0: 
                relevant_nodes.append(seat_map[y-1][x-1])                       # Top left node is of interest 
            relevant_nodes.append(seat_map[y][x-1])                             # Left node is of interest
            if y != column_end: 
                relevant_nodes.append(seat_map[y+1][x-1])                       # Bottom left node is of interest
            
        
        if x != row_end:
            if y != 0: relevant_nodes.append(seat_map[y-1][x+1])                # Top right node is of interest 
            relevant_nodes.append(seat_map[y][x+1])                             # Right node is of interest
            if y != column_end: 
                relevant_nodes.append(seat_map[y+1][x+1])                       # Bottom Right node is of interest
        
        if y != 0: relevant_nodes.append(seat_map[y-1][x])                        # Top node is of interest
        if y != column_end: relevant_nodes.append(seat_map[y+1][x])               # Bottom node is of interest
        # Push info to seat_node
        seat_map[y][x].add_adjacent(relevant_nodes)
        relevant_nodes = []
print("Part 1")
#-----------------------------------------------------
'''
#-----------------------------------------------------
# Determine relevant adjacent nodes for each node in seat_map  *Part 2* 
column_end = len(seat_map) - 1
row_end = len(seat_map[0]) - 1
relevant_nodes = []
search_directions = ['tl', 'l', 'bl', 'b', 'br', 'r', 'tr', 't']
for y, line in enumerate(seat_map):
    for x, node in enumerate(line):
        # If node is a seat, search in each direction to find nodes of itnerest
        if node.static == False:
            for direction in search_directions:
                y_target, x_target = seat_search(seat_map, y, x, direction)
                if x_target > row_end or y_target > column_end:
                    print(direction, "x target: ", x_target, "y target: ", y_target)    #DEBUG
                    print("x: ", x, "y: ", y)
                # If node of interest was found, add node as a node of interest
                if x_target != -1:
                    relevant_nodes.append(seat_map[y_target][x_target])
            
        # Push info to seat_node
        seat_map[y][x].add_adjacent(relevant_nodes)
        relevant_nodes = []
print("Part 2")
#-----------------------------------------------------
# Cycle through map changes until nothing changes
map_changed = True
while map_changed:
    #print_map(seat_map) #DEBUG
    map_changed = False
    for row in seat_map:
        for node in row:
            node.determine_new_value()
    # since all changes have to happen at once, updating values has to happen durring a second loop
    for row in seat_map:
        for node in row:
            node_changed = node.update_value()
            if node_changed: map_changed = True

# once the map stablizes, count the number of occupied seats 
occupied_counter = 0
for row in seat_map:
    for node in row:
        if node.occupied: occupied_counter += 1

print("Occupied Seats: ", occupied_counter)