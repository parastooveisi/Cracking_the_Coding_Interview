class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def isEmpty(self):
        return self.items == []

    def getStack(self):
        return self.items

    def last(self):
        if not self.isEmpty():
            return self.items[-1]


def balance(p1, p2):
    return True if p1+p2 in ['()', '[]', '{}'] else False


def checkBalance(inputStr):
    s = Stack()
    flag = True

    for char in inputStr:
        if char in "({[":
            s.push(char)

        else:
            if s.isEmpty():
                return False

            else:
                top = s.pop()
                if balance(char, top):
                    flag = True

    return s.isEmpty() and flag


print(checkBalance("))"))
