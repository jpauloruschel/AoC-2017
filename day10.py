import copy

file = open('input-day10.txt','r')

SIZE = 256

array = [0] * SIZE
for i in range(0,SIZE):
    array[i] = i
current_pos = 0
skip_size = 0
lengths = []

for line in file.readlines():
    for word in line.split(','):
        lengths.append(int(word))

def Reverse(begin, length):
    string = "Reverse " + str(begin) + "," + str(length) + ": " + str(array) + " -> "
    for i in range(int(length/2)):
        circular_i = (begin + i) % SIZE
        circular_j = (begin + length - i - 1) % SIZE
        string = string + "(" + str(circular_i) + "," + str(circular_j) + ")"
        temp = array[circular_i]
        array[circular_i] = array[circular_j]
        array[circular_j] = temp
    string = string + " -> " + str(array)
    #print(string)

for length in lengths:
    Reverse(current_pos, length)
    current_pos = current_pos + length + skip_size
    current_pos = current_pos % SIZE
    skip_size = skip_size + 1

print(array[0] * array[1])
