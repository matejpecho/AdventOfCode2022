myinput_file = open('./01/myinput.txt', 'r')
inputs = myinput_file.readlines()

max_calories = 0
current_calories = 0
three_elfs = []

def threeElfs(current_calories, three_elfs):
    three_elfs.append(current_calories)
    
for input in inputs:
    if(input != '\n'):
        current_calories += int(input)
        if(input == inputs[-1]):
            threeElfs(current_calories, three_elfs)
            current_calories = 0
    else:
        threeElfs(current_calories, three_elfs)
        current_calories = 0
        
three_elfs.sort(reverse=True)
print(sum(three_elfs[:3]))