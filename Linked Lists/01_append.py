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


lList = LinkedList()
lList.append("A")
lList.append("B")
lList.printList()
