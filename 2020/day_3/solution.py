def part_1():
    with open("input.txt") as f:
        array = [line.rstrip() for line in f.readlines()]

        # toboggan travel right 3, down 1
        x = 0
        y = 0

        treeCount = 0
        
        while y < len(array):

            if array[y][x%len(array[y])] == "#":
                treeCount += 1

            x += 3
            y += 1
        return treeCount

def part_2_a():
    with open("input.txt") as f:
        data = [line.rstrip() for line in f.readlines()]
        slopes = [[1,1],[3,1],[5,1],[7,1],[1,2]]

        combin = 1
        
        for slope in slopes:
            combin *= part_2_b(list(data),slope[0],slope[1])
            
        return combin
        
def part_2_b(data, xInc, yInc):
        x = 0
        y = 0

        treeCount = 0
        
        while y < len(data):

            if data[y][x%len(data[y])] == "#":
                treeCount += 1

            x += xInc
            y += yInc
        return treeCount
    

print(part_2_a())
