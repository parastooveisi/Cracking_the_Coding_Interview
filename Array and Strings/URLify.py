def URLify(inputStr, length):
    result = ""
    for i in range(length):
        if inputStr[i] == " ":
            result += "%20"
        else:
            result += inputStr[i]

    return result


print(URLify("hello I am     ", 10))
print(URLify("Mr. John Smith", 14))
