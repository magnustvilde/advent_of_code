def createReports() -> list:
    with open('2/second.txt', 'r+') as r:
        reports = [[int(level) for level in line.strip('\n').split(' ')] for line in r.readlines()]
    return reports


def validReports(reports) -> int:
    count = 0
    invalid = []
    for report in reports:
        if report[1] > report[0]:
            if validASC(report):
                count += 1
        elif validDESC(report):
            count += 1
        else: 
            invalid.append(report)
    print('--- --- --- INVALID REPORTS --- --- ---')
    for item in invalid:
        print(item)
    return count

def validASC(report) -> bool:
    if 
    for index in range(len(report)-1):
        diff = report[index+1] - report[index]
        if diff < 1 or diff > 3:
            return problemDampenerASC(report, index+1)
    # returns true if the report is safe without the problem dampener
    return True

def validDESC(report) -> bool:
    for index in range(len(report)-1):
        diff = report[index+1] - report[index]
        if diff > -1 or diff < -3:
            return problemDampenerDESC(report, index+1)
    # returns true if the report is safe without the problem dampener
    return True


def problemDampenerASC(report, index):
    removed = report.pop(index)
    for i in range(len(report)-1):
        diff = report[i+1] - report[i]
        if diff < 1 or diff > 3:
            print(f'{report}\t-\tUNSAFE with Problem Dampener!')
            return False
    print(f'Valid: {report} \tRemoved: {removed}, {index}')
    return True

def problemDampenerDESC(report, index):
    removed = report.pop(index)
    for i in range(len(report)-1):
        diff = report[i+1] - report[i]
        if diff > -1 or diff < -3:
            print(f'{report}\t-\tUNSAFE with Problem Dampener!')
            return False
    print(f'Valid: {report} \tRemoved: {removed}, {index}')
    return True


REPORTS = createReports()

print(validReports(REPORTS))
