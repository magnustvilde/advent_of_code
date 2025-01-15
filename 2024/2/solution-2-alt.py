def createReports() -> list:
    with open('2/second.txt', 'r+') as r:
        reports = [[int(level) for level in line.strip('\n').split(' ')] for line in r.readlines()]
    return reports


def validReports(reports) -> int:
    count = 0
    invalid = []
    for report in reports:
        if valid(report):
            if(report[1] > report[0]):
                for i in range(len(report)-1):
                    if report[i+1]> report[i]:
                        continue
                    else:
                        break
                count += 1
        elif problemDampener(report):
            count += 1
    return count

def valid(report) -> bool:
    copy = report[::]
    copy.sort()
    return copy == report or copy.reverse() == report

def problemDampener(report):
    for i in range(len(report)):
        copy = report[::]
        removed = copy.pop(i)
        if valid(copy):
            print(f'NOT VALID: {report}')
            print(f'VALID: {copy}')
            print(f'REMOVED: {removed}')
            return True
    return False

    # for element in report:
    
    #     dampened = [item for item in report if item != element]
    #     if valid(dampened):
    #          return True
    # print(report)
    # return False

REPORTS = createReports()

print(validReports(REPORTS))
