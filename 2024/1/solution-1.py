def configureInput() -> tuple:
    with open('input-1.txt','r+') as r:
        lines = [line.strip('\n') for line in r.readlines()]
        left = [int(line[0:5]) for line in lines]
        right = [int(line[8:13]) for line in lines]
    return (left, right)

def compareLists(list1, list2) -> int:
    # sort the lists
    list1, list2 = sorted(list1), sorted(list2)
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

def similarityScore(list1, list2) -> int:
    score = 0
    for item in list1:
        # check how many times left list index appears in right list
        count = list2.count(item)
        # multiply left list NUMBER by right list COUNT
        score += count * item
        # add to total 
    return score

print(similarityScore(LEFT, RIGHT))