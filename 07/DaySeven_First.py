mypuzzle = open('./07/myinput.txt', 'r').read().splitlines()

terminal_output = []
path = []

for line in mypuzzle:
    terminal_output = line.split(' ')
    if(terminal_output[1] == 'cd'):
        if(terminal_output[2] == '..'):
            path.pop()
        else:
            path.append(terminal_output[2])
        print(terminal_output)
    elif(terminal_output[1] == 'ls'):
        continue
    else: 
        print(terminal_output[0], terminal_output[1])

print(path)
