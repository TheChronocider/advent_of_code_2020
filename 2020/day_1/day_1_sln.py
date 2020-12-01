# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 15:55:41 2020

@author: Zane Rogalewicz
"""

def part_1():
    with open('input.txt') as f:
        data = f.readlines()
        
        for x in range(len(data)):
            for y in range(len(data) - x):
                try:
                    a = int(data[x])
                    b = int(data[x + y])
                    
                    if (a + b) == 2020:
                        return (a * b)
                except:
                    print("error")
                    
def part_2():
    with open('input.txt') as f:
        data = f.readlines()
        
        for x in range(len(data)):
            for y in range(len(data) - x):
                for z in range(len(data) - x - y):
                    try:
                        a = int(data[x])
                        b = int(data[x + y])
                        c = int(data[x + y + z])
                        
                        if (a + b + c) == 2020:
                            return (a * b * c)
                    except:
                        print("error")      
                        
print(part_2())
                    