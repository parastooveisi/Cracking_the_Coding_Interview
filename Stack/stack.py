class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def getStack(self):
        return self.items

    def isEmpty(self):
        return items == []

    def whatIsTheTop(self):
        if not self.isEmpty():
            return self.items[-1]


s = Stack()
s.push("A")
s.push("B")
s.push("C")
print(s.getStack())

s.pop()
print(s.getStack())

print(s.whatIsTheTop())
