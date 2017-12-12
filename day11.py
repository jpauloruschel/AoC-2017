input = open('input-day11.txt', 'r').readlines()[0].strip('\n').split(',')

axial_directions = [
   [+1,  0], [+1, -1], [ 0, -1],
   [-1,  0], [-1, +1], [ 0, +1]
]

def hex_direction(direction):
    return axial_directions[direction]

def hex_neighbor(hex, direction):
    dir = hex_direction(direction)
    return [hex[0] + dir[0], hex[1] + dir[1]]

def hex_distance(a, b):
    return (abs(a[0] - b[0])
          + abs(a[0] + a[1] - b[0] - b[1])
          + abs(a[1] - b[1])) / 2

w, h = 4000, 4000
matrix = [[0 for x in range(w)] for y in range(h)]

start_pos = [w/2, h/2]
position = [w/2, h/2]

max_distance = 0

for direction in input:
    if direction == 'se':
        position = hex_neighbor(position, 0)
    if direction == 'ne':
        position = hex_neighbor(position, 1)
    if direction == 'n':
        position = hex_neighbor(position, 2)
    if direction == 'nw':
        position = hex_neighbor(position, 3)
    if direction == 'sw':
        position = hex_neighbor(position, 4)
    if direction == 's':
        position = hex_neighbor(position, 5)

    distance = hex_distance(start_pos, position)
    if distance > max_distance:
        max_distance = distance

print("Distance from start: " + str(hex_distance(start_pos, position)))
print("Furthest from start: " + str(max_distance))
