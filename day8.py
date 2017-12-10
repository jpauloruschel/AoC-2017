file = open('input-day8.txt','r')

registers = {}

max_value_during = 0
for line in file.readlines():
    words = line.split()

    op_register = words[0]
    op_op = words[1]
    op_value = int(words[2])
    check_register = words[4]
    check_cond = words[5]
    check_value = int(words[6])

    perform_op = False

    # first, do the check
    try:
        current_register_value = registers[check_register]
    except KeyError:
        current_register_value = 0
        pass

    if check_cond == '>':
        if current_register_value > check_value:
            perform_op = True
    if check_cond == '<':
        if current_register_value < check_value:
            perform_op = True
    if check_cond == '<=':
        if current_register_value <= check_value:
            perform_op = True
    if check_cond == '>=':
        if current_register_value >= check_value:
            perform_op = True
    if check_cond == '==':
        if current_register_value == check_value:
            perform_op = True
    if check_cond == '!=':
        if current_register_value != check_value:
            perform_op = True

    #perform_op
    current_op_register_value = registers.get(op_register, 0)
    if perform_op:
        if op_op == 'inc':
            registers[op_register] = current_op_register_value + op_value
        if op_op == 'dec':
            registers[op_register] = current_op_register_value - op_value
        if (registers.get(op_register, 0)) > max_value_during:
            max_value_during = (registers.get(op_register, 0))

max_value = 0
for register in registers:
    if registers[register] > max_value:
        max_value = registers[register]
print("Max value in the end is: " + str(max_value))
print("Max value during is: " + str(max_value_during))
