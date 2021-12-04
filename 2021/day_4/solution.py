def part_1():
    with open('input.txt') as f:
        data = f.readlines()

        number_order = [char.rstrip() for char in data.pop(0).split(',')]

        boards = parse_boards(data)

        
        min_moves = 99999999
        score = 0

        for board in boards:
            moves = 0

            for x in range(len(number_order)):
                numbers = number_order[0:x + 1]

                if evaluate_board(board, numbers):
                    if x < min_moves:
                        min_moves = x
                        
                        score = int(number_order[x]) * sum_unmarked(board,numbers)
                    
                    break
                    
                

        return score

def sum_unmarked(board, numbers):
    count = 0

    for line in board:
        for char in line:
            if char not in numbers:
                count += int(char)
    return count
        
def evaluate_board(board, numbers):
    for line in board:
        if set(line) <= set(numbers):
            return True

    for x in range(len(board[0])):
        column = [line[x] for line in board]
        if set(column) <= set(numbers):
            return True
        
    return False
            
        
# Parse boards into arrays
def parse_boards (data):
    boards = []
    board = []
    
    for line in data:
        if line == '\n':
            if board:
                boards.append(board)
                
            board = []

        else:
            board.append([char.rstrip() for char in line.split()])

    # Add final board
    boards.append(board)

    return boards

def part_2():
    with open('input.txt') as f:
        data = f.readlines()

        number_order = [char.rstrip() for char in data.pop(0).split(',')]

        boards = parse_boards(data)

        
        max_moves = 0
        score = 0

        for board in boards:
            moves = 0

            for x in range(len(number_order)):
                numbers = number_order[0:x + 1]

                if evaluate_board(board, numbers):
                    if x > max_moves:
                        max_moves = x
                        
                        score = int(number_order[x]) * sum_unmarked(board,numbers)
                    
                    break
                    
                

        return score

            
            


print(part_2())
