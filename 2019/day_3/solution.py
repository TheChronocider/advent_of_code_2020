class line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def intersect(self, line1):
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
                
                points_1 = points_1 ++ [p]
                
    #except:
    #    print("error")


part_1()
