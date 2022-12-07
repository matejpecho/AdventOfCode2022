myinput_file = open('./04/myinput.txt', 'r').read().splitlines()
count = 0

for input in myinput_file:
    sections = input.split(',')
    first_section = sections[0].split('-')
    second_section = sections[1].split('-')

    left = (int(first_section[0]) - int(second_section[0]))
    right = (int(first_section[1]) - int(second_section[1]))
    
    if((left <= 0 and right >= 0) or (left >=0 and right <= 0)):
        count += 1

print(count)