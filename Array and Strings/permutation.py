# o(n)
def permutation(inputStr1, inputStr2):
    inputStr1, inputStr2 = inputStr1.lower(), inputStr2.lower()
    if len(inputStr1) != len(inputStr2):
        return False

    hashMap1 = {}
    hashMap2 = {}
    for char in inputStr1:
        hashMap1[char] = inputStr1.count(char)

    for char in inputStr2:
        hashMap2[char] = inputStr2.count(char)

    return hashMap1 == hashMap2


print(permutation("abcd", "dabc"))  # True
print(permutation("God", "dog"))  # True
print(permutation("Not", "top"))  # False
