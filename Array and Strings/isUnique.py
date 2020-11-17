def isUnique(inputStr):
    hashMap = {}

    for char in inputStr:
        hashMap[char] = inputStr.count(char)

    for value in hashMap:
        if hashMap[value] > 1:
            return False

    return True


print(isUnique("helo"))
