# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 14:16:43 2020

@author: Zane Rogalewicz
"""

import math

def part_1():
    with open('input.txt') as f:
        data = f.readlines()
        
        ans = 0
        
        for val in data:
            try:
                #print(val)
                result = int(math.floor(float(val) / 3.0) - 2.0)
                #print (result)
                ans += result
            except:
                print('error')
        f.close()
        return (ans)
    return 0

def part_2():
    with open('input.txt') as f:
        data = f.readlines()
        
        ans = 0
        
        for val in data:
            try:
                result = int(math.floor(float(val) / 3.0) - 2.0)
                ans += part_2_a(result)
            except:
                print('error')
        f.close()
        return (ans)
    return 0
    
def part_2_a(fuel_req):
    
    if fuel_req <= 0:
        return 0
    ans = int(math.floor(float(fuel_req) / 3.0) - 2.0)
    
    return fuel_req + part_2_a(ans)
        

print(part_2())
    
