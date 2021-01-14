

class minStack:
    def __init__(self):
        self.min_values = []
        self.stack = []

    def push(self, value):
        self.stack.append(value)
        if self.min_values == [] or value <= self.minimum():
            self.min_values.append(value)

    def pop(self):
        if self.min_values[-1] == self.stack[-1]:
            return self.min_values.pop()
        return self.stack.pop()

    def minimum(self):
        return (self.min_values[-1])


s = minStack()
s.push(4)
s.push(7)
s.push(3)
s.push(1)
s.pop()
s.pop()
print(s.minimum())
