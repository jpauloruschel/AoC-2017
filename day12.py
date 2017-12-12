class Program:
    def __init__(self):
        self.pipes = [] # array of indices
        self.group_id = 0 # 0 = no group

programs = []

for line in open('input-day12.txt', 'r').readlines():
    words = line.strip('\n').split(' ')

    index = int(words[0])
    if len(programs) < index+1:
        programs.append(Program())

    for i in range(2, len(words)):
        programs[index].pipes.append(int(words[i].strip(',')))

def check_connection(index, id):
    if (programs[index].group_id > 0):
        return 0
    programs[index].group_id = id
    contained = 1
    for pipe in programs[index].pipes:
        contained = contained + check_connection(pipe, id)
    return contained

groups = [] # number of nodes
group_id = 1
current_program = 0
processed_programs = 0
while processed_programs < len(programs):
    groups.append(check_connection(current_program, group_id))
    processed_programs = processed_programs + groups[group_id-1]
    print("In group " + str(group_id) + ", from program  #" + str(current_program) + ": " + str(groups[group_id-1]))
    group_id = group_id + 1

    # find next free program
    for i in range(current_program, len(programs)):
        if programs[i].group_id == 0:
            current_program = i
            break
