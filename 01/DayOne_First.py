myinput_file = open('./01/myinput.txt', 'r')
inputs = myinput_file.readlines()

max_calories = 0
current_calories = 0

for input in inputs:
    if(input == '\n'):
        if(current_calories > max_calories):
            max_calories = current_calories
        current_calories = 0
    else:
        current_calories += int(input)

print(max_calories)