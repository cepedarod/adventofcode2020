#!/usr/bin/python3
import string

class bag_type(object):
    def __init__(self, name):
        self.name = name
        self.smaller_bags = {}
        self.holds_gold = False
        self.checked = False

        self.recursive_sub_bags = ''
    
    def add_bag(self, bag_name, amount):
        self.smaller_bags[bag_name] = amount

    def print_info(self):
        return self.name, self.smaller_bags

def bag_search(master_list_of_bags, bag_object):
    #print("looking at ", bag_object.name) #DEBUG
    if not bag_object.smaller_bags: 
        #print("ROCK bottom!") #DEBUG
        master_list_of_bags[bag_object.name].checked = True
        return False
    for bag in bag_object.smaller_bags:
        #print("sub bag: ", bag, "under ", bag_object.name) #DEBUG
        if bag == "shiny gold":
            #print("FOUND GOLD ") #DEBUG
            master_list_of_bags[bag_object.name].holds_gold = True
            master_list_of_bags[bag_object.name].checked = True
            return True
        elif master_list_of_bags[bag].holds_gold == True:
            #print("FOUND GOLD ") #DEBUG
            master_list_of_bags[bag_object.name].holds_gold = True
            master_list_of_bags[bag_object.name].checked = True
            return True
        elif master_list_of_bags[bag].checked == False:
            master_list_of_bags[bag].holds_gold = bag_search(master_list_of_bags,master_list_of_bags[bag])
            master_list_of_bags[bag].checked = True
            if master_list_of_bags[bag].holds_gold == True: return True
    #print("ROCK bottom!") #DEBUG
    return False

def count_sub_bags(master_list_of_bags, master_count, bag_object):
    #print("looking at ", bag_object.name) #DEBUG
    new_count = 0       
    if not bag_object.smaller_bags: 
        master_list_of_bags[bag_object.name].recursive_sub_bags = 0
        #print("ROCK bottom!") #DEBUG
        return 0
    
    for bag in bag_object.smaller_bags:
        #print("sub bag: ", bag, "under ", bag_object.name) #DEBUG
        if type(master_list_of_bags[bag].recursive_sub_bags) == int:
            #print("sub bag: ", bag, "already counted") #DEBUG
            new_count += (master_list_of_bags[bag].recursive_sub_bags + 1) * int(bag_object.smaller_bags[bag]) 
        else:
            #print("recursing") #DEBUG
            bag_subtotal = count_sub_bags(master_list_of_bags, new_count, master_list_of_bags[bag])
            master_list_of_bags[bag].recursive_sub_bags = bag_subtotal
            new_count += (master_list_of_bags[bag].recursive_sub_bags + 1) * int(bag_object.smaller_bags[bag]) 
    return new_count


with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

list_of_bags = {}
for line in lines:
    formated_line = line[:-1]
    bag_name = formated_line.split(" bags contain ")[0]
    new_bag = bag_type(bag_name)
    smaller_bags = formated_line.split(" bags contain ")[1]
    for b in smaller_bags.split(", "):
        other_bag_quantity = b.split(" ", 1)[0]
        other_bag_name = b.split(" ", 1)[1].replace(" bags", "").replace(" bag", "")
        if other_bag_quantity != "no":
            new_bag.add_bag(other_bag_name, other_bag_quantity)
    list_of_bags[bag_name] = new_bag
'''
#  DEBUG
for b in list_of_bags:
    print(list_of_bags[b].print_info())
'''
part_one_solution = 0
for bag in list_of_bags:
    if list_of_bags[bag].checked == False:
        list_of_bags[bag].holds_gold = bag_search(list_of_bags, list_of_bags[bag])
    if list_of_bags[bag].holds_gold == True: 
        #print(bag, " has GOLD ") #DEBUG
        part_one_solution += 1

print("Part 1: ", part_one_solution)

part_two_solution = count_sub_bags(list_of_bags, 0, list_of_bags["shiny gold"])
print("Part 2: ", part_two_solution)
