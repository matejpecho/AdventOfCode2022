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
left_score = 0
for r in range(len(grid)):
    for c in range(len(grid[r])):
        print(grid[r][c])
        for item in range(c-1, -1, -1):
            left_score += 1
            if(grid[r][item] >= grid[r][c]):
                print(left_score)
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
        left_score = 0
 
print(count)