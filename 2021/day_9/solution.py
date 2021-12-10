class Point:
    lower = None
    
    def __init__(self, value):
        self.value = value

    def set_lower(self, point):
        self.lower = point

    def get_val(self):
        return self.val

    def get_lower(self):
        return self.get_points() if lower == None else self.lower.get_points()


def solution ():
    with open('input.txt') as f:
        data = [[Point(int(val)) for val in line.rstrip()] for line in f.readlines()]

        lower_sum = 0
        
        for y in range(len(data)):
            for x in range(len(data[y])):
                if y > 0 and data[y][x].value > data[y-1][x].value:
                    data[y][x].set_lower(data[y-1][x])
                elif y < (len(data)-1) and data[y][x].value > data[y+1][x].value:
                    data[y][x].set_lower(data[y+1][x])
                elif x > 0 and data[y][x].value > data[y][x-1].value:
                    data[y][x].set_lower(data[y][x-1])
                elif x < (len(data[y])-1) and data[y][x].value > data[y][x+1].value:
                    data[y][x].set_lower(data[y][x+1])
                else:
                    lower_sum += data[y][x].value + 1
                    
        return lower_sum         
                

#Stolen from reddit. I screwed up my implementation, might go back again.
from math import prod

height = {(x,y):int(h) for y,l in enumerate(open("input.txt"))
                       for x,h in enumerate(l.strip())}

def neighbours(x, y):
  return filter(lambda n: n in height,  # remove points
    [(x,y-1),(x,y+1),(x-1,y),(x+1,y)])  #  outside grid

def is_low(p):
  return all(height[p] < height[n]
    for n in neighbours(*p))

low_points = list(filter(is_low, height))
print(sum(height[p]+1 for p in low_points))

def count_basin(p):
  if height[p] == 9: return 0  # stop counting at ridge
  del height[p]                # prevent further visits
  return 1+sum(map(count_basin, neighbours(*p)))

basins = [count_basin(p) for p in low_points]
print(prod(sorted(basins)[-3:]))
