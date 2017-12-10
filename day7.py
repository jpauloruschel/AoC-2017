file = open('input-day7.txt','r')

class Program:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.sub_names = []
        self.sub_programs = []
        self.sub_weights = []
        self.aggregate_weight = weight
        self.parent = None

    def ToString(self, ident=0):
        children_string = " " + str(len(self.sub_programs))
        if children_string > 0:
            children_string = children_string + "\n"
        for sub in self.sub_programs:
            for i in range(0, ident):
                children_string = children_string + ".."
            children_string = children_string + sub.ToString(ident+1)
        return self.name + " (" + str(self.weight) + ", " + str(self.aggregate_weight) + "): " + children_string

programs = []

for line in file.readlines():
    words = line.split()
    n_program = Program(words[0], int(words[1].strip("()")))
    for i in range(3, len(words)):
        n_program.sub_names.append(words[i].strip(","))

    programs.append(n_program)

for program in programs:
    for sub_program_name in program.sub_names:
        for sub_program in programs:
            if sub_program.name == sub_program_name:
                program.sub_programs.append(sub_program)
                sub_program.parent = program

root = None
for program in programs:
    #print(program.name + " (" + str(program.weight) + ") -> " + str(len(program.sub_programs)) + ", " + str(len(program.sub_names)))
    if program.parent == None:
        root = program
        print("Found root: " + program.name)

def calculate_weights(node):
    for sub in node.sub_programs:
        sub_weight = calculate_weights(sub)
        node.aggregate_weight = node.aggregate_weight + sub_weight
        node.sub_weights.append(sub_weight)
    return node.aggregate_weight

calculate_weights(root)

def find_unbalance(node):
    value = -1
    for i in range(0, len(node.sub_weights)):
        if value == -1:
            value = node.sub_weights[i]
            continue
        if node.sub_weights[i] != value:
            return find_unbalance(node.sub_programs[i])
    print(program.name + " (" + str(program.weight) + ") -> " + str(program.sub_names) + ", " + str(program.sub_weights))
find_unbalance(root)

for program in programs:
    value = -1
    for i in range(0, len(program.sub_weights)):
        if value == -1:
            value = program.sub_weights[i]
            continue
        if program.sub_weights[i] != value:
            print("FOUND\n")
            print(program.ToString())
            break
