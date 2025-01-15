calibrationdata = open("numbers.txt").readlines()

numbers = []

textnums = {
    'one': 'o1e',
    'two': 't2o',
    'three': 't3e',
    'four': 'f4r',
    'five': 'f5e',
    'six': 's6x',
    'seven': 's7n',
    'eight': 'e8t',
    'nine': 'n9e'
}

for line in calibrationdata:
    digits = []

    for key, value in textnums.items():
        line = line.replace(key, value)

    for letter in line:
        if letter.isdigit():
            digits.append(letter)

    numbers.append(int(digits[0] + digits[len(digits)-1]))

numbers = sum(numbers)
print(numbers)