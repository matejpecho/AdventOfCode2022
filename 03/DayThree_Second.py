myinput_file = open('./03/myinput.txt', 'r')
input = myinput_file.readlines()
abeced = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
common_items = []
elf_group = []

for line in input:
    elf_group.append(line[:-1])

    if(len(elf_group) == 3):
        first_compar = []
        second_compar = []
        third_compar = []

        first_compar[:0] = elf_group[0]
        second_compar[:0] = elf_group[1]
        third_compar[:0] = elf_group[2]
        common_items.append(abeced.index(list(set(third_compar).intersection(list(set(first_compar).intersection(second_compar))))[0]) + 1)
        group_count = 0
        elf_group = []

print(sum(common_items))