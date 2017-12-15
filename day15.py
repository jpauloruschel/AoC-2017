
factor_a = 16807
factor_b = 48271
def produce_next(previous, factor):
    return (previous * factor) % 2147483647

def produce_next_2(previous, factor, modulus):
    value = modulus-1
    while value % modulus > 0:
        value = (previous * factor) % 2147483647
        previous = value
    return value

# input
previous_a = 289
previous_b = 629

count = 0
#for i in range(0, 40000000): # part 1
for i in range(0, 5000000): #part 2
    if i % 100000 == 0:
        print(str(i) + " = " + str(count))
    #part1
    #current_a = produce_next(previous_a, factor_a)
    #current_b = produce_next(previous_b, factor_b)

    #part2
    current_a = produce_next_2(previous_a, factor_a, 4)
    current_b = produce_next_2(previous_b, factor_b, 8)

    check_a = current_a % 65536
    check_b = current_b % 65536

    if check_a == check_b:
        count = count + 1

    previous_a = current_a
    previous_b = current_b

print(count)
