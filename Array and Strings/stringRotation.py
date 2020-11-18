def stringrotation(s1, s2):
    hashMap1 = {}
    hashMap2 = {}

    for char in s1:
        hashMap1[char] = s1.count(char)

    for char in s2:
        hashMap2[char] = s2.count(char)

    return hashMap1 == hashMap2


print(stringrotation("waterbottle", "erbottlewat"))
