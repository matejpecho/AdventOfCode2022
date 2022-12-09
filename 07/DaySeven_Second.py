mypuzzle = open('./07/myinput.txt', 'r').read().splitlines()

terminal_output = []
whole_path = []
path = []
current_dir_size = 0

for line in mypuzzle:
    terminal_output = line.split(' ')

    if (terminal_output[0] == '$'):
        if (terminal_output[1] == 'cd'):
            if (terminal_output[2] == '..'):
                whole_path.append(path[-1])
                path.pop()
            else:

                current_dir_size = 0
                path.append([])
                path[-1].append(terminal_output[2])
                #path.append(terminal_output[2])

        elif (terminal_output[0] == 'ls'):
            continue
    else:
        if (terminal_output[0] == "dir"):
            continue

        current_dir_size += int(terminal_output[0])

        if (len(path) > 0):
            # print(whole_path[0])
            #print('\n')
            for dir in path:

                if(len(dir) > 1):
                    dir[1] = dir[1] + current_dir_size
                else:
                    dir.append(current_dir_size)
                    
                #print(path)
                #print(dir)
                #print('----------------------------')
        current_dir_size = 0
        #print(path)


print('\nResult:')   
#print(path)
for a in path:
    whole_path.append(a)
#print(whole_path)

size = 0
used_space = 0

for b in whole_path:
    if(b[0] == '/'):
        used_space = b[1]
    if(b[1] < 100000):
        size += b[1]
#   print(size)
to_free_up = 30000000 - (70000000 - used_space)

smallest_to_remove = []

for c in whole_path:
    if(c[1] >= to_free_up):
        smallest_to_remove.append(c[1])
print(min(smallest_to_remove))
    #print(terminal_output)
