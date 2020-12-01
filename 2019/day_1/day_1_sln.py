# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 14:16:43 2020

@author: Zane Rogalewicz
"""

import math

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
    print (ans)
    f.close()
    
