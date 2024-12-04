def createReports() -> list:
    with open('2/second.txt', 'r+') as r:
        reports = [[int(level) for level in line.strip('\n').split(' ')] for line in r.readlines()]
    return reports


def validReports(reports) -> int:
    count = 0
    for report in reports:
        if report[1] > report[0]:
            if validASC(report):
                count += 1
        elif validDESC(report):
            count += 1
    return count

def validASC(rep) -> bool:
    for index in range(len(rep)-1):
        diff = rep[index+1] - rep[index]
        if diff < 1 or diff > 3:
            print(f'ASC {rep[index]} - {rep[index+1]}')
            print(f'DIFF IS NOT ASC: {diff}')
            return False
    # print('Valid asc report.')
    return True

def validDESC(rep) -> bool:
    for index in range(len(rep)-1):
        diff = rep[index+1] - rep[index]
        if diff > -1 or diff < -3:
            print(f'DESC {rep[index]} - {rep[index+1]}')
            print(f'DIFF IS NOT DESC: {diff}')
            return False
    # print('Valid desc report.')
    return True

REPORTS = createReports()

print(validReports(REPORTS))
