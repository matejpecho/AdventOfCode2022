myinput_file = open('./06/myinput.txt', 'r').read().splitlines()
my_marker = []
count = 0
same_letter = False

marker_mask = 4 # First
#marker_mask = 19 # Second

for letter in myinput_file[0]:
    if(len(my_marker) == marker_mask):
        for item in my_marker:
            if(my_marker.count(item) > 1):
                same_letter = True
                break
            else:
                same_letter = False
        if(same_letter):
            my_marker.pop(0)
            #print(my_marker)
            my_marker.append(letter)
        else:
            break
    else:
        my_marker.append(letter)
    count += 1

print(count)
print(my_marker)