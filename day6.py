import copy

file = open('input-day6.txt','r')

current_banks = []
bank_count = 0

for line in file.readlines():
    for word in line.split('\t'):
        current_banks.append(int(word))
        bank_count = bank_count + 1

previous_iterations = []
count = 0

previous_iterations.append(copy.copy(current_banks))

while True:

    rellocation_value = max(current_banks)
    rellocation_index = current_banks.index(rellocation_value)
    current_banks[rellocation_index] = 0

    index = (rellocation_index + 1) % bank_count
    while rellocation_value > 0:
        current_banks[index] = current_banks[index] + 1
        rellocation_value = rellocation_value - 1
        index = (index + 1) % bank_count

    find = False
    found_index = 0
    for p in range(0, len(previous_iterations)):
        equal = True
        for i in range(0, bank_count):
            if current_banks[i] != previous_iterations[p][i]:
                equal = False
                break
        if equal:
            found_index = p
            find = True
            break

    previous_iterations.append(copy.copy(current_banks))
    count = count + 1

    if find:
        print("Found current previously " + str(count - found_index) + " iterations ago")
        break

print ("Count: " + str(count))
