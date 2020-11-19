class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.next

    def append(self, data):
        newNode = Node(data)

        if not self.head:
            self.head = newNode
            return

        lastNode = self.head

        while lastNode.next:
            lastNode = lastNode.next

        lastNode.next = newNode

    def deletion(self, key):
        curr = self.head
        if curr.data == key:
            self.head = curr.next
            curr = None
        prev = None
        while curr and curr.data != key:
            prev = curr
            curr = curr.next
        prev.next = curr.next
        curr = None


lList = LinkedList()
lList.append("A")
lList.append("B")
lList.append("C")
lList.append("D")
lList.deletion("B")

lList.printList()
