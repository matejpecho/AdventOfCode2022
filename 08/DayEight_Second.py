mypuzzle = open('./08/myinput.txt', 'r').read().splitlines()

grid = []

for line in mypuzzle:
    grid.append(list(map(int,line)))

left_score = 0
right_score = 0
up_score = 0
down_score = 0
full_score = 0

for r in range(len(grid)):
    for c in range(len(grid[r])):
        #print(grid[r][c])

        for item in range(c-1, -1, -1):
            left_score += 1
            if(grid[r][item] >= grid[r][c]):
                break

        for item in range(c + 1, len(grid[r])):
            right_score += 1
            if(grid[r][item] >= grid[r][c]):
                break

        for item in range(r-1, -1, -1):
            up_score += 1
            if(grid[item][c] >= grid[r][c]):
                break
            
        for item in range(r + 1, len(grid[r])):
            down_score += 1
            if(grid[item][c] >= grid[r][c]):
                break
                
        if(r == 0 or c == 0 or r == len(grid)-1 or c == len(grid[r]) - 1):
            #print('edge')
            left_score = 0
        if(full_score < (left_score * right_score * up_score * down_score)):
            full_score = left_score * right_score * up_score * down_score

        left_score = 0
        right_score = 0
        up_score = 0
        down_score = 0
 
print(full_score)