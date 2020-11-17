def palindromePermutation(inputStr):
    inputStr = inputStr.lower().replace(" ", "")
    hashMap = {}
    oddCounter = 0
    for char in inputStr:
        hashMap[char] = inputStr.count(char)

    for key in hashMap:
        if hashMap[key] % 2 != 0:
            oddCounter += 1

    return oddCounter == 0 or oddCounter == 1


print(palindromePermutation("this is not"))  # False
print(palindromePermutation("Tact Coa"))  # True
