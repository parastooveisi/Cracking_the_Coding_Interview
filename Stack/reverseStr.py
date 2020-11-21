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
        return self.items == []


def reverseStr(inputStr):
    s = Stack()
    result = ""
    for char in inputStr:
        s.push(char)

    while not s.isEmpty():
        last = s.pop()
        result += last
    print(result)


reverseStr("hello")
