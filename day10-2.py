import copy

file = open('input-day10.txt','r')

SIZE = 256

sparse_hash = [0] * SIZE
for i in range(0,SIZE):
    sparse_hash[i] = i
current_pos = 0
skip_size = 0
lengths = []

for line in file.readlines():
    for char in line:
        if ord(char) > 32:
            lengths.append(ord(char))
lengths.append(17)
lengths.append(31)
lengths.append(73)
lengths.append(47)
lengths.append(23)

def Reverse(array, begin, length):
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

for i in range(64):
    for length in lengths:
        Reverse(sparse_hash, current_pos, length)
        current_pos = current_pos + length + skip_size
        current_pos = current_pos % SIZE
        skip_size = skip_size + 1

dense_hash = []
for i in range(16):
    value = 0
    for j in range(16):
        value = value ^ sparse_hash[(i*16) + j]
    dense_hash.append(value)

dense_hash_string = ""
for value in dense_hash:
    current = hex(value)[2:]
    if len(current) == 1:
        dense_hash_string = dense_hash_string + "0"
    dense_hash_string = dense_hash_string + current
print(dense_hash_string)
