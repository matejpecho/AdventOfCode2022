myinput_file = open('./03/myinput.txt', 'r')
input = myinput_file.readlines()
abeced = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
common_items = []

for line in input:
    first_compar = []
    second_compar = []
    half = int(len(line)/2)
    first_compar[:0] = (line[:half])
    second_compar[:0] = (line[half:len(line)])
    common_items.append(abeced.index(list(set(first_compar).intersection(second_compar))[0]) + 1)

print(sum(common_items))