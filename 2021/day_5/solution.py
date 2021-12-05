def part_1():
    with open('input.txt') as f:
        data = f.readlines()

        matrix = {}

        dangerousCount = 0

        for line in data:
            start, end = [[int(coord) for coord in point.rstrip().lstrip().split(',')] for point in line.split('->')]

            if start[0] == end[0] or start[1] == end[1]:

                for x,y in get_line(start,end):
                    key = str(x) + ',' + str(y)

                    if key in matrix:
                        matrix[key] += 1

                        if matrix[key] == 2:
                            dangerousCount += 1
                    else:
                        matrix[key] = 1
                        
        return dangerousCount

def part_2():
    with open('input.txt') as f:
        data = f.readlines()

        matrix = {}

        dangerousCount = 0

        for line in data:
            start, end = [[int(coord) for coord in point.rstrip().lstrip().split(',')] for point in line.split('->')]

            for x,y in get_line(start,end):
                key = str(x) + ',' + str(y)

                if key in matrix:
                    matrix[key] += 1

                    if matrix[key] == 2:
                        dangerousCount += 1
                else:
                    matrix[key] = 1
                        
        return dangerousCount


# user1048839 - stackexchange
def get_line(start, end):
    x1, y1 = start
    x2, y2 = end
    
    points = []

    issteep = abs(y1 - y2) > abs(x1 - x2)

    if issteep:
        x1, y1 = y1, x1
        x2, y2 = y2, x2

    rev = False

    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1
        
        rev = True

    deltax = x2 - x1

    deltay = abs(y2 - y1)

    error = int(deltax /2)

    y = y1

    ystep = None
    if y1 < y2:
        ystep = 1
    else:
        ystep = -1

    for x in range(x1, x2 + 1):
        if issteep:
            points.append((y,x))
        else:
            points.append((x,y))
        error -= deltay
        if error < 0:
            y += ystep
            error += deltax

    # if Coords were reversed
    if rev:
        points.reverse()

    return points

print(part_1())
print(part_2())
