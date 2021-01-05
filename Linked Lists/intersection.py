# Given two (singly) linked lists, determine if the two lists intersect.
# Return the inter­secting node.

from linked_list import *


def intersection(list1, list2):

    shorter = list1 if list1.list_length() < list2.list_length() else list2
    longer = list2 if list1.list_length() < list2.list_length() else list1

    len_shorter, len_longer = shorter.list_length(), longer.list_length()
    curr_longer, curr_shorter = longer.head, shorter.head

    for _ in range(len_longer - len_shorter):
        curr_longer = curr_longer.next

    while curr_shorter is not curr_longer:
        curr_longer = curr_longer.next
        curr_shorter = curr_shorter.next

    return curr_shorter.data


A = Node(7)
B = Node(2)
C = Node(1)

first_list = LinkedList()
first_list.append(3)
first_list.append(1)
first_list.append(5)
first_list.append(9)
first_list.append(A)
first_list.append(B)
first_list.append(C)


second_list = LinkedList()
second_list.append(4)
second_list.append(6)
second_list.append(A)
second_list.append(B)
second_list.append(C)

print(intersection(first_list, second_list))
