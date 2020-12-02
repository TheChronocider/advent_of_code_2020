# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 09:05:25 2020

@author: Zane Rogalewicz
"""

def part_1():
    with open("input.txt") as f:
        data = f.read().split(',')
        
        i = 0 # Index
        
        while i < len(data):
            if int(data[i]) == 99:
                break
            
            opcode = int(data[i])
            loc_1 = int(data[i+1])
            loc_2 = int(data[i+2])
            loc_ans = int(data[i+3])
            
            if opcode == 1:
                data[loc_ans] = int(data[loc_1]) + int(data[loc_2])
            elif opcode == 2:
                data[loc_ans] = int(data[loc_1]) * int(data[loc_2])
            else:
                print ("error")
            i += 4
        return int(data[0])

def part_2_a(noun, verb):
    with open("input.txt") as f:
        data = f.read().split(',')
        
        data[1] = noun
        data[2] = verb
        
        i = 0 # Index
        
        while i < len(data):
            if int(data[i]) == 99:
                break
            
            opcode = int(data[i])
            loc_1 = int(data[i+1])
            loc_2 = int(data[i+2])
            loc_ans = int(data[i+3])
            
            if opcode == 1:
                data[loc_ans] = int(data[loc_1]) + int(data[loc_2])
            elif opcode == 2:
                data[loc_ans] = int(data[loc_1]) * int(data[loc_2])
            else:
                print ("error")
            i += 4
        return int(data[0])

def part_2_b(ans):
    for x in range(100):
    #x = 77
        for y in range(100):
            val = part_2_a(x,y)
            if val == ans:
                return (100*x * y)
            if val > ans:
                break
    return -1

print(part_2_b(19690720))