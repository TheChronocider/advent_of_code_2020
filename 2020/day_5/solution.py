def part_1():
    with open("input.txt") as f:
        data = f.readlines()

        highestId = 0
        
        for line in data:
            
            lower = 0
            upper = 127
            row = 0
            
            for val in range(7):
                if line[val] == "F":
                    upper -= 128 / (2 ** (val + 1))
                if line[val] == "B":
                    lower += 128 / (2 ** (val + 1))
                if lower == upper:
                    row = lower
            lower = 0
            upper = 7
            col = 0

            for val in range(3):
                if line[val + 7] == "L":
                    upper -= 8 / (2 ** (val + 1))
                if line[val + 7] == "R":
                    lower += 8 / (2 ** (val + 1))
                if lower == upper:
                    col = lower


            calcId = row * 8 + col
            if calcId > highestId:
                highestId = calcId
                
        return highestId

def part_2():
    with open("input.txt") as f:
        data = f.readlines()
        
        lowest = id_calc("FFFFFFFRRR")
        highest = id_calc("BBBBBBBBRRR")

        idList = []
        
        for line in data:
            idList.append(id_calc(line))

        prevID = 27

        print(lowest)
        print(highest)
        
        for val in sorted(idList):
            if val > lowest:
                if val > highest:
                    break
                if (val - prevID) > 1:
                    return val - 1
            prevID = val
                
            
        

def id_calc(code):
    lower = 0
    upper = 127
    row = 0
            
    for val in range(7):
        if code[val] == "F":
            upper -= 128 / (2 ** (val + 1))
        if code[val] == "B":
            lower += 128 / (2 ** (val + 1))
        if lower == upper:
            row = lower
    lower = 0
    upper = 7
    col = 0

    for val in range(3):
        if code[val + 7] == "L":
            upper -= 8 / (2 ** (val + 1))
        if code[val + 7] == "R":
            lower += 8 / (2 ** (val + 1))
        if lower == upper:
            col = lower


    return row * 8 + col

print(part_2())
