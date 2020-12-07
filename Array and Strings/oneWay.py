# Given two strings, write a function to check if they are one edit (or zero edits) away.


def oneWay(s1, s2):
    hashMap1 = {}
    hashMap2 = {}
    count = 0

    for char in s1:
        hashMap1[char] = s1.count(char)

    for char in s2:
        hashMap2[char] = s2.count(char)

    for key in hashMap1:
        if key not in hashMap2:
            count += 1
    return count == 1 or count == 0


print(oneWay("pale", "ple"))  # True
print(oneWay("pales", "pale"))  # True
print(oneWay("pale", "bale"))  # True
print(oneWay("pale", "bake"))  # False
