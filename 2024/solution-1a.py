def configureInput() -> tuple:
    # sort the lists
    with open('input.txt','r+') as r:
        lines = [line.strip('\n') for line in r.readlines()]
        left = sorted([int(line[0:5]) for line in lines])
        right = sorted([int(line[8:13]) for line in lines])
    return (left, right)

def compareLists(list1, list2) -> int:
    total = 0
    # compare each index
    for index in range(len(list1)):
        # measure difference
        diff = abs(list1[index] - list2[index])
        # add to total diff
        total += diff
    return total

LEFT, RIGHT =  configureInput()
TOTAL = compareLists(LEFT, RIGHT)
print(TOTAL)


# unsort left list AND right list

# check how many times left list index appears in right list 
