# Given a string, write a function to check if it is a permutation of a palin­drome.
# A palindrome is a word or phrase that is the same forwards and backwards
# A permutation is a rearrangement of letters


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
