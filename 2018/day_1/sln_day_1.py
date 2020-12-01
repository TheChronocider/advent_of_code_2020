def part_1():
    with open("input.txt") as f:
        lines = f.readlines()

        freqSum = 0
        
        for line in lines:
            try:
                freqSum += int(line)
            except:
                print("error")
        return freqSum

def part_2():
    with open("input.txt") as f:
        values = {''}

        sumFreq = 0

        i = 0

        lines = f.readlines()
        
        while not(sumFreq in values):            
            values.add(sumFreq)
            
            sumFreq += int(lines[i%len(lines)])
            
            i += 1
        return sumFreq
    return -1

print(part_2())
