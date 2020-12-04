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
    
    # Get intersections with another line
    def get_intersections(self, line1):
        # Line either horizontal or vertical
        # Line either intersects once or multiple times
        
        xdiff = (self.p1.x - self.p2.x, line1.p1.x - line1.p2.x)
        ydiff = (self.p1.y - self.p2.y, line1.p1.y - line1.p2.y)
        
        
        def det(a, b):
            return a[0] * b[1] - a[1] * b[0]
        
        div = det(xdiff, ydiff)
        
        if div == 0:
            return None
        
        
        d = (det(*[[self.p1.x, self.p1.y],[self.p2.x, self.p2.y]]),
             det(*[[line1.p1.x, line1.p1.y],[line1.p2.x, line1.p2.y]]))
        
        x = det(d, xdiff) / div
        y = det(d, ydiff) / div
        
        return x,y
        
    
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
                    intersects.add(intersect)
        
        print(sorted(intersects))
        return sum(1 for coord in intersects)
                
        

print(part_1())