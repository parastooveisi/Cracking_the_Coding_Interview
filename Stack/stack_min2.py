
class minStack:
    def __init__(self):
        self.min_value = None
        self.values = []

    def push(self, data):
        if not self.min_value or data < self.min_value:
            self.min_value = data

        self.values.append((data, self.min_value))

    def pop(self):
        return self.values.pop()

    def get_minimum(self):
        return self.values[-1][1]


s = minStack()
s.push(7)
s.push(4)
print(s.get_minimum())
s.push(6)
s.push(3)
print(s.get_minimum())
s.pop()
print(s.get_minimum())
