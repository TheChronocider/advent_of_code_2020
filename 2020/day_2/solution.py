def part_1():
    with open("input.txt") as f:
        data = f.readlines() # Get each line. We'll split further

        valid = 0
        
        for entry in data:
            # Split into format: amount (1-5), letter (a:), password (aaaa)
            amount, letter, password = entry.split()
            
            # First: Split the list based on the - delimiter
            # Second: Map the resulting list into ints
            # Third: Turn the map object into a list object
            amount = list(map(int, amount.split('-')))

            # Remove the colon from the letter
            letter = letter.strip(':')

            # Keep track of the number of instances
            count = 0

            # For each letter in password, check amount of letter in
            for val in password:
                if val == letter:
                    count += 1
                        
            if count >= amount[0] and count <= amount[1]:
                valid += 1
                
        return valid

def part_2():
    with open("input.txt") as f:
        data = f.readlines() # Get each line. We'll split further

        valid = 0
        
        for entry in data:
            # Split into format: amount (1-5), letter (a:), password (aaaa)
            positions, letter, password = entry.split()
            
            # First: Split the list based on the - delimiter
            # Second: Map the resulting list into ints
            # Third: Turn the map object into a list object
            positions = list(map(int, positions.split('-')))

            # Remove the colon from the letter
            letter = letter.strip(':')

            # Keep track of the number of instances
            count = 0

            # Check positions for whether the letter matches
            if password[positions[0]-1] == letter:
                count += 1
            if password[positions[1]-1] == letter:
                count += 1

            # Only one instance can match
            if count == 1:
                valid += 1
                
        return valid

print(part_2())
