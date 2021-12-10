import statistics

def solution ():
    with open('input.txt') as f:

        data = [line.rstrip() for line in f.readlines()]

        open_sym = "([{<"
        close_sym = ")]}>"
        corrupt_score_list = [3,57,1197,25137]
        close_score_list = [1,2,3,4]
        
        corrupt_score = 0
        close_score = []

        for line in data:            
            last_char = []

            corrupt = False
            
            while not(corrupt) and len(line) > 0:
                char, line = line[0], line[1:]
                
                if last_char == []:
                    if char in close_sym:
                        corrupt_score += corrupt_score_list[close_sym.index(char)]
                        corrupt = True
                    else:
                        last_char = [char]
                else:
                    if (char in close_sym):
                        if char == close_sym[open_sym.index(last_char[-1])]:
                            last_char.pop()
                        else:
                            corrupt_score += corrupt_score_list[close_sym.index(char)]
                            corrupt = True
                    else:
                        last_char.append(char)

            if not(corrupt):
                score = 0
                while not(corrupt) and len(last_char) > 0:
                    char, last_char = last_char[-1], last_char[:-1]
                    score = (score * 5) + close_score_list[open_sym.index(char)]

                close_score.append(score)
                    

            
        
        print(corrupt_score)
        print(statistics.median(close_score))

        

solution()
                            
  
