"""
Created on Weds Dec  1 16:00 2021

@author: Zane Rogalewicz
"""
def part_1():
    with open('input.txt') as f:
        data = f.readlines()

        depth = -1

        count = 0
        
        for x in range(len(data)):
            try:
                if (int(data[x]) > depth):
                    count += 1
                    
                depth = int(data[x])
            except:
                print("error")

        return count

def part_2():
    with open('input.txt') as f:
        data = f.readlines()

        depth = -1

        count = -1
        
        for x in range(len(data) - 2):
            try:
                window = int(data[x]) + int(data[x+1]) + int(data[x+2])
                print(window)
                
                if (window > depth):
                    count += 1
                    
                depth = window
            except:
                print("error")

        return count


print(part_2())
