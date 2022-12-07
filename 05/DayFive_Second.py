myinput_file = open('./05/myinput.txt', 'r').read().splitlines()
procedure = open('./05/procedure.txt', 'r').read().splitlines()

initial_crates = []
sorted_crates = []
line_array = []
count = 0
result = ''


def sortInitialCrates(input_crates):

    for crate in input_crates:
        for item in range(len(crate)):
            
            if(len(sorted_crates) != len(crate)):
                sorted_crates.append([])
                if(crate[item] == ' '):
                    continue
                sorted_crates[item].insert(0,crate[item])
            else:
                if(crate[item] == ' '):
                    continue
                sorted_crates[item].insert(0,crate[item])
    #print(sorted_crates)

for line in myinput_file:
    for letter in line:
    
            if(letter == ' ' and count < 4):
                count += 1
            if(letter == ' ' and count == 4):
                line_array.append(' ')
                count = 0
            if(letter != ' '):
                count = 0
                if(letter == '[' or letter == ']'):
                    continue
                else:
                    line_array.append(letter)
    initial_crates.append(line_array)
    line_array = []

initial_crates.pop()
sortInitialCrates(initial_crates)
#print(initial_crates)

def crateOperation(crates_count, source_crate, target_crate):
    crates_to_move = []
    for i in range(crates_count):
        crates_to_move.append(sorted_crates[source_crate][len(sorted_crates[source_crate])-1])
        sorted_crates[source_crate].pop(len(sorted_crates[source_crate])-1)
    #print(sorted_crates)
    #print(crates_to_move)
    crates_to_move.reverse()
    #print(crates_to_move)
    for item in crates_to_move:
        sorted_crates[target_crate].append(item)
        #print(sorted_crates)
    

for procedure_line in procedure:
    procedure_simplified = procedure_line.split(' ')
    crateOperation(int(procedure_simplified[1]), int(procedure_simplified[3])-1, int(procedure_simplified[5])-1)

for crate in sorted_crates:
    if(crate == []):
        continue
    crate.reverse()
    result += crate[0]
print(result)