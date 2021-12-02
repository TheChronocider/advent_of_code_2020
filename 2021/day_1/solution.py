"""
Created on Weds Dec  1 16:00 2021

@author: Zane Rogalewicz
"""
def part_1():
    with open('input.txt') as f:
        data = f.readlines()
        
        count = 0
        
        for x in range(1, len(data)): # start at x = 1
            try:
                if (int(data[x]) > int(data[x-1])):
                    count += 1
            except:
                print("error")

        return count

def part_2():
    with open('input.txt') as f:
        data = f.readlines()

        # depth startomg point
        depth = -1
        
        # Initialising count for return
        count = 0
        
        for x in range(len(data) - 2):
            try:
                # Initialising window for this loop
                window = int(data[x]) + int(data[x+1]) + int(data[x+2])
                
                if depth > 0:
                    if (window > depth):
                        count += 1
                    
                depth = window
            except:
                print("error")

        return count

# Displaying solutions
print("Part 1:", part_1())
print("Part 2:", part_2())
