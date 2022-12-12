mypuzzle = open('./08/myinput.txt', 'r').read().splitlines()

grid = []
count = 0

left = True
right = True
up = True
down = True

for line in mypuzzle:
    grid.append(list(map(int,line)))

'''
Future update: two function for row and columns
def visibleDirection(start, end, r, c):
    visible = True
    for item in range(start, end):
        if(grid[r][item] >= grid[r][c]):
            visible = False
            break
        visible = True
    return visible'''

for r in range(len(grid)):
    for c in range(len(grid[r])):

        for item in range(0, c):
            if(grid[r][item] >= grid[r][c]):
                left = False
                break
            left = True
            
        for item in range(c + 1, len(grid[r])):
            if(grid[r][item] >= grid[r][c]):
                right = False
                break
            right = True
            
        for item in range(0, r):
            if(grid[item][c] >= grid[r][c]):
                up = False
                break
            up = True
            
        for item in range(r + 1, len(grid[r])):
            if(grid[item][c] >= grid[r][c]):
                down = False
                break
            down = True
                
        if(left or right or up or down):
            #print('item true: ' + str(grid[r][c]))
            count += 1
        left = True
        right = True
        up = True
        down = True
 
print(count)