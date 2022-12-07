myinput_file = open('./02/myinput.txt', 'r')
inputs = myinput_file.readlines()
elf = ''
me = ''
my_score = 0

def score(elf,me): 
    match elf:
        case 'A': #rock
            if(me == 'X'): #loose scisors
                return 3
            if(me == 'Y'): #draw rock
                return 4
            if(me == 'Z'): #win paper
                return 8   
        case 'B': #paper
            if(me == 'X'): #loose rock
                return 1
            if(me == 'Y'): #draw paper
                return 5
            if(me == 'Z'): #win scisors
                return 9   
        case 'C': #scisors
            if(me == 'X'): #loose paper
                return 2
            if(me == 'Y'): #draw scisors
                return 6
            if(me == 'Z'): #win rock
                return 7
    
for input in inputs:
    elf = input[0]
    me = input[2]
    my_score += score(elf,me)
    #print(score(elf, me))
    
print(my_score)