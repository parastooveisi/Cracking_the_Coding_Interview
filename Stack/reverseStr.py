from stack import Stack


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
