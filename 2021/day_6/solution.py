def part_1(days):
    with open('input.txt') as f:
        data = [int(value) for value in f.readline().split(',')]

        f.close()

        for i in range(days):
            length = len(data)

            for j in range(length):
                if data[j] == 0:
                    data[j] = 6
                    data.append(8)

                else:
                    data[j] -= 1

        return len(data)


# Idea is that this is more efficient
def part_1_recursive(days):
    with open('input.txt') as f:
        data = [int(value) for value in f.readline().split(',')]

        f.close()

        fish_count = len(data)
        
        for fish in data:
            fish_count += part_2_loop(days - fish)

        return fish_count

def part_1_loop(days):
    if days <= 0:
        return 0

    return 1 + part_2_loop(days - 7) + part_2_loop(days - 9)


def part_2(days):
    with open('input.txt') as f:
        data = [int(value) for value in f.readline().split(',')]

        fish = [data.count(i) for i in range(9)]

        f.close()
        
        for i in range(days):
            num = fish.pop(0)

            fish[6] += num

            fish.append(num)

            assert len(fish) == 9

        return sum(fish)
    
    

#print(part_1(80))
print(part_2(256))


