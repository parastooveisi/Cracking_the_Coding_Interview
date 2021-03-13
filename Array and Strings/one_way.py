# Given two strings, write a function to check if they are one edit (or zero edits) away.


def one_way(s1, s2):
    len_s1 = len(s1)
    len_s2 = len(s2)
    if s1 == s2:
        return True
    if len_s1 == len_s2:
        return replace_edit(s1, s2)
    if len_s1 + 1 == len_s2:
        return insert_edit(s1, s2)
    if len_s1 == len_s2 + 1:
        return insert_edit(s2, s1)

    return False


def replace_edit(s1, s2):
    flag = False
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            if flag:
                return False
            flag = True

    return True


def insert_edit(s1, s2):
    edited = False
    i, j = 0, 0
    while i < len(s1) and j < len(s2):
        if s1[i] != s2[j]:
            if edited:
                return False
            edited = True
            i += 1
        else:
            i += 1
            j += 1
    return True


print(insert_edit("paleabc", "pleabc"))  # Truereact
