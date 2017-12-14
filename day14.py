input_string = "wenycdww"

def knot_hash(m_input):
    SIZE = 256
    sparse_hash = [0] * SIZE
    for i in range(0,SIZE):
        sparse_hash[i] = i
    current_pos = 0
    skip_size = 0
    lengths = []

    for char in m_input:
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
    return dense_hash_string

def bitfield(n):
    return [int(digit) for digit in bin(n)[2:]] # [2:] to chop off the "0b" part

w, h = 128, 128
d_used = [[False for x in range(w)] for y in range(h)]
d_groups = [[0 for x in range(w)] for y in range(h)]

count = 0
for i in range(0, 128):
    m_hash = knot_hash(input_string + "-" + str(i))
    print(m_hash)
    bitmask = bin(int(m_hash, 16))[2:].zfill(128)

    for b in range(0, 128):
        d_groups[i][b] = 0
        if bitmask[b] == '1':
            d_used[i][b] = True
            count = count + 1
        else:
            d_used[i][b] = False

print("Used squares: " + str(count))

def find_group_recursive(i, j, group):
    if i < 0 or j < 0 or i > 127 or j > 127:
        return
    if not d_used[i][j]:
        return
    if d_groups[i][j] > 0:
        return
    d_groups[i][j] = group
    find_group_recursive(i - 1, j, group)
    find_group_recursive(i + 1, j, group)
    find_group_recursive(i, j - 1, group)
    find_group_recursive(i, j + 1, group)

current_group = 1
for i in range(0, 128):
    for j in range(0, 128):
        if not d_used[i][j]:
            continue
        if d_groups[i][j] == 0:
            find_group_recursive(i, j, current_group)
            current_group = current_group + 1

print("Total groups: " + str(current_group-1))
