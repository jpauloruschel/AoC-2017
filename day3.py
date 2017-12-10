import sys

input = 265149

w, h = 8000, 8000;
matrix = [[0 for x in range(w)] for y in range(h)]

center_x = int(w/2)
center_y = int(h/2)

current_value = 1
current_x = center_x
current_y = center_y

v_x = 1
v_y = 0

left = current_x - 1
right = current_x + 1
top = current_y + 1
bottom = current_y - 1

while current_value < input:

    matrix[current_x][current_y] = current_value

    current_x = current_x + v_x
    current_y = current_y + v_y

    if current_x == right:
        v_x = 0
        v_y = 1
        right = right + 1
    else:
        if current_y == top:
            v_x = -1
            v_y = 0
            top = top + 1
        else:
            if current_x == left:
                v_x = 0
                v_y = -1
                left = left - 1
            else:
                if current_y == bottom:
                    v_x = 1
                    v_y = 0
                    bottom = bottom - 1

    current_value = current_value + 1

matrix[current_x][current_y] = current_value

for i in range(center_x - 5, center_x + 5):
    for j in range(center_y - 5, center_y + 5):
        sys.stdout.write(str(matrix[i][j]))
        sys.stdout.write('\t')
        sys.stdout.flush()
    print("")

distance = abs(current_x - center_x) + abs(current_y - center_y)
print(distance)
