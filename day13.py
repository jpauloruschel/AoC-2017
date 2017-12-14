# Disclaimer: this is slow. VERY slow. It took 13 minutes in my potato laptop.

class Layer:
    def __init__(self, depth, rge):
        self.depth = depth
        self.rge = rge
        self.reset()
    def update(self):
        if self.rge > 0:
            self.scanner = self.scanner + self.velocity
            if self.scanner == 0:
                self.velocity = 1
            if self.scanner == self.rge - 1:
                self.velocity = -1
    def reset(self):
        self.scanner = 0
        self.current = False
        self.velocity = 1
    def save(self):
        self.save_scanner = self.scanner
        self.save_current = self.current
        self.save_velocity = self.velocity
    def load(self):
        self.scanner = self.save_scanner
        self.current = self.save_current
        self.velocity = self.save_velocity
    def __repr__(self):
        if self.current:
            return "(" + str(self.depth) + ", " + str(self.rge) + ": " + str(self.scanner) + ")"
        else:
            return "[" + str(self.depth) + ", " + str(self.rge) + ": " + str(self.scanner) + "]"

layers = [] # array of layers
index = 0

for line in open('input-day13.txt', 'r').readlines():
    words = line.strip('\n').split(' ')
    depth = int(words[0].strip(':'))
    rge = int(words[1])
    while index < depth:
        layers.append(Layer(index, 0))
        index = index + 1
    layers.append(Layer(index, rge))
    index = index + 1

# return hits, severity
def calculate_run(do_break):
    for layer in layers:
        layer.save()
    position = 0
    hits = 0
    severity = 0
    while position < len(layers):
        layers[position].current = True

        # 1 check current position
        if layers[position].scanner == 0 and layers[position].rge > 0:
            severity = severity + (layers[position].depth * layers[position].rge)
            hits = hits + 1
            if do_break:
                break

        # 2 update all layers
        for i in range(position, len(layers)):
            layers[i].update()

        # move
        position = position + 1
    for layer in layers:
        layer.load()
    return hits, severity

print("Severity without delay: " + str(calculate_run(False)[1]))

for layer in layers:
    layer.reset()

delay = 0
while True:
    if delay % 1000 == 0:
        print("Delay: " + str(delay))
    if calculate_run(True)[0] == 0:
        break
    for layer in layers:
        layer.update()
    delay = delay + 1

print("Minimum delay: " + str(delay))
