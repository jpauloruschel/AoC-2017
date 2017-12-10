file = open('input-day9.txt','r')
input = file.readlines()[0]

ignore_next = False
is_garbage = False
in_group = False

current_level = 0
score = 0
removed_garbage = 0

for char in input:
    if ignore_next:
        ignore_next = False
        continue

    if char == '!':
        ignore_next = True
        continue

    if is_garbage:
        if char == '>':
            is_garbage = False
            continue
        removed_garbage = removed_garbage + 1
    else:
        if char == '<':
            is_garbage = True

        if char == '{':
            current_level = current_level + 1

        if char == '}':
            score = score + current_level
            current_level = current_level - 1

print ("Score: " + str(score))
print ("Removed garbage: " + str(removed_garbage))
