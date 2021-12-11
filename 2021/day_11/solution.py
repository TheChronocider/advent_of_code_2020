from numpy import *
from copy import *

def solution():
    with open('input.txt') as f:

        # Reading each input as an integer
        data = [[int(val) for val in line.rstrip()] for line in f.readlines()]

        flash_count =0
        step = 100
        
        display_data(data)
        
        for i in range(step):
            prev = list(map(list, data))
            for y in range(len(data)):
                for x in range(len(data[y])):
                    data, flash_inc = flash(prev, data, x, y)
                    flash_count += flash_inc


            #display_data(data)
                    
        data_sum = -1
        
        while not(data_sum == 0):
            prev = list(map(list, data))
            for y in range(len(data)):
                for x in range(len(data[y])):
                    data, flash_inc = flash(prev, data, x, y)
            display_data(data)

            data_sum = sum([sum(line) for line in data])
            step += 1
            
                
            

        print(flash_count)

        print(step)

        
def display_data(data):
    for line in data:
        data_print = ""
        for val in line:
            data_print += str(val)

        print(data_print)

    print('')
            
def flash(prev, data, px, py):
    
    flash_count = 0
    
    if (data[py][px] < 9 and data[py][px] > 0) or prev[py][px] == 0:
        data[py][px] += 1
    elif data[py][px] == 9:    
        x1 = px if px <= 0 else px-1
        x2 = px+1 if px >= len(data[0]) -1 else px+2
        y1 = py if py <= 0 else py-1
        y2 = py+1 if py >= len(data)-1 else py+2
        flash_count += 1

        data[py][px] = 0

        for y in range(y1, y2):
            for x in range(x1, x2):
                if data[y][x] > 0 or prev[y][x] == 0:
                    data, flash_inc = flash(prev, data, x, y)
                    flash_count += flash_inc
                #elif data[y][x] > 0:
                #    data[y][x] += 1
                    

    return data, flash_count

        

solution()
                            
  
