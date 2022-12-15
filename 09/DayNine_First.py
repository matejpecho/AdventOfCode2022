mypuzzle = open('./09/myinput.txt', 'r').read().splitlines()

H = [0,0]
T = [0,0]

#def touching(head, tail):


for line in mypuzzle:
    navigation = line.split(' ')
    direction = navigation[0]
    distance = int(navigation[1])
    if(direction == 'R'):
        H[1] += distance
        T[1] += distance - 1
    print(H)
    print(T)