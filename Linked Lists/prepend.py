class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next

    def prepend(self, value):
        newNode = Node(value)
        newNode.next = self.head
        self.head = newNode


lList = LinkedList()
lList.prepend("A")
lList.prepend("B")
lList.prepend("C")
lList.printList()
