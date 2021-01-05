# Write code to partition a linked list around a value x, such that all nodes less than x come before all nodes greater than or equal to x.
# Input: Output: 3  ->  5  ->  8  ->  5  ->  10  ->  2  ->  1 [partition= 5]
# 3  ->  1  ->  2  ->  10  ->  5  ->  5  ->  8

from linked_list import LinkedList


def partition(llist, key):
    lower_list = LinkedList()
    heigher_list = LinkedList()
    curr = llist.head

    while curr:
        if curr.value < key:
            lower_list.append(curr.value)
            lower_list_last = curr

        elif curr.value >= key:
            heigher_list.append(curr.value)

        curr = curr.next

    lower_list_last = lower_list.head
    while lower_list_last.next:
        lower_list_last = lower_list_last.next

    lower_list_last.next = heigher_list.head

    lower_list.printList()


llist = LinkedList()
llist.append(3)
llist.append(5)
llist.append(8)
llist.append(5)
llist.append(10)
llist.append(2)
llist.append(1)

partition(llist, 5)
