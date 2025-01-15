with open('input.txt','r') as o:
    lines = o.readlines()
currentElf, myElves, elvNum = 0, {}, 0

for line in lines:
    line = line.strip('\n')
    if line:
        currentElf += int(line)
    else:
        elvNum+=1
        myElves[elvNum] = currentElf
        currentElf = 0

# min_list_comp = [x.strip('\n') for x in lines if x]
def most_cal(remainingElves):
    biggest = 0
    for elf in remainingElves:
        if remainingElves[elf] > biggest:
            biggest = remainingElves[elf]
    return max(remainingElves, key=remainingElves.get), biggest
number, maks = most_cal(myElves)


def top_three(elves_list):
    top_three = []
    for i in range(3):
        number, maks = most_cal(elves_list)
        top_three.append(maks)
        elves_list.pop(number)
    return sum(top_three)

print(top_three(myElves))