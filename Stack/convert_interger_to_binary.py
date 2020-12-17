# convert integar to binary
# 242 /2 = 121 -> 0
# 121 /2 = 60 -> 1
# 60 /2 = 30 -> 0
# 30 /2 = 15 -> 1
# 15 /2 = 7 -> 1
# 7 /2 = 3 -> 1
# 7 /2 = 3 -> 1
# 3 /2 = 1 -> 1
# 1 /2 = 0 -> 1


from stack import Stack


def div_by_2(num):
    s = Stack()

    while num > 0:
        s.push(num % 2)
        num = num // 2

    result = ""
    while not s.isEmpty():
        result = result + str(s.pop())

    return result


div_by_2(242)
