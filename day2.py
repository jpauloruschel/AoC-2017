file = open('input-day2.txt','r')
sum = 0

for line in file.readlines():
    row_min = 99999999
    row_max = 0
    for number in line.split('\t'):
        if int(number) > row_max:
            row_max = int(number)
        if int(number) < row_min:
            row_min = int(number)
    sum += row_max - row_min

print(sum)

file = open('input-day2.txt','r')
sum = 0

for line in file.readlines():
    for number1 in line.split('\t'):
        for number2 in line.split('\t'):
            if int(number1) != int(number2):
                if int(number1) % int(number2) == 0:
                    sum += int(number1) / int(number2)

print(sum)
