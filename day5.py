file = open('input-day5.txt','r')

memory = []

for line in file.readlines():
    memory.append(int(line))

current_instruction = 0
total_instructions = 0

while current_instruction < len(memory):
    new_instrution = current_instruction + memory[current_instruction]
    memory[current_instruction] = memory[current_instruction] + 1
    current_instruction = new_instrution
    total_instructions = total_instructions + 1

print (total_instructions)

file = open('input-day5.txt','r')

memory = []

for line in file.readlines():
    memory.append(int(line))

current_instruction = 0
total_instructions = 0

while current_instruction < len(memory):
    new_instrution = current_instruction + memory[current_instruction]
    if (memory[current_instruction] >= 3):
        memory[current_instruction] = memory[current_instruction] - 1
    else:
        memory[current_instruction] = memory[current_instruction] + 1
    current_instruction = new_instrution
    total_instructions = total_instructions + 1

print (total_instructions)
