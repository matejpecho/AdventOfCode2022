mypuzzle = open('./08/myinput.txt', 'r').read().splitlines()

grid = []
count = 0

left = True
right = True
up = True
down = True

for line in mypuzzle:
    grid.append(list(map(int,line)))


left_score = 0
right_score = 0
up_score = 0
down_score = 0

for r in range(len(grid)):
    for c in range(len(grid[r])):
        print(grid[r][c])
        for item in range(c-1, -1, -1):
            left_score += 1
            if(grid[r][item] >= grid[r][c]):
                
                left = False
                break
            left = True
            
        for item in range(c + 1, len(grid[r])):
            right_score += 1
            if(grid[r][item] >= grid[r][c]):
                right = False
                break
            right = True
        print(right_score)

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
        right_score = 0
        up_score = 0
        down_score = 0
 
print(count)