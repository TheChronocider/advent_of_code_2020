from numpy import *

def part_1():
    with open("input.txt") as f:
        data = [int(number) for number in f.readline().split(',')]

        return int(sum(abs(data-median(data))))


def part_2():
    with open("input.txt") as f:
        data = [int(number) for number in f.readline().split(',')]

        fuel_consumption = lambda d: d*(d+1)/2



        return int(min(sum(fuel_consumption(abs(data - floor(mean(data))))),
          sum(fuel_consumption(abs(data - ceil(mean(data)))))))

        
    



def part_1_orig():
    with open("input.txt") as f:
        data = [int(number) for number in f.readline().split(',')]

        return int(min_cost(data))

        
def min_cost(data):
    
    cost = 0
    
    length = len(data)

    data.sort()    

    mid = data[int(length/2)]

    for value in data:
        cost = cost + abs(value - mid)

    
    if length % 2 == 0:
        even_cost = 0

        mid = data[int(length/2) -1]

        for value in data:
            even_cost = even_cost + abs(value - mid)

        cost = min(cost, even_cost)

    return cost

    



print(part_1_orig())
print(part_2())
