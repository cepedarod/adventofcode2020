#!/usr/bin/python3


with open('input.txt', 'r') as f:
    #lines = f.readlines()
    lines = f.read().splitlines()

valid_docs = 0
byr = False
iyr = False
eyr = False
hgt = False
hcl = False
ecl = False
pid = False
cid = False
for line in lines:
    if line == "\n" or line == '/n' or line == "":
        if byr and iyr and eyr and hgt and hcl and ecl and pid: valid_docs += 1
        byr = False
        iyr = False
        eyr = False
        hgt = False
        hcl = False
        ecl = False
        pid = False
        cid = False
    else:
        data = line.split(" ")
        for item in data:
            item.strip
            if "byr" in item:
                d = item.split(":")[1]
                if len(d) == 4 and int(d) >= 1920 and int(d) <= 2002: byr = True
            elif "iyr:" in item: 
                d = item.split(":")[1]
                if len(d) == 4 and int(d) >= 2010 and int(d) <= 2020: iyr = True
            elif "eyr:" in item: 
                d = item.split(":")[1]
                if len(d) == 4 and int(d) >= 2020 and int(d) <= 2030: eyr = True
            elif "hgt:" in item: 
                d = item.split(":")[1]
                if "cm" in d : 
                    if d.split("cm")[0].isnumeric():
                        if int(d.split("cm")[0]) >= 150 and int(d.split("cm")[0]) <= 193: hgt = True
                elif "in" in d:
                    if d.split("in")[0].isnumeric():
                        if int(d.split("in")[0]) >= 59 and int(d.split("in")[0]) <= 76: hgt = True
            elif "hcl:" in item: 
                d = item.split(":")[1]
                if d.startswith("#") and len(d) == 7:
                    hex_num = d.split("#")[1]
                    try:
                        int(hex_num, 16)        #Check if valid Hex number
                        hcl = True
                    except:
                        hcl = False
            elif "ecl:" in item: 
                d = item.split(":")[1]
                if d == "amb" or d == "blu" or d == "brn" or d == "gry" or d == "grn" or d == "hzl" or d == "oth": ecl = True
            elif "pid:" in item: 
                d = item.split(":")[1]
                if len(d) == 9 and d.isnumeric(): pid = True
            elif "cid:" in item: cid = True

if byr and iyr and eyr and hgt and hcl and ecl and pid: valid_docs += 1

print(valid_docs)


