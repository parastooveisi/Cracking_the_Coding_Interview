# Given a singly linked list, write a function to swap elements pairwise.

# nput: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> NULL
# Output: 2 -> 1 -> 4 -> 3 -> 6 -> 5 -> NULL

# Input: 1 -> 2 -> 3 -> 4 -> 5 -> NULL
# Output: 2 -> 1 -> 4 -> 3 -> 5 -> NULL


class Node():

    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList():

    def __init__(self):
        self.head = None

    def printList(self):
        curr = self.head
        while curr:
            print(curr.value)
            curr = curr.next

    def append(self, value):
        newNode = Node(value)

        if self.head is None:  # if the list is empty
            self.head = newNode
            return

        lastNode = self.head
        while lastNode.next:
            lastNode = lastNode.next

        lastNode.next = newNode

    def swap_pairs(self):
        curr = self.head

        if curr is None:
            return

        while curr and curr.next:

            if(curr.value == curr.next.value):
                curr = curr.next.next

            else:
                curr.value, curr.next.value = curr.next.value, curr.value
                curr = curr.next.next


lList = LinkedList()
lList.append("A")
lList.append("A")
lList.append("C")
lList.append("D")


lList.printList()
print("-------")
lList.swap_pairs()
lList.printList()
