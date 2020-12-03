
class line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def intersect(self, line1):
        #i1 = [min(self.p1.x, self.p2.x),max(self.p1.x, self.p2.x)]
        #i2 = [min(line1.p1.x, line1.p2.x),max(line1.p1.x, line1.p2.x)]
        
        #iA = [max(min(self.p1.x, self.p2.x),min(line1.p1.x, line1.p2.x)),
        #      min(max(self.p1.x, self.p2.x),max(line1.p1.x, line1.p2.x))]
        
        #if (max(self.p1.x, self.p2.x) < min(line1.p1.x, line1.p2.x)):
        #    return False
        
        x1, x2, x3, x4 = [self.p1.x, self.p2.x, line1.p1.x, line1.p2.x]
        y1, y2, y3, y4 = [self.p1.y, self.p2.y, line1.p1.y, line1.p2.y]
        
        
            
        
        
        return False

    def int_point(self, line1):      
        return None

class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
def new_coord(x, y, direction, steps):
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
    #try:
        with open("input.txt") as f:
            line_1, line_2 = [line.rstrip().split(',') for line in f.readlines()]
            line_1 = [[var[0], int(var[1:])] for var in line_1]
            line_2 = [[var[0], int(var[1:])] for var in line_2]

            x = 0
            y = 0

            points_1 = [point(x,y)]
            points_2 = [point(x,y)]
            
            lines_1 = []
            lines_2 = []
            
            for val in line_1:
                x, y = new_coord(x,y,val[0],val[1])
                
                p = point(x,y)
                
                # Store new line in list
                lines_1.append(line(points_1[-1], p))
                # Store new point in list
                points_1.append(p)
                
            for val in line_2:
                x, y = new_coord(x,y,val[0],val[1])
                
                p = point(x,y)
                
                # Store new line in list
                lines_2.append(line(points_1[-1], p))
                # Store new point in list
                points_2.append(p)
            
            intersects = 0
            
            for line1 in lines_1:
                for line2 in lines_2:
                    if line1.intersect(line2):
                        intersects += 1
            
            return intersects
                
    #except:
    #    print("error")


part_1()
