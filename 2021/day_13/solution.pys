# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 08:05:12 2021

@author: Zane Rogalewicz
"""
import numpy as np

def solution():
    with open('input.txt') as f:
        
        line = f.readline()
        
        matrix = np.zeros((9999, 9999), bool)
        
        while not(line == '\n'):
            x, y = [int(val) for val in line.strip().split(',')]
            
            matrix[y,x] = True
            
            line = f.readline()
        
        line = f.readline()
        
        while line:
            axis, val = line.strip().split()[2].split('=')
            val = int(val)
            
            if axis == 'x':
                matrix = matrix[:,:val] | matrix[:,2*val:val:-1]
            
            if axis == 'y':
                matrix = matrix[:val,:]|matrix[2*val:val:-1,:]
            
            print(matrix.sum())
            line = f.readline()
        
        print(np.array2string(matrix, separator='',formatter={'bool':{0:' ',1:'#'}.get}))
            
            
solution()
            
