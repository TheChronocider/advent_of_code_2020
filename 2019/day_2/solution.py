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

def part_2_b(data, noun, verb):
        i = 0

        #Updated variables
        data[1] = noun
        data[2] = verb
        
        while not(data[i] == 99) and i < len(data):
            opcode = data[i]
            a = data[i+1]
            b = data[i+2]
            z = data[i+3]

            if opcode == 1:
                data[z] = data[a] + data[b]
            if opcode == 2:
                data[z] = data[a] * data[b]
            
            i+=4
        return data[0]

def part_2_a(ans):
    with open("input.txt") as f:
        # Get the list of values
        data = [int(val) for val in f.read().split(',')]

        for x in range(100):
            for y in range(100):
                if part_2_b(list(data), x, y) == ans:
                    return 100 * x + y
    return -1

print(part_2_a(19690720))
