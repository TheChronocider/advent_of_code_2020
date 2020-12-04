# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 13:22:26 2020

@author: Zane Rogalewicz
"""

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    # Manhattan distance from origin
    def manhattan_dist(self):
        return abs(x) + abs(y)
    

class Line:
    
    # A line between two points
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        
        self.horizontal = (p1.x == p2.x)
    
    # Get intersections with another line
    def get_intersections(self, line1):
        # Line either horizontal or vertical
        # Line either intersects once or multiple times
        
        # Getting x and y values stored as simple variables
        x1, x2, x3, x4 = [self.p1.x, self.p2.x, line1.p1.x, line1.p2.x]
        y1, y2, y3, y4 = [self.p1.y, self.p2.y, line1.p1.y, line1.p2.y]
        
        if self.horizontal and not line1.horizontal:
            if y1 <= max(y3, y4) and y1 >= min(y3, y4) and x3 <= max(x1,x2) and x3 >= min(x1, x2):
                return x3, y1
        elif line1.horizontal and not self.horizontal:
            if x1 <= max(x3, x4) and x1 >= min(y3,y4) and y3 <= max(y1, y2) and y3 >= min(y1, y2):
                return x1, y3
        
        
        
        return None
    
    def print_line(self):
        print(self.p1.x, self.p1.y, self.p2.x, self.p2.y)
        
    
def inc_position(x, y, direction, steps):
    if direction == "R":
        x += steps
    elif direction == "L":
        x -= steps
    elif direction == "U":
        y += steps
    elif direction == "D":
        y -= steps

    return x, y
        

def part_1():
    # Opening file
    with open("input.txt") as f:
        # Create list of inputs:
        # lines = [line]
        # line = [val]
        # val = [direction, steps]
        data = [[[val[0], int(val[1:])] 
                  for val in line.rstrip().split(',')] 
                     for line in f.readlines()]
        
        # A 2D array collection of lines
        lines = []
        
        # Iterate through all values
        for line in data:
            # Reset coords to centre
            x = 0
            y = 0
            
            # Define prev point, being origin in this case
            prevPoint = Point(x,y)
            
            newLines = []
            
            for point in line:
                x,y = inc_position(x,y,point[0], point[1])
                
                newPoint = Point(x,y)
                
                newLines.append(Line(prevPoint, newPoint))
                
                prevPoint = newPoint
            
            lines.append(newLines)
            
        
        intersects = set()
        
        for line1 in lines[0]:
            for line2 in lines[1]:
                intersect = line1.get_intersections(line2)
                
                if not(intersect == None):
                    print("intersect:", intersect)
                    print("Line 1:")
                    print (line1.p1.x, line1.p1.y)
                    print (line1.p2.x, line1.p2.y)
                    print("Line 2:")
                    print (line2.p1.x, line2.p1.y)
                    print (line2.p2.x, line2.p2.y)
                    intersects.add(intersect)
        
        #print(sorted(intersects))
        return sum(1 for coord in intersects)
                
        

print(part_1())