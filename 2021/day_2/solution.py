def part_1():
    with open("input.txt") as f:
        
        data = f.readlines()
        
        x = 0
        y = 0
        
        for line in data:
            direction, distance = line.split() # [value1, value2]

            try:
                if direction == "forward":
                    x += int(distance)
                elif direction == "down":
                    y += int(distance)
                elif direction == "up":
                    y -= int(distance)
            except:
                print("error")

        return x * y

        f.close()

def part_2():
    with open("input.txt") as f:
        
        data = f.readlines()
        
        x = 0
        y = 0
        z = 0
        
        for line in data:
            direction, distance = line.split()

            try:
                if direction == "forward":
                    x += int(distance)
                    y += int(distance) * z
                elif direction == "down":
                    z += int(distance)
                elif direction == "up":
                    z -= int(distance)
            except:
                print("error")

        return x * y

        f.close()
        
            
print (part_1())
print (part_2())
