import re

class passport:
    byr = None
    iyr = None
    eyr = None
    hgt = None
    hcl = None
    ecl = None
    pid = None
    
    def add_byr(self, byr):
        if len(byr) == 4:
            try:
                if int(byr) >= 1920 and int(byr) <= 2002:
                    self.byr = int(byr)
            except:
                print("")
        else:
            print("")
            
    def add_iyr(self, iyr):
        if len(iyr) == 4:
            try:
                if int(iyr) >= 2010 and int(iyr) <= 2020:
                    self.iyr = int(iyr)
            except:
                a = 0
        else:
            a = 0
            
    def add_eyr(self, eyr):
        if len(eyr) == 4:
            try:
                if int(eyr) >= 2020 and int(eyr) <= 2030:
                    self.eyr = int(eyr)
            except:
                a = 0
        else:
            a = 0

    def add_hgt(self, hgt):
        split = re.split('(\d+)',hgt)

        try:
            if split[2] == "cm":
                if int(split[1]) >= 150 and int(split[1]) <= 193:
                    self.hgt = hgt
            if split[2] == "in":
                if int(split[1]) >= 59 and int(split[1]) <= 76:
                    self.hgt = hgt
        except:
            a = 0
            
    def add_hcl(self, hcl):
        if re.search('#[0-9a-fA-F]{6}', hcl):
            self.hcl = hcl
            
    def add_ecl(self, ecl):
        vals = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

        if ecl in vals:
            self.ecl = ecl
    def add_pid(self, pid):
        if len(pid) == 9:
            self.pid = pid
            
    def valid(self):
        if not(self.byr == None) and not(self.iyr == None) and not(self.eyr == None) and not(self.hgt == None) and not(self.hcl == None) and not(self.ecl == None) and not(self.pid == None):
            return True
        return False
    def print(self):
        print(self.byr,self.iyr,self.eyr,self.hgt,self.hcl,self.ecl,self.pid)


def part_1():
    with open("input.txt") as f:

        data = f.readlines()
        data.append('\n')

        current = passport()

        count = 0
        
        for line in data:
            if line == '\n':
                if current.valid():
                    count += 1
                current = passport()
            else:
                inputs = [val.split(":")for val in line.split()]
                for val in inputs:
                    if val[0] == "byr":
                        current.byr = val[1]
                    if val[0] == "iyr":
                        current.iyr = val[1]
                    if val[0] == "eyr":
                        current.eyr = val[1]
                    if val[0] == "hgt":
                        current.hgt = val[1]
                    if val[0] == "hcl":
                        current.hcl = val[1]
                    if val[0] == "ecl":
                        current.ecl = val[1]
                    if val[0] == "pid":
                        current.pid = val[1]
            
        return count

def part_2():
    with open("input.txt") as f:

        data = f.readlines()
        data.append('\n')

        current = passport()

        count = 0
        
        for line in data:
            if line == '\n':
                if current.valid():
                    count += 1
                current = passport()
            else:
                inputs = [val.split(":")for val in line.split()]
                for val in inputs:
                    if val[0] == "byr":
                        current.add_byr(val[1])
                    if val[0] == "iyr":
                        current.add_iyr(val[1])
                    if val[0] == "eyr":
                        current.add_eyr(val[1])
                    if val[0] == "hgt":
                        current.add_hgt(val[1])
                    if val[0] == "hcl":
                        current.add_hcl(val[1])
                    if val[0] == "ecl":
                        current.add_ecl(val[1])
                    if val[0] == "pid":
                        current.add_pid(val[1])
            
        return count


print(part_2())
