class setOfStacks:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stacks = [[]]

    def push(self, value):
        if len(self.stacks[-1]) == 0 or len(self.stacks[-1]) < self.capacity:
            self.stacks[-1].append(value)
        else:
            self.stacks.append([value])

    def pop(self):
        self.stacks[-1].pop()
        if len(self.stacks[-1]) == 0:
            self.stacks.pop()

    def popAt(self, index):
        self.stacks[index].pop()
        if len(self.stacks[index]) == 0 or index < 1:
            self.stacks.pop()

    def print_stacks(self):
        return self.stacks


s = setOfStacks(3)
s.push(10)
s.push(3)
s.push(5)
s.push(10)
s.push(45)
s.push(4)
s.push(4)

print(s.print_stacks())
s.popAt(1)
print(s.print_stacks())
