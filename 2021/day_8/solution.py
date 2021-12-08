
def process_data():
    with open('input.txt')  as f:
        data = f.readlines()
        
        for line in data:
            signal, output = [val.split() for val in line.split('|')]
            
            value = ''
            
            l = {len(s) : set(s) for s in signal}
            
            for o in map(set, output):
                match len(o), len(o&k[4]), len(o&l[2]):
                    case 2,_,_: value += '1'
                    case 3,_,_: value += '7'
                    case 4,_,_: value += '4'
                    case 7,_,_: value += '8'
                    case 5,2,_: value += '2'
                    case 5,3,1: value += '5'
                    case 5,3,2: value += '3'
                    case 6,4,_: value += '9'
                    case 6,3,1: value += '6'
                    case 6,3,2: value += '0'
                
            
            
        f.close()
        
        return count



print(process_data())
