myinput_file = open('./02/myinput.txt', 'r')
inputs = myinput_file.readlines()
elf = ''
me = ''
my_score = 0

def score(elf,me): 
    match me:
        case 'X': #rock
            if(elf == 'A'): #rock
                return 4
            if(elf == 'C'): #scisors
                return 7    
            return 1   
        case 'Y': #paper
            if(elf == 'B'): #paper
                return 5
            if(elf == 'A'): #rock
                return 8
            return 2
        case 'Z': #scisors
            if(elf == 'B'): #paper
                return 9 
            if(elf == 'C'): #scisors
                return 6
            return 3
    
for input in inputs:
    elf = input[0]
    me = input[2]
    my_score += score(elf,me)
    #print(score(elf, me))
    
print(my_score)