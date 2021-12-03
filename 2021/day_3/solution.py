def part_1():
    file = open('input.txt','r')

    data = [[char for char in line.rstrip('\n')] for line in file.readlines()]

    gamma = ""
    epsilon = ""
    
    for x in range(len(data[0])):
        
        char = 0
        
        for y in range(len(data)):
            if data[y][x] == '0':
                char -= 1
            else:
                char += 1
                
        if char > 0:
            gamma = gamma + '1'
            epsilon = epsilon + '0'
        else:
            gamma = gamma + '0'
            epsilon = epsilon + '1'

    return int(gamma, 2) * int(epsilon, 2)

def filter_list_by_bit_position(data, bit, position):
    filtered = []

    for line in data:
        if line[position] == bit:
            filtered.append(line)

    return filtered
         

def part_2():
    file = open('input.txt','r')

    data = [line.rstrip() for line in file.readlines()]

    oxygen = find_oxygen(data)
    co2 = find_co2(data)

    return int(oxygen, 2) * int(co2, 2)

def find_oxygen(data):
    
    oxygen = ""
    
    for x in range(len(data[0])):
        count = 0

        for y in range(len(data)):
            if data[y][x] == '0':
                count -= 1
            else:
                count += 1
                
        bit = '1' if count >= 0 else '0'

        oxygen = oxygen + bit

        filtered = []
        for y in range(len(data)):
            if data[y][x] == bit:
                filtered.append(data[y])

        data = filtered
        
    return oxygen

def find_co2(data):
    
    co2 = ""
    
    for x in range(len(data[0])):
        count = 0

        for y in range(len(data)):
            if data[y][x] == '0':
                count -= 1
            else:
                count += 1
                
        bit = '0' if count >= 0 else '1'
        co2 = co2 + bit

        filtered = []

        for y in range(len(data)):
            if data[y][x] == bit:
                filtered.append(data[y])

        data = filtered

        if len(data) == 1:
            co2 = data[0]
            break

    return co2

#print(part_1())
print(part_2())
